from unittest import TestCase
from rdflib import Graph, URIRef

from pycali.license import ODRLLicense, ODRLLicenses, License
from pycali.vocabulary import ODRLVocabulary, ODRL, CC
from pycali.deontic_lattice import DeonticLattice
from pycali.ontologies.cali_onto import Permission
from pycali.examples.deontic_lattices.DL1 import dl1_rdf
from pycali.examples.deontic_lattices.DL2 import dl2_rdf
from pycali.examples.licenses.ld_licenses_odrl import ld_licenses_rdf
from pycali.examples.licenses.rep_licenses_odrl import rep_licenses_rdf
import pycali.exceptions as exceptions

MIT = URIRef('http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336041529177465061342556133156838395276')
ApacheV2 = URIRef('http://cali.priloo.univ-nantes.fr/api/rep/licenses/-31743129373347913608637588286180985472-4454034421496533318')


class testLicense(TestCase):
    """Tests for License object."""

    def test_odrl_license(self):
        """Test if ODRL licenses are well instanciated."""
        odrl = ODRLVocabulary()
        DL1 = DeonticLattice(Graph().parse(data=dl1_rdf, format='ttl'))
        DL2 = DeonticLattice(Graph().parse(data=dl2_rdf, format='ttl'))
        ld_licenses_graph = Graph().parse(data=ld_licenses_rdf, format='ttl')
        rep_licenses_graph = Graph().parse(data=rep_licenses_rdf, format='ttl')
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
        DL1 = DeonticLattice(Graph().parse(data=dl1_rdf, format='ttl'))
        ld_licenses_graph = Graph().parse(data=ld_licenses_rdf, format='ttl')
        licenses = ODRLLicenses(vocabulary=odrl, deontic_lattice=DL1, rdf_graph=ld_licenses_graph)
        self.assertEqual(len(licenses), 7)
        for license in licenses:
            self.assertIsInstance(license, License)
            self.assertIsInstance(license, ODRLLicense)

    def test_license_functions(self):
        """Test licenses methods."""
        odrl = ODRLVocabulary()
        DL1 = DeonticLattice(Graph().parse(data=dl1_rdf, format='ttl'))
        ld_licenses_graph = Graph().parse(data=ld_licenses_rdf, format='ttl')
        rep_licenses_graph = Graph().parse(data=rep_licenses_rdf, format='ttl')
        mit_license = ODRLLicense(vocabulary=odrl, deontic_lattice=DL1, rdf_graph=ld_licenses_graph, iri=MIT)
        apache_license = ODRLLicense(vocabulary=odrl, deontic_lattice=DL1, rdf_graph=rep_licenses_graph, iri=ApacheV2)
        permissions = [ODRL['modify'], CC['CommericalUse'], CC['Distribution'], CC['DerivativeWorks'], CC['Reproduction']]
        self.assertCountEqual(permissions, mit_license.get_action(vocabulary=odrl, state=Permission))
        state = apache_license.get_state(vocabulary=odrl, action=ODRL['derive'])
        self.assertEqual(state, Permission)
