from rdflib import Graph


class License(object):
    """A License.

    A License is identified by an IRI
    and contains a set of deontic states.
    The constructor accepts three arguments,
    the 'vocabulary', the 'rdf_license_path' that is
    the rdf file path containing the license and the 'iri'
    that is the IRI identifying the license in the rdf file
    'rdf_license_path'.
    """

    def __init__(self, vocabulary, rdf_license_path, iri):
        """
        License Constructor.

        The constructor accepts three arguments,
        the 'vocabulary', the 'rdf_license_path' that is
        the rdf file path containing the license and the 'iri'
        that is the IRI identifying the license in the rdf file
        'rdf_license_path'
        creates an attribute 'iri' and 'deontic states' containing
        all deontic states of the actions of the vocabulary.
        """
        self.iri = iri
        self.deontic_states = []


class ODRLLicense(object):
    """An ODRL License.

    The constructor accepts three arguments,
    the odrl 'vocabulary', the 'rdf_license_path' that is
    the rdf file path containing the odrl license and the 'iri'
    identifying the license in the rdf file.
    """

    def __init__(self, vocabulary, rdf_license_path, iri):
        """
        License Constructor.

        creates an attribute 'iri' and 'deontic states' containing
        all deontic states of the actions of the vocabulary.
        """
        License.__init__(self, iri)
        self.deontic_states = []
