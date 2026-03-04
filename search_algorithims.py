from collections import deque
import heapq
capacities = (8, 5, 3)
initial = (8, 0, 0)
goal = (4, 4, 0)
def get_neighbors(state):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if i != j and state[i] > 0 and state[j] < capacities[j]:
                transfer = min(state[i], capacities[j] - state[j])
                new_state = list(state)
                new_state[i] -= transfer
                new_state[j] += transfer
                neighbors.append(tuple(new_state))
    return neighbors
def bfs():
    queue = deque([(initial, [initial])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        visited.add(state)
        for next_state in get_neighbors(state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))
def dfs():
    stack = [(initial, [initial])]
    visited = set()
    while stack:
        state, path = stack.pop()
        if state == goal:
            return path
        if state not in visited:
            visited.add(state)
            for next_state in get_neighbors(state):
                stack.append((next_state, path + [next_state]))
def depth_limited_dfs(limit):
    stack = [(initial, [initial], 0)]
    visited = set()
    while stack:
        state, path, depth = stack.pop()
        if state == goal:
            return path
        if depth < limit:
            visited.add(state)
            for next_state in get_neighbors(state):
                stack.append((next_state, path + [next_state], depth + 1))
def iterative_deepening():
    depth = 0
    while True:
        result = depth_limited_dfs(depth)
        if result:
            return result
        depth += 1
def uniform_cost_search():
    pq = []
    heapq.heappush(pq, (0, initial, [initial]))
    visited = set()
    while pq:
        cost, state, path = heapq.heappop(pq)
        if state == goal:
            return path
        if state not in visited:
            visited.add(state)
            for next_state in get_neighbors(state):
                heapq.heappush(pq, (cost + 1, next_state, path + [next_state]))
def print_solution(name, path):
    print("\n", name)
    for step in path:
        print(step)
if __name__ == "__main__":
    print_solution("BFS Solution:", bfs())
    print_solution("DFS Solution:", dfs())
    print_solution("Depth Limited DFS:", depth_limited_dfs(10))
    print_solution("Iterative Deepening:", iterative_deepening())
    print_solution("Uniform Cost Search:", uniform_cost_search())