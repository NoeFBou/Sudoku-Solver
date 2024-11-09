# Author: Noe Florence
# Description: SudokuSolver class that applies deduction rules to solve a Sudoku puzzle.

from DeductionRuleFactory import DeductionRuleFactory


class SudokuSolver:
    """
    Solver for Sudoku puzzles using deduction rules.
    """

    def __init__(self, grid):
        """
        Initialize the SudokuSolver with a grid.
        Args:
            grid (SudokuGrid): The Sudoku grid to solve.
        """
        self._updating = None
        self.grid = grid
        factory = DeductionRuleFactory()
        self.rule_chain = factory.create_rules()
        self.used_rules = set()
        self.user_intervened = False
        grid.add_observer(self)

    def update(self, observable, event=None):
        """
        Observer update method, called when the grid changes.
        Args:
            observable (Observable): The observable object.
            event: Optional event data.
        """
        if hasattr(self, '_updating') and self._updating:
            return
        self._updating = True
        try:
            self.apply_rules()
        finally:
            self._updating = False

    def apply_rules(self):
        """
        Apply deduction rules to the grid iteratively until no progress can be made.
        """
        while True:
            # Check for inconsistencies in the grid
            for index in range(81):
                if self.grid.cells[index] != -1:
                    continue
                if not self.grid.candidates[index]:
                    raise ValueError("Inconsistency detected in the grid.")
            rule_name = self.rule_chain.handle(self.grid)
            if rule_name:
                self.used_rules.add(rule_name)
            else:
                if self.grid.is_solved():
                    return True
                else:
                    # Prompt user input if the grid is not solvable by rules alone
                    self.user_input()
                    break

    def solve(self):
        """
        Attempt to solve the Sudoku puzzle.
        Returns:
            bool: True if solved successfully, False otherwise.
        """
        try:
            self.apply_rules()
            return self.grid.is_solved()
        except ValueError:
            print("Please restart the solving.")
            return False

    def user_input(self):
        """
        Prompt the user to manually input a value when automatic solving is not possible.
        """
        self.user_intervened = True  # User intervention occurred
        self.grid.print_grid()
        while True:
            try:
                index = int(input("Enter cell index (0-80): "))
                if not (0 <= index < 81):
                    raise ValueError()
                if self.grid.cells[index] != -1:
                    print("Cell is already filled.")
                    continue
                value = int(input("Enter value (1-9): "))
                if not (1 <= value <= 9):
                    raise ValueError()
                self.grid.set_value(index, value)
                break
            except ValueError:
                print("Invalid input. Please try again.")

    def evaluate_difficulty(self):
        """
        Evaluate the difficulty level of the Sudoku puzzle based on the rules used.
        Returns:
            str: A string representing the difficulty level.
        """
        if not self.grid.is_solved():
            return "Very Hard"
        print(f"Used rules: {self.used_rules}")
        if 'DR1' in self.used_rules and len(self.used_rules) == 1:
            return "Simple"
        elif 'DR4' in self.used_rules or 'DR5' in self.used_rules:
            return "Hard"
        elif 'DR3' in self.used_rules:
            return "Intermediate"
        elif 'DR2' in self.used_rules:
            return "Easy"
        else:
            return "Not possible to evaluate with current rules"
