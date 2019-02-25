import inspect

from pycali.exceptions import NotACompatibilityConstraint, NotALicenseConstraint


class LicenseConstraints(object):
    """
    License constraints object.

    Contains a list of functions.
    Function takes a vocabulary and a license object in parameter
    and returns a Boolean.
    """

    def __init__(self, vocabulary, constraint_list=None):
        """
        License constraint Constructor.

        It accepts a vocabulary object and a list of function.
        Functions takes a license object in parameter and returns a Boolean.
        List is empty by default.
        """
        if constraint_list is None:
            constraint_list = []
        self.vocabulary = vocabulary
        self.functions = []
        for constraint in constraint_list:
            if hasattr(constraint, '__call__'):

                args = inspect.getfullargspec(constraint)[0]
                if len(args) == 2:
                    self.functions.append(constraint)
                else:
                    raise NotALicenseConstraint
            else:
                raise NotALicenseConstraint

    def is_valid(self, license):
        """Return True if license in parameter respects all constraints."""
        for constraint in self.functions:
            if not constraint(self.vocabulary, license):
                return False
        return True


class CompatibilityConstraints(object):
    """
    Compatibility constraints object.

    Contains a list of functions.
    Function takes a vocabulary and two license object in parameter
    and returns a Boolean.
    """

    def __init__(self, vocabulary, constraint_list=None):
        """
        License constraint Constructor.

        It accepts a vocabulary object and a list of function.
        Functions takes 2 licenses object in parameter and returns a Boolean.
        List is empty by default.
        """
        if constraint_list is None:
            constraint_list = []
        self.vocabulary = vocabulary
        self.functions = []
        for constraint in constraint_list:
            if hasattr(constraint, '__call__'):
                args = inspect.getfullargspec(constraint)[0]
                if len(args) == 3:
                    self.functions.append(constraint)
                else:
                    raise NotACompatibilityConstraint
            else:
                raise NotACompatibilityConstraint

    def is_compatible(self, license1, license2):
        """
        Return True if license1 and license2 in parameter respect all compatibility constraints.

        license 1 should be less restrictive that license 2
        """
        for constraint in self.functions:
            if not constraint(self.vocabulary, license1, license2):
                return False
        return True
