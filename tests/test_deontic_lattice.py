from unittest import TestCase
from rdflib import Graph

from pycali.restrictiveness_lattice_of_status import RestrictivenessLatticeOfStatus
from pycali.ontologies.cali_onto import Undefined, Permission, Prohibition, Duty
from pycali.examples.restrictiveness_lattice_of_status.DL1 import dl1_rdf
from pycali.examples.restrictiveness_lattice_of_status.DL2 import dl2_rdf


class testRestrictivenessLatticeOfStatus(TestCase):
    """Test for RestrictivenessLatticeOfStatus object."""

    def test_ls(self):
        """Test if Restrictiveness lattice of status is well instanciated."""
        DL1 = RestrictivenessLatticeOfStatus(Graph().parse(data=dl1_rdf, format='ttl'))
        DL2 = RestrictivenessLatticeOfStatus(Graph().parse(data=dl2_rdf, format='ttl'))
        self.assertCountEqual([Undefined, Permission, Prohibition, Duty], DL1.restrictiveness[Undefined])
        self.assertCountEqual([Permission, Prohibition, Duty], DL1.restrictiveness[Permission])
        self.assertCountEqual([Prohibition, Duty], DL1.restrictiveness[Prohibition])
        self.assertCountEqual([Duty], DL1.restrictiveness[Duty])
        self.assertCountEqual([Permission, Prohibition, Duty], DL2.restrictiveness[Permission])
        self.assertCountEqual([Prohibition, Duty], DL2.restrictiveness[Prohibition])
        self.assertCountEqual([Duty], DL2.restrictiveness[Duty])

    def test_restrictiveness(self):
        """Test restrictiveness function of the restrictiveness lattice of status."""
        DL1 = RestrictivenessLatticeOfStatus(Graph().parse(data=dl1_rdf, format='ttl'))
        self.assertTrue(DL1.is_less_restrictive(Undefined, Permission))
        self.assertTrue(DL1.is_less_restrictive(Undefined, Duty))
        self.assertTrue(DL1.is_less_restrictive(Permission, Duty))
        self.assertTrue(DL1.is_less_restrictive(Duty, Duty))
        self.assertFalse(DL1.is_less_restrictive(Duty, Undefined))
        self.assertFalse(DL1.is_less_restrictive(Prohibition, Permission))
        self.assertFalse(DL1.is_less_restrictive(Permission, Undefined))
