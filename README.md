# CaLi

[![Build Status](https://travis-ci.com/benjimor/CaLi.svg?branch=master)](https://travis-ci.com/benjimor/CaLi)
[![PyPI version](https://badge.fury.io/py/pycali.svg)](https://badge.fury.io/py/pycali)

A python package that defines a partial order over RDF licenses

# Introduction

CaLi is a lattice-based model for license orderings. This repository contains a python package that implements this model.


Our code uses the ODRL CaLi ordering ⟨A, DL, C<sub>L</sub>, C<sub>→</sub>⟩ such that:
* A is the set of 72 actions of ODRL (e.g., cc:Distribution, cc:ShareAlike, etc.),
* DL is the deontic lattice `Undefined <= Permissions <= Duty <= Prohibition` (actions can be either permitted, obliged, prohibited or not specified; in this deontic lattice, the undefined status is the least restrictive and the prohibited one the most restrictive),
* C<sub>L</sub> and
* C<sub>→</sub> are sets of constraints.

[CaLi online demonstrator](http://cali.priloo.univ-nantes.fr/) Is an exemple of 
license compliant search engine using CaLi model.

# Installation

Installation in a `virtualenv` is recommended.

Assuming you already have `python 3` and `pip` installed

```bash
pip install pycali
```

this will automatically install [rdflib](https://github.com/RDFLib/rdflib) used to manipulate RDF.

# Getting started

This section shows how to create a CaLi ordering with ease.

## Load a vocabulary

A vocabulary object is a set of URIs ([rdflib.term.URIRef](https://rdflib.readthedocs.io/en/stable/rdf_terms.html#urirefs)) identifying actions (e.g., cc:Distribution, cc:ShareAlike, odrl:play, etc.)

Create your own vocabulary inheriting from Vocabulary object or
use the implemented ODRL Vocabulary:

```python
from pycali.vocabulary.vocabulary import ODRLVocabulary

odrl = ODRLVocabulary()
# access the list of actions
odrl.actions
```

## Load a deontic lattice

A deontic lattice is a lattice defining the restrictiveness order between states of the 
actions (permitted, obliged, prohibited).
Repository contains [examples of deontic lattices](https://github.com/benjimor/CaLi/tree/master/cali/examples/deontic_lattices) in RDF.
A Deontic lattice is instanciated using a deontic lattice in RDF ([rdflib.Graph](https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.html?highlight=graph#rdflib.graph.Graph)):

```python
from rdflib import Graph
from pycali.deontic_lattice import DeonticLattice

# Load the deontic lattice in the examples
DL1 = DeonticLattice(Graph().parse(location='.../examples/deontic_lattices/DL1.ttl', format='ttl'))
```

## Load licenses

A license i a set of states associated to actions of the vocabulary.
You can define your own license by creating a class inheriting from License object or 
use the implemented ODRLLicense object.
Repository contains [examples of ODRL licenses dataset](https://github.com/benjimor/CaLi/tree/master/cali/examples/licenses).

### Load a dataset of licenses

ODRLLicenses object is able to generate a set of ODRLlicense object from a rdf dataset of licenses
described using [ODRL Vocabulary](https://www.w3.org/TR/odrl-vocab/):


```python
from pycali.license import ODRLLicenses

ld_licenses_graph = Graph().parse(location='.../examples/licenses/ld_licenses_odrl.ttl',
                                  format='ttl')
licenses = ODRLLicenses(vocabulary=odrl,
                        deontic_lattice=DL1,
                        rdf_graph=ld_licenses_graph)
```

### Load a specific license

IRI of the license can be used to retrieve a specific license:

```python
from pycali.license import ODRLLicense
from rdflib import Graph, URIRef
from pycali.vocabulary.vocabulary import ODRL, CC
from pycali.vocabulary.ontologies.cali_onto import Permission

MIT = URIRef('http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336041529177465061342556133156838395276')

ld_licenses_graph = Graph().parse(location='.../examples/licenses/ld_licenses_odrl.ttl',
                                  format='ttl')
mit_license = ODRLLicense(vocabulary=odrl,
                      deontic_lattice=DL1,
                      rdf_graph=ld_licenses_graph,
                      iri=MIT)
# Returns a list of actions in the specified state
actions = mit_license.get_action(vocabulary=odrl, state=Permission)
# Returns the state of an action
state = mit_license.get_state(vocabulary=odrl, action=ODRL['derive'])
```

## Define constraints

Constraints on license C<sub>L</sub> defines if a license is valid or not. Compatibility constraints C<sub>→</sub>
defines if a restrictiveness relation is a compatibility relation or not.
Repository contains [examples of license and compatibility constraints](https://github.com/benjimor/CaLi/tree/master/cali/examples).

### Constraints on licenses

A constraints on license is a a python function that takes 2 parameters,
a vocabulary and a license and returns a boolean:

```python
from pycali.vocabulary.ontologies.cali_onto import Duty
from pycali.vocabulary.vocabulary import CC

# A License should not obligates the commercial use of a resource
def CommercialUse_Not_Duty(vocabulary, license):
    return license.get_state(vocabulary, CC['CommericalUse']) != Duty
```

### Compatibility constraints

A compatibility constraint is a a python function that takes 3 parameters, a vocabulary and 2 licenses
and returns a boolean:

```python
from pycali.vocabulary.ontologies.cali_onto import Duty
from pycali.vocabulary.vocabulary import CC

# A license that obligates to share alike should not be compatible with another license
def ShareAlike_Compatibility(vocabulary, license1, license2):
    return license1.get_state(vocabulary, CC['ShareAlike']) != Duty
```

### Instanciate constraints

Constraints are instanciated using LicenseConstraints and CompatibilityConstraints objects.
They are initiated with a list of constraints (signature of functions (onstraints) are tested during initialization).

```python
from pycali.constraints import LicenseConstraints, CompatibilityConstraints
from pycali.examples.license_constraints import CommercialUse_Not_Duty, ShareAlike_Not_Prohibition, CommercialUse_Include_Use
from pycali.examples.compatibility_constraints import ShareAlike_Compatibility, DerivativeWorks_Compatibility

license_constraints = LicenseConstraints(odrl, [CommercialUse_Not_Duty, ShareAlike_Not_Prohibition, CommercialUse_Include_Use])
compatibility_constraints = CompatibilityConstraints(ODRL, [ShareAlike_Compatibility, DerivativeWorks_Compatibility])

# Checks if license respects all constraints on license
license_constraints.is_valid(license)
# Checks if the restrictiveness relation between license1 and license2 repects all compatibility relations
compatibility_constraints.is_compatible(license1, license2)
```

## Instantiate a CaLi Ordering (Complete Example)

CaLi ordering automatically defines compatibility relations between licenses.
It takes 4 parameters, the deontic_lattice, the vocabulary, licenses constraints and compatibility constraints.
Then, every license added in the cali_ordering is ordered among other using compatibility relation.

```python
from rdflib import Graph
from pycali.cali_ordering import CaliOrdering
from pycali.deontic_lattice import DeonticLattice
from pycali.license import ODRLLicenses
from pycali.vocabulary.vocabulary import ODRLVocabulary
from pycali.constraints import LicenseConstraints, CompatibilityConstraints
from pycali.examples.license_constraints import CommercialUse_Not_Duty, ShareAlike_Not_Prohibition, CommercialUse_Include_Use
from pycali.examples.compatibility_constraints import ShareAlike_Compatibility, DerivativeWorks_Compatibility

# instantiate a cali ordering
cali_ordering = CaliOrdering(deontic_lattice=DeonticLattice(Graph().parse(location='.../examples/deontic_lattices/DL1.ttl', format='ttl')),
                             vocabulary=ODRLVocabulary(),
                             license_constraints=LicenseConstraints(odrl, [CommercialUse_Not_Duty, ShareAlike_Not_Prohibition, CommercialUse_Include_Use]),
                             compatibility_constraints=CompatibilityConstraints(odrl, [ShareAlike_Compatibility, DerivativeWorks_Compatibility]))
# add licenses to order
licenses = ODRLLicenses(vocabulary=odrl, deontic_lattice=DL1, rdf_graph=ld_licenses_graph)
# use cali_ordering.add_license(license) to add one license
cali_ordering.add_licenses(licenses)
```

### Browse the CaLi Ordering

```python
# checks if license1 is compatible with license2
boolean = cali_ordering.is_compatible(license1, license2)
# checks if license2 is compatible with license1
boolean = cali_ordering.is_compliant(license1, license2)
# Returns all licenses that are compatible with license entered in parameter
licenses = cali_ordering.all_compatible(license)
# Returns all licenses that are compliant with license entered in parameter
licenses = cali_ordering.all_compliant(license)
# Returns an RDF graph containing license IRI's and compatibility relations
rdf_graph = cali_ordering.get_rdf_graph()
# serialize rdf graph in turtle
turtle_string = rdf_graph.serialize(format='turtle')
```