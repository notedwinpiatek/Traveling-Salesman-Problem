import os
import math
import random

# Configuration
start_point = 2
file_name = input("Enter file name: ")

# functions
def parse_tsp(file_path):
    start_line = "NODE_COORD_SECTION\n"
    end_line = "EOF\n"
    order_number = []
    x_cord = []
    y_cord = []
    
    processing = False
    
    with open(file_path, "r") as file:
        for line in file:
            if start_line in line:
                processing = True
                continue
            if processing and end_line in line:
                break
            
            if processing:
                parts = line.strip().split()
                order_number.append(int(parts[0]))
                x_cord.append(float(parts[1]))
                y_cord.append(float(parts[2]))
    return order_number, x_cord, y_cord

def calculate_distance(x1, y1, x2, y2):
    result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return result

def random_solution(id_num):
    solution = id_num.copy()
    random.shuffle(solution)
    solution.append(solution[0])
    return solution 

def fitness(order, x, y):
    total_distance = 0
    for i in range(len(order) - 1):
        x1, y1 = x[order[i] - 1], y[order[i] - 1]
        x2, y2 = x[order[i + 1] - 1], y[order[i + 1] - 1]
        total_distance += calculate_distance(x1, y1, x2, y2)
    return total_distance

def info(solution):
    res = " → ".join([str(sol) for sol in solution])
    return res

def greedy(start):
    solution = [start]
    while len(solution) != len(id_num):
        next_city = -1
        best_distance = float("inf")
        for city in id_num:
            if city not in solution:
                distance = calculate_distance(x[solution[-1]-1], y[solution[-1]-1], x[city-1], y[city-1])
                if distance < best_distance:
                    best_distance = distance
                    next_city = city
        solution.append(next_city)
    solution.append(start)
    return solution
    
#executing functions 
file_path = os.path.join(os.path.dirname(__file__), f"files/{file_name}.tsp")
id_num, x, y = parse_tsp(file_path)
random_number = random_solution(id_num)
greedy_path = greedy(start_point)



# printing
print(f"Greedy Path: {info(greedy_path)}")
# print(random_number)
# print(greedy_path)
# print(f"Random Distance: {round(fitness(random_number, x, y), 2)}")
print(f"Greedy Distance: {round(fitness(greedy_path, x, y), 2)}")