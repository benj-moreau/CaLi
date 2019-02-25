from rdflib import RDF

import cali.exceptions as exceptions
from cali.vocabulary.ontologies.cali_onto import Undefined
from cali.vocabulary.vocabulary import ODRL


class License(object):
    """A License.

    A License is identified by an IRI
    and associates each actions of the vocabulary to
    deontic states.
    """

    def __init__(self, vocabulary, deontic_lattice, rdf_graph, iri):
        """
        License Constructor.

        The constructor accepts three arguments,
         - the 'vocabulary',
         - the 'rdf_graph' (rdflib.Graph) that is
        the rdf graph containing the license,
         - the 'iri' (rdflib.URIRef) that is the IRI identifying
        the license in the rdf file'rdf_graph'

        creates an attribute 'iri' and 'deontic states' containing
        all deontic states of the actions of the vocabulary.
        """
        if (iri, None, None) in rdf_graph:
            self.iri = iri
            self.deontic_states = []
        else:
            raise(exceptions.MissingLicense)

    def get_state(self, vocabulary, action):
        """
        Return the state of the action in the current license.

        Vocabulary parameter should be the same as the one used to instanciated
        the license.
        """
        if len(vocabulary.actions) != len(self.deontic_states):
            raise exceptions.BadVocabulary()
        for index, voc_action in enumerate(vocabulary.actions):
            if voc_action == action:
                return self.deontic_states[index]
        raise exceptions.BadVocabulary()

    def get_action(self, vocabulary, state):
        """Return a list of actions from the current license that are in the state."""
        if len(vocabulary.actions) != len(self.deontic_states):
            raise exceptions.BadVocabulary()
        actions_to_return = []
        for action, action_state in zip(vocabulary.actions, self.deontic_states):
            if action_state == state:
                actions_to_return.append(action)
        return actions_to_return

    def __hash__(self):
        """Use the iri to identify licenses."""
        return hash(self.iri)

    def __eq__(self, other):
        """Use the iri to compare licenses."""
        return (self.iri == other.iri)

    def __str__(self):
        """Use the iri to print licenses."""
        return self.iri

    def __repr__(self):
        """Use the iri to represent licenses."""
        return self.iri


class ODRLLicense(License):
    """An ODRL License.

    An ORDL license contains an IRI and
    a set of ODRL actions associated to deontic states
    of the deontic lattice.
    """

    def __init__(self, vocabulary, deontic_lattice, rdf_graph, iri):
        """
        ODRL License Constructor.

        accepts 4 arguments,
        the odrl 'vocabulary', the 'rdf_graph' (rdflib.Graph) that is
        the rdf file path containing the odrl license and the 'iri'
        (rdflib.URIRef) identifying the license in the rdf file.

        creates an attribute 'iri' and 'deontic states' containing
        all deontic states of the actions of the vocabulary.
        """
        License.__init__(self, vocabulary, deontic_lattice, rdf_graph, iri)
        for action in vocabulary.actions:
            try:
                deontic_status = next(rdf_graph.predicates(subject=iri, object=action))
                self.deontic_states.append(deontic_status)
            except StopIteration:
                if Undefined not in deontic_lattice.restrictiveness:
                    raise exceptions.MissingAction()
                else:
                    self.deontic_states.append(Undefined)


def ODRLLicenses(vocabulary, deontic_lattice, rdf_graph):
    """Instanciate multiple ODRL licenses.

    Accepts 3 arguments:
    the odrl 'vocabulary', the  deontic lattice and the 'rdf_graph' (rdflib.Graph) that is
    the rdf file path containing multiple odrl licenses.

    Returns a list of License objects.
    """
    licenses = []
    for iri in rdf_graph.subjects(predicate=RDF.type, object=ODRL['Policy']):
        licenses.append(ODRLLicense(vocabulary, deontic_lattice, rdf_graph, iri))
    return licenses
