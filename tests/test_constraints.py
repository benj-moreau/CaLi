from unittest import TestCase
from rdflib import Graph, URIRef

from cali.license.license import ODRLLicense
from cali.vocabulary.vocabulary import ODRLVocabulary
from cali.constraints import LicenseConstraints, CompatibilityConstraints
from cali.deontic_lattice import DeonticLattice
import cali.exceptions as exceptions
from cali.examples.license_constraints import CommercialUse_Not_Duty, ShareAlike_Not_Prohibition, CommercialUse_Include_Use

MIT = URIRef('http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336041529177465061342556133156838395276')
NON_VALID1 = URIRef('http://example.org/License/1')
NON_VALID2 = URIRef('http://example.org/License/2')
NON_VALID3 = URIRef('http://example.org/License/3')


def not_valid_constraint(test):
    return test


class testLicenseConstraint(TestCase):
    """Tests for LicenseConstraint object."""

    def test_license_constraint(self):
        """Test if license constraints works as expected."""
        ODRL = ODRLVocabulary()
        ld_licenses_graph = Graph().parse(location='cali/examples/licenses/ld_licenses_odrl.ttl', format='ttl')
        non_valid_graph = Graph().parse(location='cali/examples/licenses/non_valid_licenses.ttl', format='ttl')
        DL1 = DeonticLattice('cali/examples/deontic_lattices/DL1.ttl', 'ttl')
        mit_license = ODRLLicense(vocabulary=ODRL, deontic_lattice=DL1, rdf_graph=ld_licenses_graph, iri=MIT)
        non_valid1 = ODRLLicense(vocabulary=ODRL, deontic_lattice=DL1, rdf_graph=non_valid_graph, iri=NON_VALID1)
        non_valid2 = ODRLLicense(vocabulary=ODRL, deontic_lattice=DL1, rdf_graph=non_valid_graph, iri=NON_VALID2)
        non_valid3 = ODRLLicense(vocabulary=ODRL, deontic_lattice=DL1, rdf_graph=non_valid_graph, iri=NON_VALID3)
        with self.assertRaises(exceptions.NotALicenseConstraint):
            license_constraints = LicenseConstraints(ODRL, [not_valid_constraint])
        with self.assertRaises(exceptions.NotALicenseConstraint):
            license_constraints = LicenseConstraints(ODRL, [MIT])
        license_constraints = LicenseConstraints(ODRL, [CommercialUse_Not_Duty, ShareAlike_Not_Prohibition, CommercialUse_Include_Use])
        self.assertTrue(license_constraints.is_valid(mit_license))
        self.assertFalse(license_constraints.is_valid(non_valid1))
        self.assertFalse(license_constraints.is_valid(non_valid2))
        self.assertFalse(license_constraints.is_valid(non_valid3))


class testCompatibilityConstraint(TestCase):
    """Tests for LicenseConstraint object."""

    def test_license_constraint(self):
        """Test if compatibility constraints works as expected."""
        ODRL = ODRLVocabulary()
        ld_licenses_graph = Graph().parse(location='cali/examples/licenses/ld_licenses_odrl.ttl', format='ttl')
        DL1 = DeonticLattice('cali/examples/deontic_lattices/DL1.ttl', 'ttl')
        mit_license = ODRLLicense(vocabulary=ODRL, deontic_lattice=DL1, rdf_graph=ld_licenses_graph, iri=MIT)
        with self.assertRaises(exceptions.NotACompatibilityConstraint):
            license_constraints = CompatibilityConstraints(ODRL, [not_valid_constraint])
        with self.assertRaises(exceptions.NotACompatibilityConstraint):
            license_constraints = CompatibilityConstraints(ODRL, [MIT])
        license_constraints = LicenseConstraints(ODRL, [])