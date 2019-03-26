from rdflib import RDF

from pycali.ontologies.cali_onto import Status, lessRestrictiveThan
from pycali.exceptions import MissingStatus


class RestrictivenessLatticeOfStatus(object):
    """
    A Restrictiveness Lattice Of Status.

    Implemented with Dict.
    Contains status (Permision, Obligation, etc.)
    partially ordered by restrictiveness.
    """

    def __init__(self, rdf_ls_graph):
        """
        Restrictiveness Lattice Of Status Constructor.

        Init function accepts a rdf Restrictiveness Lattice Of Status (rdflib.Graph)
        described using cali ontology.
        Constructs a Dict representing the restrictiveness ordered
        between status.
        """
        self.restrictiveness = {}
        for status in rdf_ls_graph.subjects(predicate=RDF.type, object=Status):
            # restrictiveness relation is reflexive
            more_restrictives = [status]
            _rec_restrictives(rdf_ls_graph, status, more_restrictives)
            self.restrictiveness[status] = more_restrictives

    def is_less_restrictive(self, status1, status2):
        """Return True if status1 is less restrictive than status2. Return False otherwise."""
        if status1 in self.restrictiveness:
            return status2 in self.restrictiveness[status1]
        raise MissingStatus


def _rec_restrictives(ls, status, more_restrictives):
    # recursively find for more restrictives states (transitivity)
    for more_restrictive_status in ls.objects(subject=status, predicate=lessRestrictiveThan):
        if more_restrictive_status not in more_restrictives:
            more_restrictives.append(more_restrictive_status)
        if status is not more_restrictive_status:
            _rec_restrictives(ls, more_restrictive_status, more_restrictives)
