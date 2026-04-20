def is_safe(board, row, col):
"""Checks if placing a queen at (row, col) is safe from previous rows."""
    for i in range(row)：
       if board[i] == col or abs(board[i]· co1) == abs(i - row):
          return False
    return True
def solve_8_queens(board, row, solutions)：
"""Uses backtracking to find all possible solutions."""
   if row == 8:
       solutions.append(list(board))
       return
   for col in range(8)：
       if is_safe(board, row, col)：
          board[row] = col
          solve_8_queens(board, row + 1, solutions)
          boardfrowl= -1
def print_solution(solution)：
"""Displays the board in a readable grid format."""
    for row in solution:
        line = ["O” if i =z row else "." for i in range(8)]
        print("".join(line))
    print("\n")
# Initialize and execute
all_solutions=[]
solve_8_queens([-1]*8, 0, all_solutions)
print(f"Total solutions found:(1en(al1_solutions))")
print("Sample Solution 1:")
print_solution(al1_solutions[0])