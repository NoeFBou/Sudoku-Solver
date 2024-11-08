# Author: Noe Florence
# Description: Implementation of the Naked Pairs deduction rule (DR3).

from DeductionRule import DeductionRule


class DR3(DeductionRule):
    """
    Naked Pairs: If two cells in a unit have the same two candidates, those candidates can be
    eliminated from other cells in the unit.
    """

    def apply(self, grid):
        """
        Apply the Naked Pairs rule to the Sudoku grid.
        Args:
            grid (SudokuGrid): The Sudoku grid to apply the rule to.
        Returns:
            bool: True if any changes were made to the grid, False otherwise.
        """

        changed = False
        for unit in grid.units:
            pairs = {}  # Dictionary to store pairs of candidates and their cell indices
            for index in unit:
                if len(grid.candidates[index]) == 2:
                    # Create a key based on the sorted tuple of candidates
                    key = tuple(sorted(grid.candidates[index]))
                    pairs.setdefault(key, []).append(index)
            for key, indices in pairs.items():
                # If the same pair of candidates appears in exactly two cells
                if len(indices) == 2:
                    for index in unit:
                        if index not in indices and grid.cells[index] == -1:
                            # Remove these candidates from other cells in the unit
                            before = len(grid.candidates[index])
                            grid.candidates[index] -= set(key)
                            if len(grid.candidates[index]) != before:
                                changed = True
        return changed
