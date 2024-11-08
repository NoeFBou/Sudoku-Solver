# Author: Noe Florence
# Description: Base class for deduction rules used in solving Sudoku puzzles.

class DeductionRule:
    """
    Abstract base class for Sudoku deduction rules.
    """

    def apply(self, grid):
        """
        Apply the deduction rule to the grid.
        Args:
            grid (SudokuGrid): The Sudoku grid to apply the rule to.
        Returns:
            bool: True if any changes were made to the grid, False otherwise.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")
