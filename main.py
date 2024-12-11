import os

file_path = os.path.join(os.path.dirname(__file__), "files/berlin11_modified.tsp")

def parse_tsp(file_path):
    order_number = []
    x_cord = []
    y_cord = []
    
    with open(file_path, "r") as file:
        # print(file.read())
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                order_number.append(int(parts[0]))
                x_cord.append(float(parts[1]))
                y_cord.append(float(parts[2]))
    return order_number, x_cord, y_cord





# parse_tsp(file_path)
id_num, x, y = parse_tsp(file_path)
print(id_num)
print(y)
print(x)