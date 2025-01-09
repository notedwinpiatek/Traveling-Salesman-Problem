import os
import math
import random

# Configuration
start_city = 2
tsp_file_name = input("Enter file name: ")

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

def format_path(path):
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

def initialize_population(city_ids):
    population = []
    while len(population) < 100:
        population.append(generate_random_path(city_ids))
    return population

def display_population_statistics(population, x_coords, y_coords):
    population_size = len(population)
    best_path_distance = min(calculate_path_distance(path, x_coords, y_coords) for path in population)
    greedy_path_distance = calculate_path_distance(generate_greedy_path(population[0][0], city_ids, x_coords, y_coords), x_coords, y_coords)
    best_path = format_path(population[0])

    print(f"Population Size: {population_size}")
    print(f"Best Path Distance: {best_path_distance}")
    print(f"Path: {best_path}")
    print(f"Greedy Path Distance: {greedy_path_distance}")

def tournament_selection(population):
    tournament_size = random.randint(1, len(population) - 1)
    selected_paths = random.sample(population, tournament_size)
    selected_paths.append(selected_paths[0])
    return selected_paths

# Executing Functions
file_path = os.path.join(os.path.dirname(__file__), f"files/{tsp_file_name}.tsp")
city_ids, x_coords, y_coords = parse_tsp(file_path)
random_path = generate_random_path(city_ids)
greedy_path = generate_greedy_path(start_city, city_ids, x_coords, y_coords)
# population = initialize_population(city_ids)

# Printing Results
# display_population_statistics(population, x_coords, y_coords)
print(random_path)
