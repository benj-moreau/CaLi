from rdflib import URIRef
from cali.vocabulary.ontologies.cali_onto import Duty, Prohibition


def ShareAlike_Compatibility(vocabulary, license1, license2):
    return license1.get_state(vocabulary, URIRef('http://creativecommons.org/ns#ShareAlike')) != Duty


def DerivativeWorks_Compatibility(vocabulary, license1, license2):
    return license1.get_state(vocabulary, URIRef('http://creativecommons.org/ns#DerivativeWorks')) != Prohibition
