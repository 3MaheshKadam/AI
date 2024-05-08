class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n

    def is_safe(self, row, col):
        for prev_row in range(row):
            prev_col = self.board[prev_row]
            if prev_col == col or prev_col - prev_row == col - row or prev_col + prev_row == col + row:
                return False
        return True

    def solve_backtracking(self, row=0):
        if row == self.n:
            return True
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                if self.solve_backtracking(row + 1):
                    return True
                self.board[row] = -1
        return False

    def solve_branch_and_bound(self, row=0, col_min=0):
        if row == self.n:
            return True
        for col in range(col_min, self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                if self.solve_branch_and_bound(row + 1, col + 1):
                    return True
                self.board[row] = -1
        return False

    def print_solution(self):
        for row in range(self.n):
            line = ['Q' if col == self.board[row] else '.' for col in range(self.n)]
            print(' '.join(line))


# Example usage:
n = 8
queens = NQueens(n)

print("Backtracking Solution:")
if queens.solve_backtracking():
    queens.print_solution()
else:
    print("No solution found")

print("\nBranch and Bound Solution:")
if queens.solve_branch_and_bound():
    queens.print_solution()
else:
    print("No solution found")
