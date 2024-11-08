# Author: Noe Florence
# Description: Implementation of the Naked Singles deduction rule (DR1).

from DeductionRule import DeductionRule


class DR1(DeductionRule):
    """
    Naked Singles: If a cell has only one possible candidate, it must be that number.
    """

    def apply(self, grid):
        """
        Apply the Naked Singles rule to the Sudoku grid.
        Args:
            grid (SudokuGrid): The Sudoku grid to apply the rule to.
        Returns:
            bool: True if any changes were made to the grid, False otherwise.
        """

        changed = False
        for index in range(81):
            if grid.cells[index] == -1 and len(grid.candidates[index]) == 1:
                value = grid.candidates[index].pop()
                grid.set_value(index, value)
                changed = True
        return changed
