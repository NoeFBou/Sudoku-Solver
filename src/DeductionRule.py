# Author: Noe Florence
# Description: Base class for deduction rules used in solving Sudoku puzzles.

class DeductionRule:
    """
    Abstract base class for Sudoku deduction rules.
    """
    def __init__(self):
        self.next_rule = None

    def set_next(self, rule):
        """
        Set the next deduction rule in the chain.
        Args:
            rule (DeductionRule): The next deduction rule.
        """
        self.next_rule = rule

    def apply(self, grid):
        """
        Apply the deduction rule to the grid.
        Args:
            grid (SudokuGrid): The Sudoku grid to apply the rule to.
        Returns:
            bool: True if any changes were made to the grid, False otherwise.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")

    def handle(self, grid):
        """
        Apply the deduction rule to the grid, or pass it to the next rule if no changes are made.
        Args:
            grid (SudokuGrid): The Sudoku grid to apply the rule to.
        Returns:
            str: The name of the rule that was applied, or None if no changes were made.
        """
        if self.apply(grid):
            return self.__class__.__name__
        elif self.next_rule:
            return self.next_rule.handle(grid)
        else:
            return None