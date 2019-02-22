from rdflib import RDF

from cali.vocabulary.ontologies.cali_onto import DeonticState, lessRestrictiveThan


class DeonticLattice(object):
    """
    A deontic lattice.

    Implemented with Dict.
    Contains Deontic states (Permision, Obligation, etc.)
    partially ordered by restrictiveness.
    """

    def __init__(self, rdf_deontic_graph):
        """
        Deontic Lattice Constructor.

        Init function accepts a rdf deontic lattice (rdflib.Graph)
        described using cali ontology.
        Constructs a Dict representing the restrictiveness ordered
        between deontic states.
        """
        self.restrictiveness = {}
        for deontic_state in rdf_deontic_graph.subjects(predicate=RDF.type, object=DeonticState):
            # restrictiveness relation is reflexive
            more_restrictive = [deontic_state]
            _rec_restrictives(rdf_deontic_graph, deontic_state, more_restrictive)
            self.restrictiveness[deontic_state] = more_restrictive

    def is_less_restrictive(self, state1, state2):
        """Return True if state1 is less restrictive than state2. Return False otherwise."""
        return state2 in self.restrictiveness[state1]


def _rec_restrictives(DL, deontic_state, more_restrictive):
    # recursively find for more restrictives states (transitivity)
    for more_restrictive_deontic_state in DL.objects(subject=deontic_state, predicate=lessRestrictiveThan):
        if more_restrictive_deontic_state not in more_restrictive:
            more_restrictive.append(more_restrictive_deontic_state)
        if deontic_state is not more_restrictive_deontic_state:
            _rec_restrictives(DL, more_restrictive_deontic_state, more_restrictive)
