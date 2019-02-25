from rdflib import URIRef

from unittest import TestCase

from pycali.vocabulary.vocabulary import ODRLVocabulary


class testVocabularies(TestCase):
    """Test if vocabularies are well instanciated as list of actions."""

    def test_odrl_vocabulary(self):
        """Test if ODRL vocabulary is well instanciated."""
        ODRL = ODRLVocabulary()
        self.assertEqual(len(ODRL.actions), 72)
        self.assertIn(URIRef('http://creativecommons.org/ns#Attribution'), ODRL.actions)
        self.assertIn(URIRef('http://www.w3.org/ns/odrl/2/use'), ODRL.actions)
