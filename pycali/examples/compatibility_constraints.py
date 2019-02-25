from pycali.vocabulary.ontologies.cali_onto import Duty, Prohibition
from pycali.vocabulary.vocabulary import CC


def ShareAlike_Compatibility(vocabulary, license1, license2):
    return license1.get_state(vocabulary, CC['ShareAlike']) != Duty


def DerivativeWorks_Compatibility(vocabulary, license1, license2):
    return license1.get_state(vocabulary, CC['DerivativeWorks']) != Prohibition
