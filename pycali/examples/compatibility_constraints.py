from pycali.ontologies.cali_onto import Duty, Prohibition
from pycali.vocabulary import CC


def ShareAlike_Compatibility(vocabulary, license1, license2):
    return license1.get_status(vocabulary, CC['ShareAlike']) != Duty


def DerivativeWorks_Compatibility(vocabulary, license1, license2):
    return license1.get_status(vocabulary, CC['DerivativeWorks']) != Prohibition
