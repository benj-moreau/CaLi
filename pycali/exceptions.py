class MissingAction(Exception):

    def __str__(self):
        """License does not contains all actions of the vocabulary."""
        return ("All actions of the vocabulary should be in the license or Undefined status should be in the deontic lattice")


class MissingDeonticStatus(Exception):

    def __str__(self):
        """Raise if a deontic status in the license is not in the deontic lattice."""
        return ("All deontic status of a license should be in the deontic lattice")


class BadVocabulary(Exception):

    def __str__(self):
        """Raise if the vocabulary is not the one used in the license."""
        return ("The vocabulary/action is not the one used to instanciate the license")


class MissingLicense(Exception):

    def __str__(self):
        """Raise if the license is not in the rdf graph."""
        return ("The IRI of the license is missing in the rdf graph")


class NotALicenseConstraint(ValueError):

    def __str__(self):
        """Raise if the constraint function is not a license constraint."""
        return ("Constraint is not a valid license constraint function")


class NotACompatibilityConstraint(ValueError):

    def __str__(self):
        """Raise if the constraint function is not a compatibility constraint."""
        return ("Constraint is not a valid license compatibility function")


class NotAValidLicense(ValueError):

    def __str__(self):
        """Raise if the license does not respects license constraints."""
        return ("License object does not respects License constraints.")
