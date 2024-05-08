from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            if node == goal:
                return True
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
    return False

def create_graph():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        src, dest = input("Enter source and destination node separated by space: ").split()
        if src not in graph:
            graph[src] = []
        if dest not in graph:
            graph[dest] = []
        graph[src].append(dest)
    return graph

def get_goal():
    return input("Enter the goal node: ")

def main():
    graph = create_graph()
    start = 'A'  # Assuming start node is 'A'
    goal = get_goal()
    print("Following is the Breadth First Search:")
    bfs(graph, start, goal)

if __name__ == "__main__":
    main()
