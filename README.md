# Sudoku-Solver

A Python-based Sudoku solver that applies various deduction rules to efficiently solve Sudoku puzzles.

## Features
  - Implements multiple deduction rules (DR1 to DR5) to solve Sudoku puzzles.
  - Evaluates the difficulty level of the Sudoku puzzle.
  - Allows user intervention when automatic solving is not possible.
  - Provides a clear and formatted output of the solved Sudoku grid.

## Installation
Clone the repository

1. Copier le code
  ``git clone https://github.com/yourusername/sudoku-solver.git``

2. Navigate to the project directory
  `` cd sudoku-solver ``

3. Ensure you have Python 3 installed
  The solver requires Python 3.x to run. You can check your Python version with:
  ``
  python --version
  ``

## Usage
1. Prepare your Sudoku input file

  - Create a text file containing the Sudoku puzzle.
  - Use -1 or 0 to represent empty cells.
  - Each line should contain 9 numbers separated by commas.

  ### Example (grid.txt):
  `
  5,3,-1,-1,7,-1,-1,-1,-1
  6,-1,-1,1,9,5,-1,-1,-1
  -1,9,8,-1,-1,-1,-1,6,-1
  8,-1,-1,-1,6,-1,-1,-1,3
  4,-1,-1,8,-1,3,-1,-1,1
  7,-1,-1,-1,2,-1,-1,-1,6
  -1,6,-1,-1,-1,-1,2,8,-1
  -1,-1,-1,4,1,9,-1,-1,5
  -1,-1,-1,-1,8,-1,-1,7,9
  `
2. Run the solver
  ``python sudoku_solver.py grid.txt``

3. Interpreting the output
  - If the puzzle is solved successfully, the solved grid will be displayed along with the difficulty level.
  - If user intervention is required, you will be prompted to input a cell index and value.

## Example
  ``python sudoku_solver.py examples/puzzle1.txt``

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License.
