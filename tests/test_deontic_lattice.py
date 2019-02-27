from unittest import TestCase
from rdflib import Graph

from pycali.deontic_lattice import DeonticLattice
from pycali.ontologies.cali_onto import Undefined, Permission, Prohibition, Duty
from pycali.examples.deontic_lattices.DL1 import dl1_rdf
from pycali.examples.deontic_lattices.DL2 import dl2_rdf


class testDeonticLattice(TestCase):
    """Test for DeonticLattice object."""

    def test_odrl_vocabulary(self):
        """Test if ODRL vocabulary is well instanciated."""
        DL1 = DeonticLattice(Graph().parse(data=dl1_rdf, format='ttl'))
        DL2 = DeonticLattice(Graph().parse(data=dl2_rdf, format='ttl'))
        self.assertCountEqual([Undefined, Permission, Prohibition, Duty], DL1.restrictiveness[Undefined])
        self.assertCountEqual([Permission, Prohibition, Duty], DL1.restrictiveness[Permission])
        self.assertCountEqual([Prohibition, Duty], DL1.restrictiveness[Prohibition])
        self.assertCountEqual([Duty], DL1.restrictiveness[Duty])
        self.assertCountEqual([Permission, Prohibition, Duty], DL2.restrictiveness[Permission])
        self.assertCountEqual([Prohibition, Duty], DL2.restrictiveness[Prohibition])
        self.assertCountEqual([Duty], DL2.restrictiveness[Duty])

    def test_restrictiveness(self):
        """Test restrictiveness function of the deontic lattice."""
        DL1 = DeonticLattice(Graph().parse(data=dl1_rdf, format='ttl'))
        self.assertTrue(DL1.is_less_restrictive(Undefined, Permission))
        self.assertTrue(DL1.is_less_restrictive(Undefined, Duty))
        self.assertTrue(DL1.is_less_restrictive(Permission, Duty))
        self.assertTrue(DL1.is_less_restrictive(Duty, Duty))
        self.assertFalse(DL1.is_less_restrictive(Duty, Undefined))
        self.assertFalse(DL1.is_less_restrictive(Prohibition, Permission))
        self.assertFalse(DL1.is_less_restrictive(Permission, Undefined))
