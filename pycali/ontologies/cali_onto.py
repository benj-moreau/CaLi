from rdflib import Namespace

from pycali.vocabulary import ODRL

# Namespace
CALI = Namespace('http://cali.priloo.univ-nantes.fr/ontology#')
ODRS = Namespace('http://schema.theodi.org/odrs#')

# Classes
Status = CALI['Status']

# Properties
lessRestrictiveThan = CALI['lessRestrictiveThan']
compatibleWith = ODRS['compatibleWith']

# Resources
# Status
Undefined = CALI['Undefined']
Recommended = CALI['Recommendation']
Dispensation = CALI['Dispensation']
Permission = ODRL['Permission']
Prohibition = ODRL['Prohibition']
Duty = ODRL['Duty']
