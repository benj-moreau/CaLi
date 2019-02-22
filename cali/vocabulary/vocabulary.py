from rdflib import Graph, RDF, Namespace

ODRL = Namespace('http://www.w3.org/ns/odrl/2/')
CC = Namespace('http://creativecommons.org/ns#')


class Vocabulary(object):
    """A Vocabulary.

    A vocabulary is a set of actions.
    """

    def __init__(self, rdf_vocabulary_graph):
        """
        Vocabulary Constructor.

        Init function accepts a rdf vocabulary (rdflib.Graph)
        and creates an attribute 'actions' containing
        all actions of the vocabulary.
        """
        self.actions = []


class ODRLVocabulary(Vocabulary):
    """The ODRL Vocabulary.

    Contains a set of all actions from ODRL
    vocabulary 2.2
    see. https://www.w3.org/TR/odrl-vocab/#actionConcepts
    """

    def __init__(self, rdf_vocabulary_graph=None):
        """
        Vocabulary Constructor.

        Init function accepts ODRL rdf vocabulary
        and create an attribute 'actions' containing
        all actions of ODRL vocabulary.
        """
        Vocabulary.__init__(self, None)
        odrl = Graph().parse(location='cali/vocabulary/ontologies/ODRL22.rdf')
        for action in odrl.subjects(predicate=RDF.type, object=ODRL['Action']):
            self.actions.append(action)
