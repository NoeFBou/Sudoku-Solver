# Author: Noe Florence
# Description: Implementation of the Hidden Singles deduction rule (DR2).

from DeductionRule import DeductionRule


class DR2(DeductionRule):
    """
    Hidden Singles: If a candidate appears only once in a unit, it must be in that cell.
    """

    def apply(self, grid):
        """
        Apply the Hidden Singles rule to the Sudoku grid.
        Args:
            grid (SudokuGrid): The Sudoku grid to apply the rule to.
        Returns:
            bool: True if any changes were made to the grid, False otherwise.
        """

        changed = False
        for unit in grid.units:
            counts = {}  # Dictionary to count occurrences of each candidate in the unit
            for index in unit:
                for candidate in grid.candidates[index]:
                    # Map each candidate to the list of cell indices where it appears
                    counts.setdefault(candidate, []).append(index)
            for candidate, indices in counts.items():
                # If a candidate appears only once in the unit
                if len(indices) == 1 and grid.cells[indices[0]] == -1:
                    # Assign that candidate to the cell
                    grid.set_value(indices[0], candidate)
                    changed = True
        return changed
