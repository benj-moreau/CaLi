from pycali.ontologies.cali_onto import Duty, Prohibition, Permission
from pycali.vocabulary import ODRL, CC


def CommercialUse_Not_Duty(vocabulary, license):
    return license.get_status(vocabulary, CC['CommericalUse']) != Duty


def ShareAlike_Not_Prohibition(vocabulary, license):
    return license.get_status(vocabulary, CC['ShareAlike']) != Prohibition


def CommercialUse_Include_Use(vocabulary, license):
    if license.get_status(vocabulary, ODRL['use']) == Prohibition:
        if (
            license.get_status(vocabulary, CC['CommericalUse']) == Permission or
            license.get_status(vocabulary, CC['CommericalUse']) == Duty
           ):
            return False
    return True
