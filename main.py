import os


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




file_path = os.path.join(os.path.dirname(__file__), "files/berlin11_modified.tsp")
start_line = "NODE_COORD_SECTION\n"
end_line = "EOF\n"

id_num, x, y = parse_tsp(file_path, start_line, end_line)
print(f"Ordering number: {id_num}")
print(f"x: {x}")
print(f"y: {y}")