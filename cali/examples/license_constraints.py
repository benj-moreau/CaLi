from rdflib import URIRef
from cali.vocabulary.ontologies.cali_onto import Duty, Prohibition, Permission


def CommercialUse_Not_Duty(vocabulary, license):
    return license.get_state(vocabulary, URIRef('http://creativecommons.org/ns#CommericalUse')) != Duty


def ShareAlike_Not_Prohibition(vocabulary, license):
    return license.get_state(vocabulary, URIRef('http://creativecommons.org/ns#ShareAlike')) != Prohibition


def CommercialUse_Include_Use(vocabulary, license):
    if license.get_state(vocabulary, URIRef('http://www.w3.org/ns/odrl/2/use')) == Prohibition:
        if (
            license.get_state(vocabulary, URIRef('http://creativecommons.org/ns#CommericalUse')) == Permission or
            license.get_state(vocabulary, URIRef('http://creativecommons.org/ns#CommericalUse')) == Duty
           ):
            return False
    return True
