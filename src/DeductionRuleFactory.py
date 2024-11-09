# Author: Noe Florence
# Description: Factory class to create instances of deduction rules.
# The DeductionRuleFactory class is a singleton that creates a chain of deduction rules to be applied to a Sudoku grid.

from DR1 import DR1
from DR2 import DR2
from DR3 import DR3
from DR4 import DR4
from DR5 import DR5


class DeductionRuleFactory:
    """
    Factory class to create instances of deduction rules.
    """
    _instance = None # Singleton instance

    def __new__(cls):
        """
        Singleton instance creation.
        Returns:
            DeductionRuleFactory: The singleton instance.
        """
        if cls._instance is None:
            cls._instance = super(DeductionRuleFactory, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def create_rules():
        """
        Create a chain of deduction rules.
        Returns:
            DeductionRule: The first rule in the chain.
        """
        # Create instances of each deduction rule
        dr1 = DR1()
        dr2 = DR2()
        dr3 = DR3()
        dr4 = DR4()
        dr5 = DR5()
        # Set the next rule in the chain
        dr1.set_next(dr2)
        dr2.set_next(dr3)
        dr3.set_next(dr4)
        dr4.set_next(dr5)
        # Return the first rule in the chain
        return dr1