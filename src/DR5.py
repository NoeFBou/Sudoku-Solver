# Author: Noe Florence
# Description: Implementation of the Pointing Pairs/Triples deduction rule (DR5).

from DeductionRule import DeductionRule


class DR5(DeductionRule):
    """
    Pointing Pairs/Triples: If in a block, all candidates of a number are confined to a single row or column,
    then this candidate can be eliminated from other cells in that row or column outside the block.
    """

    def apply(self, grid):
        """
        Apply the Pointing Pairs/Triples rule to the Sudoku grid.
        Args:
            grid (SudokuGrid): The Sudoku grid to apply the rule to.
        Returns:
            bool: True if any changes were made to the grid, False otherwise.
        """

        changed = False
        # Process each block (blocks are units[18:27])
        for block in grid.units[18:27]:
            candidate_cells = {}
            # Map candidates to their cells within the block
            for candidate in range(1, 10):
                candidate_cells[candidate] = [index for index in block if candidate in grid.candidates[index]]
            # Check if candidates are confined to a single row or column
            for candidate in range(1, 10):
                cells = candidate_cells[candidate]
                if not cells:
                    continue
                rows = set(index // 9 for index in cells)
                cols = set(index % 9 for index in cells)
                if len(rows) == 1:
                    # Candidate is confined to a single row within the block
                    row = rows.pop()
                    for index in range(row * 9, (row + 1) * 9):
                        if index not in block and candidate in grid.candidates[index]:
                            # Eliminate candidate from other cells in the row outside the block
                            grid.candidates[index].remove(candidate)
                            changed = True
                elif len(cols) == 1:
                    # Candidate is confined to a single column within the block
                    col = cols.pop()
                    for index in range(col, 81, 9):
                        if index not in block and candidate in grid.candidates[index]:
                            # Eliminate candidate from other cells in the column outside the block
                            grid.candidates[index].remove(candidate)
                            changed = True
        return changed
