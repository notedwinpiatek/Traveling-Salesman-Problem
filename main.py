import os
import math
import random

file_path = os.path.join(os.path.dirname(__file__), "files/berlin11_modified.tsp")
start_line = "NODE_COORD_SECTION\n"
end_line = "EOF\n"
# functions
def parse_tsp(file_path, start_line, end_line):
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
    solution = list(range(len(id_num)))
    random.shuffle(solution)
    solution.append(solution[0])
    return solution 

def fitness(order, x, y):
    total_distance = 0
    for i in range(len(order) - 2):  # Ensure i + 1 is valid
        x1, y1 = x[order[i]], y[order[i]]
        x2, y2 = x[order[i + 1]], y[order[i + 1]]
        total_distance += calculate_distance(x1, y1, x2, y2)
    return total_distance

def info(solution):
    res = " → ".join([str(sol) for sol in solution])
    return res

def greedy(start):
    pass
    # identify the first element in solution
    # for every element of your list exept for first one
        # find the distance between first element and the one in the loop
        # keep track of the smallest distance
    # add distance calculated to the total distance
    # shift your "first element" to the one that goes next
    # repeat the process of looping throung every elemnt except for "current one"
    
#executing functions 
id_num, x, y = parse_tsp(file_path, start_line, end_line)
distance = calculate_distance(x[0], y[0], x[1], y[1])
random_number = random_solution(id_num)
total_distance = fitness(random_number, x, y)


# printing
print(f"Ordering number: {id_num}")
print(f"x: {x}")
print(f"y: {y}")
print(f"Distance: {round(distance, 3)}")
print(f"Random number: {info(random_number)}")
print(f"Total distance: {round(total_distance, 3)}")
