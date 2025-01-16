# Traveling Salesman Problem (TSP)

This project implements a genetic algorithm to solve the well-known **Traveling Salesman Problem (TSP)**. The TSP involves finding the shortest possible route that visits a set of cities and returns to the origin city. The algorithm uses genetic operations such as **crossover** and **mutation** combined with **tournament selection** to evolve solutions over multiple epochs.

## Features

- **City Data Parsing**: Parses TSP files and extracts city coordinates.
- **Random Path Generation**: Generates random initial paths.
- **Greedy Path Generation**: Generates a path using a greedy approach.
- **Genetic Algorithm**: Applies crossover, mutation, and tournament selection.
- **Population Management**: Maintain a population of the best paths evolving over time.
- **Visualization**: Plots the evolution of the best path distance over epochs.

## Setup

1. **Install Required Libraries**:
   Ensure that you have the required libraries installed by using the following:
   ```bash
   pip install numpy matplotlib
2. **TSP Data Files**:
   The format of the .tsp file should include a section with NODE_COORD_SECTION and the coordinates of each city.

3. **Running the Code**: Execute the script by running the Python file:
   ```bash
   python tsp_genetic_algorithm.py

## Outputs

### Console Outputs:
Best path distance, worst path distance, and median path distance for each epoch.
The best path found during the evolution process.

### Charts:
Evolution of Best Path Distance: A plot showing how the best path distance evolves over the epochs.

Example chart showing the evolution of the best path distance over 1000 epochs.
![1000Chart](/Report/1000Chart.png)

### Example of Outputs:
After the genetic algorithm runs, you’ll see outputs like this in the console:
```bash
Population Size: 100
Best Path Distance: 2345.67
Worst Path Distance: 3456.78
Median Path Distance: 2900.12
Path: 2 → 5 → 1 → 8 → 4 → 7 → 3 → 6 → 2

