from unittest import TestCase
from rdflib import Graph, URIRef

from pycali.license import ODRLLicense
from pycali.vocabulary import ODRLVocabulary
from pycali.constraints import LicenseConstraints, CompatibilityConstraints
from pycali.restrictiveness_lattice_of_status import RestrictivenessLatticeOfStatus
from pycali.examples.license_constraints import CommercialUse_Not_Duty, ShareAlike_Not_Prohibition, CommercialUse_Include_Use
from pycali.examples.compatibility_constraints import ShareAlike_Compatibility, DerivativeWorks_Compatibility
from pycali.examples.restrictiveness_lattice_of_status.DL1 import dl1_rdf
from pycali.examples.licenses.ld_licenses_odrl import ld_licenses_rdf
from pycali.examples.licenses.non_valid_licenses import non_valid_licenses_rdf
import pycali.exceptions as exceptions

MIT = URIRef('http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336041529177465061342556133156838395276')
CC_BY_SA = URIRef('http://cali.priloo.univ-nantes.fr/api/ld/licenses/6592775249673133604-9092176396027616413133156838395276')
CC_BY_NC_SA = URIRef('http://cali.priloo.univ-nantes.fr/api/ld/licenses/509627953938751272-9092176396027616413-4061970458552090152')
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
        ld_licenses_graph = Graph().parse(data=ld_licenses_rdf, format='ttl')
        non_valid_graph = Graph().parse(data=non_valid_licenses_rdf, format='ttl')
        DL1 = RestrictivenessLatticeOfStatus(Graph().parse(data=dl1_rdf, format='ttl'))
        mit_license = ODRLLicense(vocabulary=ODRL, ls=DL1, rdf_graph=ld_licenses_graph, iri=MIT)
        non_valid1 = ODRLLicense(vocabulary=ODRL, ls=DL1, rdf_graph=non_valid_graph, iri=NON_VALID1)
        non_valid2 = ODRLLicense(vocabulary=ODRL, ls=DL1, rdf_graph=non_valid_graph, iri=NON_VALID2)
        non_valid3 = ODRLLicense(vocabulary=ODRL, ls=DL1, rdf_graph=non_valid_graph, iri=NON_VALID3)
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
        ld_licenses_graph = Graph().parse(data=ld_licenses_rdf, format='ttl')
        DL1 = RestrictivenessLatticeOfStatus(Graph().parse(data=dl1_rdf, format='ttl'))
        mit = ODRLLicense(vocabulary=ODRL, ls=DL1, rdf_graph=ld_licenses_graph, iri=MIT)
        cc_by_sa = ODRLLicense(vocabulary=ODRL, ls=DL1, rdf_graph=ld_licenses_graph, iri=CC_BY_SA)
        cc_by_nc_sa = ODRLLicense(vocabulary=ODRL, ls=DL1, rdf_graph=ld_licenses_graph, iri=CC_BY_NC_SA)
        with self.assertRaises(exceptions.NotACompatibilityConstraint):
            compatibility_constraints = CompatibilityConstraints(ODRL, [not_valid_constraint])
        with self.assertRaises(exceptions.NotACompatibilityConstraint):
            compatibility_constraints = CompatibilityConstraints(ODRL, [MIT])
        compatibility_constraints = CompatibilityConstraints(ODRL, [ShareAlike_Compatibility, DerivativeWorks_Compatibility])
        self.assertTrue(compatibility_constraints.is_compatible(mit, cc_by_sa))
        self.assertTrue(compatibility_constraints.is_compatible(mit, cc_by_nc_sa))
        self.assertFalse(compatibility_constraints.is_compatible(cc_by_sa, cc_by_nc_sa))
