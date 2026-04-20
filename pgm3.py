import heapq
def a_star_algorithm(graph, heuristics, start, goal):
    priority_queue = [(heuristics[start], start, 0, [])]
    visited = set()

    while priority_queue:
        f, current_node, g, path = heapq.heappop(priority_queue)
        if current_node in visited:
            continue
        path = path + [current_node]
        if current_node == goal:
            return path, g
        visited.add(current_node)
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                new_g = g + weight
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(priority_queue, (new_f, neighbor, new_g, path))

    return None, float('inf')
graph = {
    'A': {'B': 2, 'E': 3},
    'B': {'A': 2, 'C': 1, 'G': 9},
    'C': {'B': 1},
    'E': {'A': 3, 'D': 6},
    'D': {'E': 6, 'G': 1},
    'G': {'B': 9, 'D': 1}
}
heuristics = {
    'A': 11,
    'B': 6,
    'C': 99,
    'E': 7,
    'D': 1,
    'G': 0
}
path, total_cost = a_star_algorithm(graph, heuristics, 'A', 'G')

print(f"Optimal Path: {' -> '.join(path)}")
print(f"Total Path Cost: {total_cost}")