import os
import math
import random
import numpy as np
import matplotlib.pyplot as plt

# Configuration
start_city = 2
tsp_file_name = input("Enter file name: ")
# tsp_file_name = "berlin52" # For testing only
file_path = os.path.join(os.path.dirname(__file__), f"files/{tsp_file_name}.tsp")

# Functions
def parse_tsp(file_path):
    start_marker = "NODE_COORD_SECTION\n"
    end_marker = "EOF\n"
    city_ids = []
    x_coords = []
    y_coords = []

    parsing = False

    with open(file_path, "r") as file:
        for line in file:
            if start_marker in line:
                parsing = True
                continue
            if parsing and end_marker in line:
                break

            if parsing:
                parts = line.strip().split()
                city_ids.append(int(parts[0]))
                x_coords.append(float(parts[1]))
                y_coords.append(float(parts[2]))
    return city_ids, x_coords, y_coords

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def generate_random_path(city_ids):
    path = city_ids.copy()
    random.shuffle(path)
    path.append(path[0])
    return path

def calculate_path_distance(path, x_coords, y_coords):
    total_distance = 0
    for i in range(len(path) - 1):
        x1, y1 = x_coords[path[i] - 1], y_coords[path[i] - 1]
        x2, y2 = x_coords[path[i + 1] - 1], y_coords[path[i + 1] - 1]
        total_distance += calculate_distance(x1, y1, x2, y2)
    return total_distance

def info(path):
    return " → ".join([str(city) for city in path])

def generate_greedy_path(start_city, city_ids, x_coords, y_coords):
    path = [start_city]
    while len(path) != len(city_ids):
        next_city = -1
        shortest_distance = float("inf")
        for city in city_ids:
            if city not in path:
                distance = calculate_distance(
                    x_coords[path[-1] - 1], y_coords[path[-1] - 1],
                    x_coords[city - 1], y_coords[city - 1]
                )
                if distance < shortest_distance:
                    shortest_distance = distance
                    next_city = city
        path.append(next_city)
    path.append(start_city)
    return path

def initialize_population(city_ids, size, greedy_percentage):
    population = []
    
    while len(population) < size:
        if random.random() < greedy_percentage:

            start_city = random.choice(city_ids)
            population.append(generate_greedy_path(start_city, city_ids, x_coords, y_coords))
        else:
            population.append(generate_random_path(city_ids))
    
    return population


def display_population_statistics(population):
    population_size = len(population)
    best_path_distance = min(calculate_path_distance(path, x_coords, y_coords)for path in population)
    median_distance = np.median([calculate_path_distance(path, x_coords, y_coords) for path in population])
    worst_path_distance = max(calculate_path_distance(path, x_coords, y_coords) for path in population)
    best_path = info(population[0])

    print(f"Population Size: {population_size}")
    print(f"Best Path Distance: {best_path_distance:.2f}")
    print(f"Worst Path Distance: {worst_path_distance:.2f}")
    print(f"Median Path Distance: {median_distance:.2f}")
    print(f"Path: {best_path}")
    
def tournament_selection(population, tournament_size):
    selected_paths = random.sample(population, tournament_size)
    smallest_distance = float('inf')
    smallest_path = []
    for path in selected_paths:
        path_distance = calculate_path_distance(path, x_coords, y_coords)
        if path_distance < smallest_distance:
            smallest_distance = path_distance
            smallest_path = path
    return smallest_path

def crossover(parent1, parent2):
    
    child = [None] * len(parent1)  
    
    parent1 = parent1[:-1]
    parent2 = parent2[:-1]

    # Random crossover points
    in_point = random.randint(0, len(parent1) - 1)
    out_point = random.randint(0, len(parent1) - 1)

    # Ensure valid range
    if in_point > out_point:
        in_point, out_point = out_point, in_point
    while in_point == out_point:
        in_point = random.randint(0, len(parent1) - 1)
        out_point = random.randint(0, len(parent1) - 1)

    child[in_point:out_point] = parent1[in_point:out_point]

    # Track used values
    used_values = child[in_point:out_point]

    # Fill remaining None values in child with values from parent2
    for index in range(len(child)):
        if child[index] is None:
            for value in parent2:
                if value not in used_values:
                    child[index] = value
                    used_values.append(value)
                    break

    # Wrap around
    child[-1] = child[0]
    
    
    return child

def mutation(child, probability):
    if random.random() <= probability:
        # Select mutation points
        in_point = random.randint(0, len(child) - 2)
        out_point = random.randint(0, len(child) - 2)

        # Ensure in_point is less than out_point
        if in_point > out_point:
            in_point, out_point = out_point, in_point
        while in_point == out_point:
            out_point = random.randint(0, len(child) - 2)
            
        # Reverse the segment
        child[in_point:out_point + 1] = reversed(child[in_point:out_point + 1])
        
        child[-1] = child[0]
    return child

def epoch(initial_population,number_of_epoch, probability, tournament_size):
    epoch_id = 0
    population = initial_population
    best_distance = float("inf")
    epoch_distances = []
    
    while epoch_id < number_of_epoch:
        print(f"\nEpoch {epoch_id}")
        
        # Generate a new population
        new_population = []
        while len(new_population) < len(population):
            parent1 = tournament_selection(population, tournament_size)
            parent2 = tournament_selection(population, tournament_size)
            child = mutation(crossover(parent1, parent2), probability)
            new_population.append(child)
        
        # Evaluate and update best distance
        current_best_distance = min(calculate_path_distance(path, x_coords, y_coords) for path in new_population)
        if current_best_distance < best_distance:
            best_distance = current_best_distance
            print(f"New Best Distance: {best_distance:.2f}")
        
        epoch_distances.append(best_distance)
        
        # Update population
        population = new_population
        epoch_id += 1
        
        
        # Display statistics
        display_population_statistics(population)
    # Chart
    plot_epoch_results(epoch_distances)

def plot_epoch_results(epoch_distances):
    """
    Plots the best path distance over epochs.

    Args:
        epoch_distances (list): A list of the best path distances for each epoch.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(epoch_distances, marker='', linestyle='-', color='red', label='Best Path Distance')
    plt.title('Evolution of Best Path Distance Over Epochs', fontsize=14)
    plt.xlabel('Epoch', fontsize=12)
    plt.ylabel('Best Path Distance', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()
# Executing Functions
city_ids, x_coords, y_coords = parse_tsp(file_path)

def run():
    population_size = int(input("Specify size of the population: "))
    tournament_size = int(input("Specify size of the tournament: "))
    number_of_epoch = int(input("Specify number of epochs: "))
    probability = int(input("Mutation Probability %: "))
    greedy_percentage = int(input("Greedy %: "))
    initial_population = initialize_population(city_ids, population_size, greedy_percentage)
    
    if probability > 1:
        probability = probability / 100
    
    if greedy_percentage > 1:
        greedy_percentage = greedy_percentage / 100
    
    epoch(initial_population, number_of_epoch, probability, tournament_size)
   
run()