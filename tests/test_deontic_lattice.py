from unittest import TestCase

from cali.deontic_lattice import DeonticLattice

from cali.vocabulary.ontologies.cali_onto import Undefined, Permission, Prohibition, Duty


class testDeonticLattice(TestCase):
    """Test if DeonticLattice object is well instanciated and ."""

    def test_odrl_vocabulary(self):
        """Test if ODRL vocabulary is well instanciated."""
        DL1 = DeonticLattice('cali/examples/deontic_lattices/DL1.ttl', 'ttl')
        DL2 = DeonticLattice('cali/examples/deontic_lattices/DL2.ttl', 'ttl')
        self.assertItemsEqual([Undefined, Permission, Prohibition, Duty], DL1.moreRestrictiveThan[Undefined])
        self.assertItemsEqual([Permission, Prohibition, Duty], DL1.moreRestrictiveThan[Permission])
        self.assertItemsEqual([Prohibition, Duty], DL1.moreRestrictiveThan[Prohibition])
        self.assertItemsEqual([Duty], DL1.moreRestrictiveThan[Duty])
        self.assertItemsEqual([Permission, Prohibition, Duty], DL2.moreRestrictiveThan[Permission])
        self.assertItemsEqual([Prohibition, Duty], DL2.moreRestrictiveThan[Prohibition])
        self.assertItemsEqual([Duty], DL2.moreRestrictiveThan[Duty])

    def test_restrictiveness(self):
        DL1 = DeonticLattice('cali/examples/deontic_lattices/DL1.ttl', 'ttl')
        self.assertTrue(DL1.is_less_restrictive(Undefined, Permission))
        self.assertTrue(DL1.is_less_restrictive(Undefined, Duty))
        self.assertTrue(DL1.is_less_restrictive(Permission, Duty))
        self.assertTrue(DL1.is_less_restrictive(Duty, Duty))
        self.assertFalse(DL1.is_less_restrictive(Duty, Undefined))
        self.assertFalse(DL1.is_less_restrictive(Prohibition, Permission))
        self.assertFalse(DL1.is_less_restrictive(Permission, Undefined))
