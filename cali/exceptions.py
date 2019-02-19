class MissingAction(Exception):

    def __str__(self):
        """License does not contains all actions of the vocabulary."""
        return ("All actions of the vocabulary should be in the license or Undefined status should be in the deontic lattice")


class MissingDeonticStatus(Exception):

    def __str__(self):
        """Raise if a deontic status in the license is not in the deontic lattice"""
        return ("All deontic status of a license should be in the deontic lattice")
