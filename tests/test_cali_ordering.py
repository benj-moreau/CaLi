from unittest import TestCase
from rdflib import Graph, URIRef

from pycali.cali_ordering import CaliOrdering
from pycali.deontic_lattice import DeonticLattice
from pycali.license import ODRLLicenses, ODRLLicense
from pycali.vocabulary.vocabulary import ODRLVocabulary
from pycali.constraints import LicenseConstraints, CompatibilityConstraints
from pycali.examples.license_constraints import CommercialUse_Not_Duty, ShareAlike_Not_Prohibition, CommercialUse_Include_Use
from pycali.examples.compatibility_constraints import ShareAlike_Compatibility, DerivativeWorks_Compatibility


MIT = URIRef('http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336041529177465061342556133156838395276')
CC_BY_SA = URIRef('http://cali.priloo.univ-nantes.fr/api/ld/licenses/6592775249673133604-9092176396027616413133156838395276')
CC_BY_NC_SA = URIRef('http://cali.priloo.univ-nantes.fr/api/ld/licenses/509627953938751272-9092176396027616413-4061970458552090152')


class testCaliOrdering(TestCase):
    """Tests for Cali ordering."""

    def test_cali_ordering(self):
        """Test if Cali Ordering is well instanciated."""
        CaliOrdering(deontic_lattice=DeonticLattice(Graph().parse(location='cali/examples/deontic_lattices/DL1.ttl', format='ttl')),
                     vocabulary=ODRLVocabulary(),
                     license_constraints=LicenseConstraints([CommercialUse_Not_Duty, ShareAlike_Not_Prohibition, CommercialUse_Include_Use]),
                     compatibility_constraints=CompatibilityConstraints([ShareAlike_Compatibility, DerivativeWorks_Compatibility]))

    def test_order(self):
        odrl = ODRLVocabulary()
        DL1 = DeonticLattice(Graph().parse(location='cali/examples/deontic_lattices/DL1.ttl', format='ttl'))
        ld_licenses_graph = Graph().parse(location='cali/examples/licenses/ld_licenses_odrl.ttl', format='ttl')
        cali_ordering = CaliOrdering(deontic_lattice=DL1,
                                     vocabulary=odrl,
                                     license_constraints=LicenseConstraints(odrl, [CommercialUse_Not_Duty, ShareAlike_Not_Prohibition, CommercialUse_Include_Use]),
                                     compatibility_constraints=CompatibilityConstraints(odrl, [ShareAlike_Compatibility, DerivativeWorks_Compatibility]))
        licenses = ODRLLicenses(vocabulary=odrl, deontic_lattice=DL1, rdf_graph=ld_licenses_graph)
        cali_ordering.add_license(licenses[0])
        cali_ordering.add_licenses(licenses)
        mit_license = ODRLLicense(vocabulary=odrl, deontic_lattice=DL1, rdf_graph=ld_licenses_graph, iri=MIT)
        cc_by_sa_license = ODRLLicense(vocabulary=odrl, deontic_lattice=DL1, rdf_graph=ld_licenses_graph, iri=CC_BY_SA)
        cc_by_nc_sa_license = ODRLLicense(vocabulary=odrl, deontic_lattice=DL1, rdf_graph=ld_licenses_graph, iri=CC_BY_NC_SA)
        self.assertTrue(cali_ordering.is_compatible(mit_license, cc_by_sa_license))
        self.assertFalse(cali_ordering.is_compatible(cc_by_sa_license, mit_license))
        self.assertTrue(cali_ordering.is_compliant(cc_by_sa_license, mit_license))
        self.assertFalse(cali_ordering.is_compliant(mit_license, cc_by_sa_license))
        self.assertFalse(cali_ordering.is_compatible(cc_by_sa_license, cc_by_nc_sa_license))
        self.assertEqual(len(cali_ordering.all_compatible(mit_license)), 2)
        self.assertEqual(len(cali_ordering.all_compliant(mit_license)), 6)
        self.assertEqual(len(cali_ordering.get_rdf_graph()), 21)