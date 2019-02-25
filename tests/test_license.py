from unittest import TestCase
from rdflib import Graph, URIRef

from pycali.license import ODRLLicense, ODRLLicenses, License
from pycali.vocabulary.vocabulary import ODRLVocabulary, ODRL, CC
from pycali.deontic_lattice import DeonticLattice
from pycali.vocabulary.ontologies.cali_onto import Permission
import pycali.exceptions as exceptions

MIT = URIRef('http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336041529177465061342556133156838395276')
ApacheV2 = URIRef('http://cali.priloo.univ-nantes.fr/api/rep/licenses/-31743129373347913608637588286180985472-4454034421496533318')


class testLicense(TestCase):
    """Tests for License object."""

    def test_odrl_license(self):
        """Test if ODRL licenses are well instanciated."""
        odrl = ODRLVocabulary()
        DL1 = DeonticLattice(Graph().parse(location='pycali/examples/deontic_lattices/DL1.ttl', format='ttl'))
        DL2 = DeonticLattice(Graph().parse(location='pycali/examples/deontic_lattices/DL2.ttl', format='ttl'))
        ld_licenses_graph = Graph().parse(location='pycali/examples/licenses/ld_licenses_odrl.ttl', format='ttl')
        rep_licenses_graph = Graph().parse(location='pycali/examples/licenses/rep_licenses_odrl.ttl', format='ttl')
        with self.assertRaises(exceptions.MissingAction):
            mit_license = ODRLLicense(vocabulary=odrl, deontic_lattice=DL2, rdf_graph=ld_licenses_graph, iri=MIT)
        with self.assertRaises(exceptions.MissingLicense):
            apache_license = ODRLLicense(vocabulary=odrl, deontic_lattice=DL1, rdf_graph=ld_licenses_graph, iri=ApacheV2)
        mit_license = ODRLLicense(vocabulary=odrl, deontic_lattice=DL1, rdf_graph=ld_licenses_graph, iri=MIT)
        self.assertIsInstance(mit_license, ODRLLicense)
        self.assertTrue(mit_license.deontic_states)
        apache_license = ODRLLicense(vocabulary=odrl, deontic_lattice=DL1, rdf_graph=rep_licenses_graph, iri=ApacheV2)
        self.assertIsInstance(apache_license, ODRLLicense)
        self.assertTrue(apache_license.deontic_states)

    def test_odrl_licenses(self):
        """Test if multiple ODRL licenses are well instanciated."""
        odrl = ODRLVocabulary()
        DL1 = DeonticLattice(Graph().parse(location='pycali/examples/deontic_lattices/DL1.ttl', format='ttl'))
        ld_licenses_graph = Graph().parse(location='pycali/examples/licenses/ld_licenses_odrl.ttl', format='ttl')
        licenses = ODRLLicenses(vocabulary=odrl, deontic_lattice=DL1, rdf_graph=ld_licenses_graph)
        self.assertEqual(len(licenses), 7)
        for license in licenses:
            self.assertIsInstance(license, License)
            self.assertIsInstance(license, ODRLLicense)

    def test_license_functions(self):
        """Test licenses methods."""
        odrl = ODRLVocabulary()
        DL1 = DeonticLattice(Graph().parse(location='pycali/examples/deontic_lattices/DL1.ttl', format='ttl'))
        ld_licenses_graph = Graph().parse(location='pycali/examples/licenses/ld_licenses_odrl.ttl', format='ttl')
        rep_licenses_graph = Graph().parse(location='pycali/examples/licenses/rep_licenses_odrl.ttl', format='ttl')
        mit_license = ODRLLicense(vocabulary=odrl, deontic_lattice=DL1, rdf_graph=ld_licenses_graph, iri=MIT)
        apache_license = ODRLLicense(vocabulary=odrl, deontic_lattice=DL1, rdf_graph=rep_licenses_graph, iri=ApacheV2)
        permissions = [ODRL['modify'], CC['CommericalUse'], CC['Distribution'], CC['DerivativeWorks'], CC['Reproduction']]
        self.assertCountEqual(permissions, mit_license.get_action(vocabulary=odrl, state=Permission))
        state = apache_license.get_state(vocabulary=odrl, action=ODRL['derive'])
        self.assertEqual(state, Permission)
