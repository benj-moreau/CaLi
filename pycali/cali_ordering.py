from rdflib import Graph

from pycali.vocabulary.ontologies.cali_onto import compatibleWith
from pycali.exceptions import NotAValidLicense, BadVocabulary


class CaliOrdering(object):
    """
    A Cali Ordering.

    Implemented with Dict.
    Contains Licenses partially ordered by compatibility.
    """

    def __init__(self, deontic_lattice, vocabulary, license_constraints, compatibility_constraints):
        """
        Cali ordering Constructor.

        Init function accepts 4 arguments:
        - A deontic_lattice object that defines restrictiveness order
        - A vocabulary object that defines actions of licenses
        - LicenseConstraints object that defines if a license is valid or not
        - CompatibilityConstraints object that defines if a restrctiveness relation is also a compatibility relation

        Constructs a Dict representing the compatibility order
        between licenses.
        """
        self.compatibility = {}
        self.deontic_lattice = deontic_lattice
        self.vocabulary = vocabulary
        self.license_constraints = license_constraints
        self.compatibility_constraints = compatibility_constraints

    def add_license(self, license):
        """Add a license in the cali ordering."""
        if len(license.deontic_states) == len(self.vocabulary.actions):
            if self.license_constraints.is_valid(license):
                if license not in self.compatibility:
                    if self._is_compatible_with(license, license):
                        compatible_with = [license]
                    else:
                        compatible_with = []
                    for license2, compatible_with2 in self.compatibility.items():
                        if license2 not in compatible_with and self._is_compatible_with(license, license2):
                            compatible_with.append(license2)
                        if license not in compatible_with2 and self._is_compatible_with(license2, license):
                            compatible_with2.append(license)
                    self.compatibility[license] = compatible_with
            else:
                raise NotAValidLicense
        else:
            raise BadVocabulary

    def add_licenses(self, licenses):
        """Add a list of licenses in the cali ordering."""
        for license in licenses:
            self.add_license(license)

    def is_compatible(self, license1, license2):
        """Return True if license1 is compatible with license2."""
        if license1 not in self.compatibility:
            self.add_license(license1)
        if license1 not in self.compatibility:
            self.add_license(license2)
        return license2 in self.compatibility[license1]

    def is_compliant(self, license1, license2):
        """Return True if license1 is compliant with license2."""
        return self.is_compatible(license2, license1)

    def all_compatible(self, license):
        """Return all licenses that are compatible with license entered in parameter.

        ReturnedLicenses --- CompatibleWith ---> license
        """
        if license not in self.compatibility:
            self.add_license(license)
        compatible_licenses = []
        for license2, compatible_with in self.compatibility.items():
            if license in compatible_with:
                compatible_licenses.append(license2)
        return compatible_licenses

    def all_compliant(self, license):
        """Return all licenses that are compliant with license entered in parameter.

        license --- CompatibleWith ---> ReturnedLicenses
        """
        if license not in self.compatibility:
            self.add_license(license)
        return self.compatibility[license]

    def get_rdf_graph(self):
        """Returns an RDF graph containing license IRI's and compatibility relations."""
        rdf_graph = Graph()
        for license, compatible_licenses in self.compatibility.items():
            for compatible_license in compatible_licenses:
                rdf_graph.add((license.iri, compatibleWith, compatible_license.iri))
        return rdf_graph


    def _is_compatible_with(self, license1, license2):
        """Compute if license1 is compatible with license2."""
        if not self.compatibility_constraints.is_compatible(license1, license2):
            return False
        for state1, state2 in zip(license1.deontic_states, license2.deontic_states):
            if not self.deontic_lattice.is_less_restrictive(state1, state2):
                return False
        return True
