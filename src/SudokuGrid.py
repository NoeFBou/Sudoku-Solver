# Author: Noe Florence
# Description: SudokuGrid class representing the state of a Sudoku grid, extending Observable.

from Observable import Observable


class SudokuGrid(Observable):
    """
    Represents a Sudoku grid and manages cell values, candidates, units, and peers.
    """

    def __init__(self, initial_values):
        """
        Initialize the Sudoku grid with initial cell values.
        Args:
            initial_values (list): A list of 81 integers representing the initial cell values.
                                   Use -1 for empty cells.
        """
        super().__init__()
        # Copy the initial cell values
        self.cells = initial_values[:]  # List of 81 elements
        # Initialize candidates: for empty cells (-1), candidates are numbers 1-9; otherwise, empty set
        self.candidates = [set(range(1, 10)) if val == -1 else set() for val in self.cells]
        # Generate units (rows, columns, blocks) and peers for each cell
        self.units = self._generate_units()
        self.peers = self._generate_peers()
        # Update candidates based on initial values
        self._initialize_candidates()

    @staticmethod
    def _generate_units():
        """
        Generate the units (rows, columns, and blocks) for the Sudoku grid.
        Returns:
            list: A list containing all units of the grid.
        """
        units = []
        # Generate rows
        rows = [range(i * 9, (i + 1) * 9) for i in range(9)]
        # Generate columns
        cols = [range(i, 81, 9) for i in range(9)]
        # Generate blocks
        blocks = []
        for i in (0, 3, 6):
            for j in (0, 27, 54):
                # Each block contains 9 cells
                block = [i + j + k for k in [0, 1, 2, 9, 10, 11, 18, 19, 20]]
                blocks.append(block)
        # Combine all units
        units.extend(rows + cols + blocks)
        return units

    @staticmethod
    def _generate_peers():
        """
        Generate the peers for each cell in the Sudoku grid.
        Returns:
            list: A list of sets, where each set contains the indices of the peers for a cell.
        """
        peers = [set() for _ in range(81)]
        for index in range(81):
            row = index // 9
            col = index % 9
            # Calculate block starting positions
            block_row = (row // 3) * 3
            block_col = (col // 3) * 3
            # Indices of cells in the same block
            block_indices = [
                (block_row + r) * 9 + block_col + c
                for r in range(3) for c in range(3)
            ]
            # Combine indices of cells in the same row, column, and block
            peer_indices = set(
                [row * 9 + c for c in range(9)] +    # Same row
                [r * 9 + col for r in range(9)] +    # Same column
                block_indices                         # Same block
            )
            peer_indices.remove(index)  # Remove the cell itself
            peers[index] = peer_indices
        return peers

    def _initialize_candidates(self):
        """
        Initialize candidates for each cell based on initial values.
        """
        for index, value in enumerate(self.cells):
            if value != -1:
                # Update candidates for peers when a cell has an initial value
                self.update_candidates(index, value)

    def set_value(self, index, value):
        """
        Set a value for a cell and update candidates.
        Args:
            index (int): The index of the cell (0-80).
            value (int): The value to set (1-9).
        """
        self.cells[index] = value
        self.candidates[index] = set()
        # Update candidates for peers
        self.update_candidates(index, value)
        # Notify observers about the change
        self.notify_observers(('set_value', index, value))

    def update_candidates(self, index, value):
        """
        Update candidates for peers of a cell when a value is assigned.
        Args:
            index (int): The index of the cell that was assigned a value.
            value (int): The value that was assigned to the cell.
        """
        for peer in self.peers[index]:
            if value in self.candidates[peer]:
                self.candidates[peer].discard(value)
                # If a peer has no candidates left and is empty, the grid is inconsistent
                if not self.candidates[peer] and self.cells[peer] == -1:
                    raise ValueError("Inconsistency detected in the grid.")

    def is_solved(self):
        """
        Check if the Sudoku grid is completely solved.
        Returns:
            bool: True if all cells are filled, False otherwise.
        """
        return all(value != -1 for value in self.cells)

    def print_grid(self):
        """
        Print the current state of the Sudoku grid in a readable format.
        """
        print('+-------+-------+-------+')
        for i in range(9):
            row = ''
            for j in range(9):
                val = self.cells[i * 9 + j]
                if j % 3 == 0:
                    row += '| '
                # Use '.' for empty cells
                row += str(val) if val != -1 else '.'
                row += ' '
            row += '|'
            print(row)
            if i % 3 == 2:
                print('+-------+-------+-------+')
