from rdflib import Graph, RDF

from cali.vocabulary.ontologies.cali_onto import DeonticState, lessRestrictiveThan


class DeonticLattice(object):
    """
    A deontic lattice.

    Implemented with Dict.
    Contains Deontic states (Permision, Obligation, etc.)
    partially ordered by restrictiveness.
    """

    def __init__(self, rdf_deontic_lattice_path, format):
        """
        Deontic Lattice Constructor.

        Init function accepts a path to an rdf deontic lattice
        described using cali ontology and the rdf format of the deontic lattice.
        ('ttl', 'xml', 'n3' accepted).
        Constructs a Dict representing the restrictiveness ordered
        between deontic states.
        """
        self.moreRestrictiveThan = {}
        DL = Graph().parse(location=rdf_deontic_lattice_path, format=format)
        for deontic_state in DL.subjects(predicate=RDF.type, object=DeonticState):
            # restrictiveness relation is reflexive
            more_restrictive = [deontic_state]
            _rec_restrictives(DL, deontic_state, more_restrictive)
            self.moreRestrictiveThan[deontic_state] = more_restrictive

    def is_less_restrictive(self, state1, state2):
        """Return True if state1 is less restrictive than state2. Return False otherwise."""
        return state2 in self.moreRestrictiveThan[state1]


def _rec_restrictives(DL, deontic_state, more_restrictive):
    # recursively find for more restrictives states (transitivity)
    for more_restrictive_deontic_state in DL.objects(subject=deontic_state, predicate=lessRestrictiveThan):
        if more_restrictive_deontic_state not in more_restrictive:
            more_restrictive.append(more_restrictive_deontic_state)
        if deontic_state is not more_restrictive_deontic_state:
            _rec_restrictives(DL, more_restrictive_deontic_state, more_restrictive)
