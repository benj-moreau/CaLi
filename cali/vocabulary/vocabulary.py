from rdflib import Graph, URIRef, RDF


class Vocabulary(object):
    """A Vocabulary.

    A vocabulary is a set of actions.
    The constructor accepts one argument,
    the 'rdf_vocabulary_path' that is the path to the
    rdf vocabulary containing the actions.
    """

    def __init__(self, rdf_vocabulary_path):
        """
        Vocabulary Constructor.

        Init function accepts a rdf vocabulary
        and create an attribute 'actions' containing
        all actions of the vocabulary.
        """
        self.actions = []


class ODRLVocabulary(Vocabulary):
    """The ODRL Vocabulary.

    Contains a set of all actions from ODRL
    vocabulary 2.2
    see. https://www.w3.org/TR/odrl-vocab/#actionConcepts
    """

    def __init__(self, rdf_vocabulary_path='cali/vocabulary/ontologies/ODRL22.rdf'):
        """
        Vocabulary Constructor.

        Init function accepts ODRL rdf vocabulary
        and create an attribute 'actions' containing
        all actions of ODRL vocabulary.
        """
        Vocabulary.__init__(self, None)
        ODRL = Graph().parse(location=rdf_vocabulary_path)
        ODRL_action_type = URIRef('http://www.w3.org/ns/odrl/2/Action')
        for action in ODRL.subjects(predicate=RDF.type, object=ODRL_action_type):
            self.actions.append(action)