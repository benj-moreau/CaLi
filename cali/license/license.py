from rdflib import Graph, URIRef

import cali.exceptions as exceptions


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
        the license in the rdf file'rdf_license_path'

        creates an attribute 'iri' and 'deontic states' containing
        all deontic states of the actions of the vocabulary.
        """
        self.iri = iri
        self.deontic_states = []


class ODRLLicense(object):
    """An ODRL License.

    An ORDL license contains an IRI and
    a set of ODRL actions associated to deontic states
    of the deontic lattice.
    """

    def __init__(self, vocabulary, deontic_lattice, rdf_graph, iri):
        """
        ODRL License Constructor.

        accepts three arguments,
        the odrl 'vocabulary', the 'rdf_license_path' that is
        the rdf file path containing the odrl license and the 'iri'
        (rdflib.URIRef) identifying the license in the rdf file.

        creates an attribute 'iri' and 'deontic states' containing
        all deontic states of the actions of the vocabulary.
        """
        # TODO: HANDLE DEONTIC LATTICE
        License.__init__(self, iri)
        for action in vocabulary.actions:
            try:
                deontic_status = rdf_graph.predicates(subject=iri, object=action).next()
                self.deontic_states.append(deontic_status)
            except StopIteration:
                if 'undefined' not in deontic_lattice:
                    raise exceptions.MissingAction()
                else:
                    self.deontic_states.append(URIRef('UNDEFINED'))
