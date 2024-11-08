# Author: Noe Florence
# Description: Implementation of the Hidden Pairs deduction rule (DR4).

from DeductionRule import DeductionRule


class DR4(DeductionRule):
    """
    Hidden Pairs: In a unit (row, column, or block), if two candidates appear only in exactly two cells,
    then other candidates in these cells can be eliminated.
    """

    def apply(self, grid):
        """
        Apply the Hidden Pairs rule to the Sudoku grid.
        Args:
            grid (SudokuGrid): The Sudoku grid to apply the rule to.
        Returns:
            bool: True if any changes were made to the grid, False otherwise.
        """

        changed = False
        for unit in grid.units:
            # Build a mapping from candidates to the cells they appear in
            candidate_cells = {}
            for candidate in range(1, 10):
                candidate_cells[candidate] = [index for index in unit if candidate in grid.candidates[index]]
            # For each pair of candidates
            for candidate1 in range(1, 9):
                for candidate2 in range(candidate1 + 1, 10):
                    cells_c1 = set(candidate_cells[candidate1])
                    cells_c2 = set(candidate_cells[candidate2])
                    # Find common cells where both candidates appear
                    common_cells = cells_c1 & cells_c2
                    if len(common_cells) == 2:
                        # Check that these candidates appear only in these two cells within the unit
                        total_cells = cells_c1 | cells_c2
                        if len(total_cells) == 2:
                            # Hidden pair found, eliminate other candidates from these cells
                            for index in common_cells:
                                before = grid.candidates[index].copy()
                                grid.candidates[index].intersection_update({candidate1, candidate2})
                                if grid.candidates[index] != before:
                                    changed = True
        return changed
