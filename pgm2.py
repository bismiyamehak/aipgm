import heapq

def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3: return False
    if 0 < m < c or 0 < (3-m) < (3-c): return False 
    return True

def get_successors(state):
    m, c, b = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)] 
    results = []
    for dm, dc in moves:
        nm, nc = (m-dm, c-dc) if b == 1 else (m+dm, c+dc)
        if is_valid(nm, nc): results.append((nm, nc, 1-b))
    return results

def heuristic(state):
    return state[0] + state[1]

def best_first_search():
    start, goal = (3, 3, 1), (0, 0, 0)
    pq = [(heuristic(start), start, [start])]
    visited = {start}

    while pq:
        _, current, path = heapq.heappop(pq)
        if current == goal: return path
        for succ in get_successors(current):
            if succ not in visited:
                visited.add(succ)
                heapq.heappush(pq, (heuristic(succ), succ, path + [succ]))
    return None

path = best_first_search()+
print("Solution Path (M, C, Boat):")
for step in path: print(step)