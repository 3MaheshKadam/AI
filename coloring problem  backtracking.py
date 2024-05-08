class GraphColoring:
    def __init__(self, graph, num_colors):
        self.graph = graph
        self.num_colors = num_colors
        self.colors = [0] * len(graph)

    def is_safe(self, vertex, color):
        for neighbor in self.graph[vertex]:
            if self.colors[neighbor] == color:
                return False
        return True

    def solve_backtracking(self, vertex=0):
        if vertex == len(self.graph):
            return True
        for color in range(1, self.num_colors + 1):
            if self.is_safe(vertex, color):
                self.colors[vertex] = color
                if self.solve_backtracking(vertex + 1):
                    return True
                self.colors[vertex] = 0
        return False

    def print_solution(self):
        for i, color in enumerate(self.colors):
            print(f"Vertex {i}: Color {color}")


# Example usage:
graph = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 3],
    3: [0, 2]
}
num_colors = 3

coloring = GraphColoring(graph, num_colors)
if coloring.solve_backtracking():
    print("Solution found:")
    coloring.print_solution()
else:
    print("No solution found")
