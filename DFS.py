def dfs(visited, graph, node, goal):  # Pass 'goal' as an argument
    if node not in visited:
        print(node)
        visited.add(node)
        if node == goal:
            return True
        for neighbour in graph[node]:
            if dfs(visited, graph, neighbour, goal):  # Pass 'goal' recursively
                return True
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
    goal = get_goal()
    visited = set()
    print("Following is the Depth First Search:")
    dfs(visited, graph, 'A', goal)  # Pass 'goal' here

if __name__ == "__main__":
    main()
