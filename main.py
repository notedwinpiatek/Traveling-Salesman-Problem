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
        # print(file.read())
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

def calculate_distance(x1, x2, y1, y2):
    result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return result

def random_solution(id_num):
    solution = list(range(len(id_num)))
    random.shuffle(solution)
    return solution
        

#executing functions 
id_num, x, y = parse_tsp(file_path, start_line, end_line)
distance = calculate_distance(x[0], x[1], y[0], y[1])
random_number = random_solution(id_num)

# printing
print(f"Ordering number: {id_num}")
print(f"x: {x}")
print(f"y: {y}")
print(f"Distance: {distance}")
print(f"Random number: {random_number}")