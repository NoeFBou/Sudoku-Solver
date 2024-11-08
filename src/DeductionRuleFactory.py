# Author: Noe Florence
# Description: Factory class for creating deduction rule instances.

from DR1 import DR1
from DR2 import DR2
from DR3 import DR3
from DR4 import DR4
from DR5 import DR5


class DeductionRuleFactory:
    """
    Factory class to create instances of deduction rules.
    """

    @staticmethod
    def create_rules():
        """
        Create a list of deduction rule instances.
        Returns:
            list: A list of instantiated deduction rules.
        """

        return [DR1(), DR2(), DR3(), DR4(), DR5()]
