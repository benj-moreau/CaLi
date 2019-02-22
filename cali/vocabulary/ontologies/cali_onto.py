from rdflib import Namespace

from cali.vocabulary.vocabulary import ODRL

# Namespace
CALI = Namespace('http://cali.priloo.univ-nantes.fr/ontology#')

# Classes
DeonticState = CALI['DeonticState']

# Properties
lessRestrictiveThan = CALI['lessRestrictiveThan']

# Resources
# Deontic states
Undefined = CALI['Undefined']
Recommended = CALI['Recommended']
Permission = ODRL['Permission']
Prohibition = ODRL['Prohibition']
Duty = ODRL['Duty']
