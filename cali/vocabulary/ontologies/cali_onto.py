from rdflib import Namespace

"""
Contains Classes, Properties
and some resources of CaLi.
"""

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
