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

  Example (grid.txt):
  
    0,0,9,0,0,0,0,0,2
    0,0,0,0,0,0,7,0,8
    0,4,3,0,0,0,0,0,0
    2,0,0,0,7,0,0,0,1
    0,3,0,9,0,0,8,0,0
    1,5,4,0,0,2,3,0,9
    0,0,0,0,3,0,2,0,0
    4,0,5,0,0,1,0,0,0
    0,0,1,0,0,8,4,0,5
  
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
