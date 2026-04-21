import sys

def tsp_nearest_neighbor(graph, start=0):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    path = [start]
    visited[start] = True
    
    while len(path) < num_nodes:
        current_city = path[-1]
        nearest_city = None
        min_distance = sys.maxsize
        
        # Find the nearest unvisited city
        for city in range(num_nodes):
            if not visited[city] and graph[current_city][city] < min_distance:
                nearest_city = city
                min_distance = graph[current_city][city]
        
        visited[nearest_city] = True
        path.append(nearest_city)
        
    path.append(start)  # Return to start city
    return path

# Example Distance Matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path = tsp_nearest_neighbor(graph)
print(f"Heuristic Path: {path}")