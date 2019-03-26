from rdflib import RDF

import pycali.exceptions as exceptions
from pycali.ontologies.cali_onto import Undefined
from pycali.vocabulary import ODRL


class License(object):
    """A License.

    A License is identified by an IRI
    and associates each actions of the vocabulary to status.
    """

    def __init__(self, vocabulary, rls, rdf_graph, iri):
        """
        License Constructor.

        The constructor accepts three arguments,
         - the 'vocabulary',
         - the restrictiveness lattice of status
         - the 'rdf_graph' (rdflib.Graph) that is
        the rdf graph containing the license,
         - the 'iri' (rdflib.URIRef) that is the IRI identifying
        the license in the rdf file'rdf_graph'

        creates an attribute 'iri' and 'statuses' containing
        each status of the actions of the vocabulary.
        """
        if (iri, None, None) in rdf_graph:
            self.iri = iri
            self.statuses = []
        else:
            raise exceptions.MissingLicense

    def get_status(self, vocabulary, action):
        """
        Return the status of the action in the current license.

        Vocabulary parameter should be the same as the one used to instantiate
        the license.
        """
        if len(vocabulary.actions) != len(self.statuses):
            raise exceptions.BadVocabulary()
        for index, voc_action in enumerate(vocabulary.actions):
            if voc_action == action:
                return self.statuses[index]
        raise exceptions.BadVocabulary()

    def get_action(self, vocabulary, status):
        """Return a list of actions from the current license that are in the status."""
        if len(vocabulary.actions) != len(self.statuses):
            raise exceptions.BadVocabulary()
        actions_to_return = []
        for action, action_state in zip(vocabulary.actions, self.statuses):
            if action_state == status:
                actions_to_return.append(action)
        return actions_to_return

    def __hash__(self):
        """Use the iri to identify licenses."""
        return hash(self.iri)

    def __eq__(self, other):
        """Use the iri to compare licenses."""
        return self.iri == other.iri

    def __str__(self):
        """Use the iri to print licenses."""
        return self.iri

    def __repr__(self):
        """Use the iri to represent licenses."""
        return self.iri


class ODRLLicense(License):
    """An ODRL License.

    An ORDL license contains an IRI and
    a set of ODRL actions associated to status
    of the restrictiveness lattice of status.
    """

    def __init__(self, vocabulary, ls, rdf_graph, iri):
        """
        ODRL License Constructor.

        accepts 4 arguments,
        the odrl 'vocabulary', the restrictiveness lattice of status, the 'rdf_graph' (rdflib.Graph) that is
        the rdf file path containing the odrl license and the 'iri'
        (rdflib.URIRef) identifying the license in the rdf file.

        creates an attribute 'iri' and 'status' containing
        all status of the actions of the vocabulary.
        """
        License.__init__(self, vocabulary, ls, rdf_graph, iri)
        for action in vocabulary.actions:
            try:
                status = next(rdf_graph.predicates(subject=iri, object=action))
                self.statuses.append(status)
            except StopIteration:
                if Undefined not in ls.restrictiveness:
                    raise exceptions.MissingAction()
                else:
                    self.statuses.append(Undefined)


def ODRLLicenses(vocabulary, ls, rdf_graph):
    """Instantiate multiple ODRL licenses.

    Accepts 3 arguments:
    the odrl 'vocabulary', the  restrictiveness lattice of status and the 'rdf_graph' (rdflib.Graph) that is
    the rdf file path containing multiple odrl licenses.

    Returns a list of License objects.
    """
    licenses = []
    for iri in rdf_graph.subjects(predicate=RDF.type, object=ODRL['Policy']):
        licenses.append(ODRLLicense(vocabulary, ls, rdf_graph, iri))
    return licenses
