# Author: Noe Florence
# Description: Main script to run the Sudoku solver.

import sys
from SudokuGrid import SudokuGrid
from SudokuSolver import SudokuSolver


def parse_input(file_path):
    """
    Parse the input file to extract the Sudoku grid values.
    Args:
        file_path (str): Path to the input file.
    Returns:
        list: A list of 81 integers representing the Sudoku grid.
    Raises:
        ValueError: If the input file does not contain valid Sudoku grid data.
    """

    with open(file_path, 'r') as file:
        lines = file.readlines()
    grid_values = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        numbers = []
        for num in line.split(','):
            num = num.strip()
            if num in ('0', '-1'):
                numbers.append(-1)
            else:
                numbers.append(int(num))
        if len(numbers) != 9:
            raise ValueError("Each line must contain 9 numbers.")
        grid_values.extend(numbers)
    if len(grid_values) != 81:
        raise ValueError("The grid must contain 81 numbers.")
    return grid_values


def main():
    """
    Main function to run the Sudoku solver.
    """

    if len(sys.argv) != 2:
        print("Usage: python sudoku_solver.py <input_file>")
        return
    file_path = sys.argv[1]
    try:
        initial_values = parse_input(file_path)
        grid = SudokuGrid(initial_values)
        solver = SudokuSolver(grid)
        if solver.solve():
            print("Sudoku solved successfully!")
            grid.print_grid()
            difficulty = solver.evaluate_difficulty()
            print(f"Difficulty Level: {difficulty}")
            if solver.user_intervened:
                print("The grid was completed after you manually entered a number.")
        else:
            print("Could not solve the Sudoku.")
            print("Difficulty Level: Very High")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
