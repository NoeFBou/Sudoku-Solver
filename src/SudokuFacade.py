# Author: Noe Florence
# Description: Facade class for solving Sudoku puzzles.

from SudokuGrid import SudokuGrid
from SudokuSolver import SudokuSolver


class SudokuFacade:
    """
    Facade class for solving Sudoku puzzles.
    """

    def __init__(self, initial_values):
        """
        Initialize the SudokuFacade with initial cell values.
        Args:
            initial_values (list): A list of 81 integers representing the initial cell values.
                                   Use -1 for empty cells
        """
        self.grid = SudokuGrid(initial_values)
        self.solver = SudokuSolver(self.grid)

    def solve(self):
        """
        Solve the Sudoku puzzle and print the solution.
        """
        if self.solver.solve():
            print("Sudoku solved successfully!")
            self.grid.print_grid()
            difficulty = self.solver.evaluate_difficulty()
            print(f"Difficulty Level: {difficulty}")
            if self.solver.user_intervened:
                print("The grid was completed after you manually entered a number.")
        else:
            print("Could not solve the Sudoku.")
            print("Difficulty Level: Very High")