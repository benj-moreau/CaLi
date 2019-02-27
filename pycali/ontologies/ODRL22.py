rdf_odrl = """<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:cc="http://creativecommons.org/ns#"
   xmlns:dct="http://purl.org/dc/terms/"
   xmlns:foaf="http://xmlns.com/foaf/0.1/"
   xmlns:owl="http://www.w3.org/2002/07/owl#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
   xmlns:schema="http://schema.org/"
   xmlns:skos="http://www.w3.org/2004/02/skos/core#"
   xmlns:vcard="http://www.w3.org/2006/vcard/ns#"
   xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
   xmlns="http://www.w3.org/ns/odrl/2/">
  <Action rdf:about="http://creativecommons.org/ns#Attribution">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Attribution</rdfs:label>
    <skos:definition xml:lang="en">Credit be given to copyright holder and/or author.</skos:definition>
    <skos:note xml:lang="en">This term is defined by Creative Commons.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Action rdf:about="http://creativecommons.org/ns#CommericalUse">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Commercial Use</rdfs:label>
    <skos:definition xml:lang="en">Exercising rights for commercial purposes.</skos:definition>
    <skos:note xml:lang="en">This term is defined by Creative Commons.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Action rdf:about="http://creativecommons.org/ns#DerivativeWorks">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Derivative Works</rdfs:label>
    <skos:definition xml:lang="en">Distribution of derivative works.</skos:definition>
    <skos:note xml:lang="en">This term is defined by Creative Commons.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Action rdf:about="http://creativecommons.org/ns#Distribution">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Distribution</rdfs:label>
    <skos:definition xml:lang="en">Distribution, public display, and publicly performance.</skos:definition>
    <skos:note xml:lang="en">This term is defined by Creative Commons.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Action rdf:about="http://creativecommons.org/ns#Notice">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Notice</rdfs:label>
    <skos:definition xml:lang="en">Copyright and license notices be kept intact.</skos:definition>
    <skos:note xml:lang="en">This term is defined by Creative Commons.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Action rdf:about="http://creativecommons.org/ns#Reproduction">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Reproduction</rdfs:label>
    <skos:definition xml:lang="en">Making multiple copies.</skos:definition>
    <skos:note xml:lang="en">This term is defined by Creative Commons.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Action rdf:about="http://creativecommons.org/ns#ShareAlike">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Share Alike</rdfs:label>
    <skos:definition xml:lang="en">Derivative works be licensed under the same terms or compatible terms as the original work.</skos:definition>
    <skos:note xml:lang="en">This term is defined by Creative Commons.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Action rdf:about="http://creativecommons.org/ns#Sharing">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Sharing</rdfs:label>
    <skos:definition xml:lang="en">Permits commercial derivatives, but only non-commercial distribution.</skos:definition>
    <skos:note xml:lang="en">This term is defined by Creative Commons.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Action rdf:about="http://creativecommons.org/ns#SourceCode">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Source Code</rdfs:label>
    <skos:definition xml:lang="en">Source code (the preferred form for making modifications) must be provided when exercising some rights granted by the license.</skos:definition>
    <skos:note xml:lang="en">This term is defined by Creative Commons.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <owl:AnnotationProperty rdf:about="http://purl.org/dc/terms/contributor"/>
  <owl:AnnotationProperty rdf:about="http://purl.org/dc/terms/creator"/>
  <owl:AnnotationProperty rdf:about="http://purl.org/dc/terms/description"/>
  <owl:AnnotationProperty rdf:about="http://purl.org/dc/terms/format"/>
  <owl:AnnotationProperty rdf:about="http://purl.org/dc/terms/isVersionOf"/>
  <owl:AnnotationProperty rdf:about="http://purl.org/dc/terms/issued"/>
  <owl:AnnotationProperty rdf:about="http://purl.org/dc/terms/license"/>
  <owl:AnnotationProperty rdf:about="http://purl.org/dc/terms/subject"/>
  <owl:Class rdf:about="http://www.w3.org/2004/02/skos/core#Collection"/>
  <owl:Class rdf:about="http://www.w3.org/2004/02/skos/core#Concept"/>
  <owl:Class rdf:about="http://www.w3.org/2004/02/skos/core#ConceptScheme"/>
  <owl:AnnotationProperty rdf:about="http://www.w3.org/2004/02/skos/core#broader"/>
  <owl:AnnotationProperty rdf:about="http://www.w3.org/2004/02/skos/core#broaderTransitive"/>
  <owl:AnnotationProperty rdf:about="http://www.w3.org/2004/02/skos/core#definition"/>
  <owl:AnnotationProperty rdf:about="http://www.w3.org/2004/02/skos/core#hasTopConcept"/>
  <owl:AnnotationProperty rdf:about="http://www.w3.org/2004/02/skos/core#member"/>
  <owl:AnnotationProperty rdf:about="http://www.w3.org/2004/02/skos/core#note"/>
  <owl:AnnotationProperty rdf:about="http://www.w3.org/2004/02/skos/core#prefLabel"/>
  <owl:AnnotationProperty rdf:about="http://www.w3.org/2004/02/skos/core#scopeNote"/>
  <owl:Ontology rdf:about="http://www.w3.org/ns/odrl/2/">
    <dct:contributor>W3C Permissions &amp; Obligations Expression Working Group</dct:contributor>
    <dct:creator>Michael Steidl</dct:creator>
    <dct:creator>Renato Iannella</dct:creator>
    <dct:creator>Stuart Myles</dct:creator>
    <dct:creator>Víctor Rodríguez-Doncel</dct:creator>
    <dct:description xml:lang="en">The ODRL Vocabulary and Expression defines a set of concepts and terms (the vocabulary) and encoding mechanism (the expression) for permissions and obligations statements describing digital content usage based on the ODRL Information Model.</dct:description>
    <dct:license rdf:resource="https://www.w3.org/Consortium/Legal/2002/ipr-notice-20021231#Copyright/"/>
    <rdfs:comment xml:lang="en">This is the RDF ontology for ODRL Version 2.2.</rdfs:comment>
    <rdfs:label xml:lang="en">ODRL Version 2.2</rdfs:label>
    <owl:versionInfo>2.2</owl:versionInfo>
  </owl:Ontology>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#actionConcepts">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Action"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/action"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/implies"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/includedIn"/>
    <skos:prefLabel xml:lang="en">Action</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Core Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#actions">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/transfer"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
    <skos:prefLabel xml:lang="en">Actions for Rules</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Core Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#actionsCommon">
    <skos:member rdf:resource="http://creativecommons.org/ns#Attribution"/>
    <skos:member rdf:resource="http://creativecommons.org/ns#CommericalUse"/>
    <skos:member rdf:resource="http://creativecommons.org/ns#DerivativeWorks"/>
    <skos:member rdf:resource="http://creativecommons.org/ns#Distribution"/>
    <skos:member rdf:resource="http://creativecommons.org/ns#Notice"/>
    <skos:member rdf:resource="http://creativecommons.org/ns#Reproduction"/>
    <skos:member rdf:resource="http://creativecommons.org/ns#ShareAlike"/>
    <skos:member rdf:resource="http://creativecommons.org/ns#Sharing"/>
    <skos:member rdf:resource="http://creativecommons.org/ns#SourceCode"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/acceptTracking"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/aggregate"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/annotate"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/anonymize"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/archive"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/attribute"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/compensate"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/concurrentUse"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/delete"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/derive"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/digitize"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/display"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/distribute"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/ensureExclusivity"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/execute"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/extract"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/give"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/grantUse"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/include"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/index"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/inform"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/install"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/modify"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/move"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/nextPolicy"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/obtainConsent"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/play"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/present"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/print"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/read"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/reproduce"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/reviewPolicy"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/sell"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/stream"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/synchronize"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/textToSpeech"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/transform"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/translate"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/uninstall"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/watermark"/>
    <skos:prefLabel xml:lang="en">Actions for Rules</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Common Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#assetConcepts">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Asset"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/AssetCollection"/>
    <skos:prefLabel xml:lang="en">Asset</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Core Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#assetParty">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/partOf"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/source"/>
    <skos:prefLabel xml:lang="en">Asset and Party</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Core Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#assetRelations">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/hasPolicy"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/target"/>
    <skos:prefLabel xml:lang="en">Asset Relations</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Core Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#assetRelationsCommon">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/output"/>
    <skos:prefLabel xml:lang="en">Asset Relations</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Common Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#conflictConcepts">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/ConflictTerm"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/conflict"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/invalid"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/perm"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/prohibit"/>
    <skos:prefLabel xml:lang="en">Policy Conflict Strategy</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Core Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#constraintLeftOperandCommon">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/absolutePosition"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/absoluteSize"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/absoluteSpatialPosition"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/absoluteTemporalPosition"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/count"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/dateTime"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/delayPeriod"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/deliveryChannel"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/elapsedTime"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/event"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/fileFormat"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/industry"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/language"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/media"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/meteredTime"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/payAmount"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/percentage"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/product"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/purpose"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/recipient"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/relativePosition"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/relativeSize"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/relativeSpatialPosition"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/relativeTemporalPosition"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/resolution"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/spatial"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/spatialCoordinates"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/systemDevice"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/timeInterval"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/unitOfCount"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/version"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/virtualLocation"/>
    <skos:prefLabel xml:lang="en">Constraint Left Operands</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Common Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#constraintLogicalOperands">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/and"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/andSequence"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/or"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/xone"/>
    <skos:prefLabel xml:lang="en">Logical Constraint Operands</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Core Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#constraintRelationalOperators">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/eq"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/gt"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/gteq"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/hasPart"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/isA"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/isAllOf"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/isAnyOf"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/isNoneOf"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/isPartOf"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/lt"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/lteq"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/neq"/>
    <skos:prefLabel xml:lang="en">Constraint Operators</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Core Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#constraintRightOpCommon">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/policyUsage"/>
    <skos:prefLabel xml:lang="en">Constraint Right Operands</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Common Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#constraints">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Constraint"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/LeftOperand"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Operator"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/RightOperand"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/constraint"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/dataType"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/leftOperand"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/operator"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/refinement"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/rightOperand"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/rightOperandReference"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/status"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/unit"/>
    <skos:prefLabel xml:lang="en">Constraint</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Core Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#deprecatedTerms">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/All"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/All2ndConnections"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/AllConnections"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/AllGroups"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/AssetScope"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Group"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Individual"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/PartyScope"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/UndefinedTerm"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/adHocShare"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/append"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/appendTo"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/attachPolicy"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/attachSource"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/commercialize"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/copy"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/device"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/export"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/extractChar"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/extractPage"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/extractWord"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/ignore"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/inheritAllowed"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/inheritRelation"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/lease"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/lend"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/license"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/pay"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/payeeParty"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/preview"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/proximity"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/scope"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/secondaryUse"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/share"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/shareAlike"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/support"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/system"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/timedCount"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/undefined"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/write"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/writeTo"/>
    <skos:prefLabel xml:lang="en">Deprecated Terms</skos:prefLabel>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#duties">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Duty"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/consequence"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/duty"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/obligation"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/remedy"/>
    <skos:prefLabel xml:lang="en">Duty</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Core Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#logicalConstraints">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/LogicalConstraint"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/operand"/>
    <skos:prefLabel xml:lang="en">Logical Constraint</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Core Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#partyConcepts">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Party"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/PartyCollection"/>
    <skos:prefLabel xml:lang="en">Party</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Core Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#partyRoles">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/assignee"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/assigneeOf"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/assigner"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/assignerOf"/>
    <skos:prefLabel xml:lang="en">Party Functions</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Core Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#partyRolesCommon">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/attributedParty"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/attributingParty"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/compensatedParty"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/compensatingParty"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/consentedParty"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/consentingParty"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/contractedParty"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/contractingParty"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/informedParty"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/informingParty"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/trackedParty"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/trackingParty"/>
    <skos:prefLabel xml:lang="en">Party Functions</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Common Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#permissions">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Permission"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/permission"/>
    <skos:prefLabel xml:lang="en">Permission</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Core Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#policyConcepts">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/inheritFrom"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/profile"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/uid"/>
    <skos:prefLabel xml:lang="en">Policy</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Core Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#policySubClasses">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Agreement"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Offer"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Set"/>
    <skos:prefLabel xml:lang="en">Policy Subclasses</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Core Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#policySubClassesCommon">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Assertion"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Privacy"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Request"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Ticket"/>
    <skos:prefLabel xml:lang="en">Policy Subclasses</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Common Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#prohibitions">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Prohibition"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/prohibition"/>
    <skos:prefLabel xml:lang="en">Prohibition</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Core Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <skos:Collection rdf:about="http://www.w3.org/ns/odrl/2/#ruleConcepts">
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/Rule"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/failure"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/function"/>
    <skos:member rdf:resource="http://www.w3.org/ns/odrl/2/relation"/>
    <skos:prefLabel xml:lang="en">Rule</skos:prefLabel>
    <skos:scopeNote xml:lang="en">ODRL Core Vocabulary Terms</skos:scopeNote>
  </skos:Collection>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/Action">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Action</rdfs:label>
    <rdfs:subClassOf rdf:resource="http://schema.org/Action"/>
    <skos:definition xml:lang="en">An operation on an Asset.</skos:definition>
    <skos:note xml:lang="en">Actions may be allowed by Permissions, disallowed by Prohibitions, or made mandatory by Duties.</skos:note>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/Agreement">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Agreement</rdfs:label>
    <rdfs:subClassOf rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Assertion"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Offer"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Privacy"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Request"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Ticket"/>
    <skos:definition xml:lang="en">A Policy that grants the assignee a Rule over an Asset from an assigner.</skos:definition>
    <skos:note xml:lang="en">An Agreement Policy MUST contain at least one Permission or Prohibition rule, a Party with Assigner function, and a Party with Assignee function (in the same Permission or Prohibition). The Agreement Policy will grant the terms of the Policy from the Assigner to the Assignee.</skos:note>
  </rdfs:Class>
  <PartyScope rdf:about="http://www.w3.org/ns/odrl/2/All">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">All</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">Specifies that the scope of the relationship is all of the collective individuals within a context.</skos:definition>
    <skos:note xml:lang="en">For example, may be used to indicate all the users of a specific social network the party is a member of. Note that “group” scope is also assumed.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </PartyScope>
  <PartyScope rdf:about="http://www.w3.org/ns/odrl/2/All2ndConnections">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">All Second-level Connections</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">Specifies that the scope of the relationship is all of the second-level connections to the Party.</skos:definition>
    <skos:note xml:lang="en">For example, may be used to indicate all “friends of friends” of the Party. Note that “group” scope is also assumed.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </PartyScope>
  <PartyScope rdf:about="http://www.w3.org/ns/odrl/2/AllConnections">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">All First-Level Connections</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">Specifies that the scope of the relationship is all of the first-level connections of the Party.</skos:definition>
    <skos:note xml:lang="en">For example, may be used to indicate all “friends” of the Party. Note that “group” scope is also assumed.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </PartyScope>
  <PartyScope rdf:about="http://www.w3.org/ns/odrl/2/AllGroups">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">All Group Connections</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">Specifies that the scope of the relationship is all of the group connections of the Party.</skos:definition>
    <skos:note xml:lang="en">For example, may be used to indicate all groups that the Party is a member of. Note that “group” scope is also assumed.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </PartyScope>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/Assertion">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Assertion</rdfs:label>
    <rdfs:subClassOf rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Offer"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Privacy"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Request"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Ticket"/>
    <skos:definition xml:lang="en">A Policy that asserts a Rule over an Asset from parties.</skos:definition>
    <skos:note xml:lang="en">For example, a party (an assignee or assigner) can claim what terms they have over an Asset. An Assertion Policy does not grant such permissions/prohibitions but only asserts the parties claims. An Assetion Policy  MUST contain a target Asset, a Party with any functional role, and at least one of a Permission or Prohibition rule.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/Asset">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Asset</rdfs:label>
    <skos:definition xml:lang="en">A resource or a collection of resources that are the subject of a Rule.</skos:definition>
    <skos:note xml:lang="en">The Asset entity can be any form of identifiable resource, such as data/information, content/media, applications, or services. Furthermore, it can be used to represent other Asset entities that are needed to undertake the Policy expression, such as with the Duty entity. To describe more details about the Asset, it is recommended to use Dublin Core [[dcterms]] elements or other content metadata.</skos:note>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/AssetCollection">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Asset Collection</rdfs:label>
    <rdfs:subClassOf rdf:resource="http://www.w3.org/ns/odrl/2/Asset"/>
    <skos:definition xml:lang="en">An Asset that is collection of individual resources</skos:definition>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/AssetScope">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Asset Scope</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">Scopes for Asset Scope expressions.</skos:definition>
    <skos:note xml:lang="en">Instances of the AssetScope class represent the terms for the scope property of Assets.</skos:note>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/ConflictTerm">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Conflict Strategy Preference</rdfs:label>
    <skos:definition xml:lang="en">Used to establish strategies to resolve conflicts that arise from the merging of Policies or conflicts between Permissions and Prohibitions in the same Policy.</skos:definition>
    <skos:note xml:lang="en">Instances of ConflictTerm describe strategies for resolving conflicts.</skos:note>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/Constraint">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Constraint</rdfs:label>
    <skos:definition xml:lang="en">A boolean expression that refines the semantics of an Action and Party/Asset Collection or declare the conditions applicable to a Rule.</skos:definition>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/Duty">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Duty</rdfs:label>
    <rdfs:subClassOf rdf:resource="http://www.w3.org/ns/odrl/2/Rule"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Permission"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Prohibition"/>
    <skos:definition xml:lang="en">The obligation to perform an Action</skos:definition>
  </rdfs:Class>
  <PartyScope rdf:about="http://www.w3.org/ns/odrl/2/Group">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Group</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">Specifies that the scope of the relationship is the defined group with multiple individual members.</skos:definition>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </PartyScope>
  <PartyScope rdf:about="http://www.w3.org/ns/odrl/2/Individual">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Individual</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">Specifies that the scope of the relationship is the single Party individual.</skos:definition>
  </PartyScope>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/LeftOperand">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Left Operand</rdfs:label>
    <skos:definition xml:lang="en">Left operand for a constraint expression.</skos:definition>
    <skos:note xml:lang="en">Instances of the LeftOperand class are used as the leftOperand of a Constraint.</skos:note>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/LogicalConstraint">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Logical Constraint</rdfs:label>
    <skos:definition xml:lang="en">A logical expression that refines the semantics of an Action and Party/Asset Collection or declare the conditions applicable to a Rule.</skos:definition>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/Offer">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Offer</rdfs:label>
    <rdfs:subClassOf rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Agreement"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Assertion"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Privacy"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Request"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Ticket"/>
    <skos:definition xml:lang="en">A Policy that proposes a Rule over an Asset from an assigner.</skos:definition>
    <skos:note xml:lang="en">An Offer Policy MUST contain at least one Permission or Prohibition rule and a Party with Assigner function (in the same Permission or Prohibition). The Offer Policy MAY contain a Party with Assignee function, but MUST not grant any privileges to that Party.</skos:note>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/Operator">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Operator</rdfs:label>
    <skos:definition xml:lang="en">Operator for constraint expression.</skos:definition>
    <skos:note xml:lang="en">Instances of the Operator class representing relational operators.</skos:note>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/Party">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Party</rdfs:label>
    <rdfs:subClassOf>
      <owl:Class>
        <owl:unionOf>
          <rdf:Description>
            <rdf:first rdf:resource="http://schema.org/Person"/>
            <rdf:rest>
              <rdf:Description>
                <rdf:first rdf:resource="http://schema.org/Organization"/>
                <rdf:rest>
                  <rdf:Description>
                    <rdf:first rdf:resource="http://xmlns.com/foaf/0.1/Person"/>
                    <rdf:rest>
                      <rdf:Description>
                        <rdf:first rdf:resource="http://xmlns.com/foaf/0.1/Organization"/>
                        <rdf:rest>
                          <rdf:Description>
                            <rdf:first rdf:resource="http://xmlns.com/foaf/0.1/Agent"/>
                            <rdf:rest>
                              <rdf:Description>
                                <rdf:first rdf:resource="http://www.w3.org/2006/vcard/ns#Individual"/>
                                <rdf:rest>
                                  <rdf:Description>
                                    <rdf:first rdf:resource="http://www.w3.org/2006/vcard/ns#Organization"/>
                                    <rdf:rest>
                                      <rdf:Description>
                                        <rdf:first rdf:resource="http://www.w3.org/2006/vcard/ns#Agent"/>
                                        <rdf:rest rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"/>
                                      </rdf:Description>
                                    </rdf:rest>
                                  </rdf:Description>
                                </rdf:rest>
                              </rdf:Description>
                            </rdf:rest>
                          </rdf:Description>
                        </rdf:rest>
                      </rdf:Description>
                    </rdf:rest>
                  </rdf:Description>
                </rdf:rest>
              </rdf:Description>
            </rdf:rest>
          </rdf:Description>
        </owl:unionOf>
      </owl:Class>
    </rdfs:subClassOf>
    <skos:definition xml:lang="en">An entity or a collection of entities that undertake Roles in a Rule.</skos:definition>
    <skos:note xml:lang="en">The Party entity could be a person, group of people, organisation, or agent. An agent is a person or thing that takes an active role or produces a specified effect. To describe more details about the Party, it is recommended to use W3C vCard Ontology [[vcard-rdf]] or FOAF Vocabulary [[foaf]].</skos:note>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/PartyCollection">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Party Collection</rdfs:label>
    <rdfs:subClassOf rdf:resource="http://www.w3.org/ns/odrl/2/Party"/>
    <skos:definition xml:lang="en">A Party that is a group of individual entities</skos:definition>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/PartyScope">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Party Scope</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">Scopes for Party Scope expressions.</skos:definition>
    <skos:note xml:lang="en">Instances of the PartyScope class represent the terms for the scope property of Parties.</skos:note>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/Permission">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Permission</rdfs:label>
    <rdfs:subClassOf rdf:resource="http://www.w3.org/ns/odrl/2/Rule"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Duty"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Prohibition"/>
    <skos:definition xml:lang="en">The ability to perform an Action over an Asset.</skos:definition>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/Policy">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Policy</rdfs:label>
    <skos:definition xml:lang="en">A non-empty group of Permissions and/or Prohibitions.</skos:definition>
    <skos:note xml:lang="en">A Policy may contain multiple Rules.</skos:note>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/Privacy">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Privacy Policy</rdfs:label>
    <rdfs:subClassOf rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Agreement"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Assertion"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Offer"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Request"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Ticket"/>
    <skos:definition xml:lang="en">A Policy that expresses a Rule over an Asset containing personal information.</skos:definition>
    <skos:note xml:lang="en">A Privacy Policy  MUST contain a target Asset, a Party with Assigner  is, a Party with Assignee function, and at least one of a Permission or Prohibition rule that MUST include a Duty. The target Asset SHOULD contain or relate to personal information about the Assignee. The Duty MUST describe obligations on the Assigner about managing the Asset. The Assignee is being granted the terms of the Privacy policy from the Assigner.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/Prohibition">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Prohibition</rdfs:label>
    <rdfs:subClassOf rdf:resource="http://www.w3.org/ns/odrl/2/Rule"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Duty"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Permission"/>
    <skos:definition xml:lang="en">The inability to perform an Action over an Asset.</skos:definition>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/Request">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Request</rdfs:label>
    <rdfs:subClassOf rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Agreement"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Assertion"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Offer"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Privacy"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Ticket"/>
    <skos:definition xml:lang="en">A Policy that proposes a Rule over an Asset from an assignee.</skos:definition>
    <skos:note xml:lang="en">A Request Policy  MUST contain a target Asset, a Party with Assignee function, and at least one of a Permission or Prohibition rule. The Request MAY also contain the Party with Assigner function if this is known. No privileges are granted to any Party.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/RightOperand">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Right Operand</rdfs:label>
    <skos:definition xml:lang="en">Right operand for constraint expression.</skos:definition>
    <skos:note xml:lang="en">Instances of the RightOperand class are used as the rightOperand of a Constraint.</skos:note>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/Rule">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Rule</rdfs:label>
    <skos:definition xml:lang="en">An abstract concept that represents the common characteristics of Permissions, Prohibitions, and Duties.</skos:definition>
    <skos:note xml:lang="en">Rule is an abstract concept.</skos:note>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/Set">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Set</rdfs:label>
    <rdfs:subClassOf rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Agreement"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Assertion"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Offer"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Privacy"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Request"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Ticket"/>
    <skos:definition xml:lang="en">A Policy that expresses a Rule over an Asset.</skos:definition>
    <skos:note xml:lang="en">A Set Policy MUST contain a target Asset, and at least one Rule. A Set Policy is the default Policy subclass. The Set is aimed at scenarios where there is an open criteria for the semantics of the policy expressions and typically refined by other systems/profiles that process the information at a later time. No privileges are granted to any Party (if defined).</skos:note>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/Ticket">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Ticket</rdfs:label>
    <rdfs:subClassOf rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Agreement"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Assertion"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Offer"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Privacy"/>
    <owl:disjointWith rdf:resource="http://www.w3.org/ns/odrl/2/Request"/>
    <skos:definition xml:lang="en">A Policy that grants the holder a Rule over an Asset from an assigner.</skos:definition>
    <skos:note xml:lang="en">A Ticket Policy MUST contain a target Asset and at least one of a Permission or Prohibition rule.  The Ticket MAY contain the Party with Assigner function and MUST NOT contain an Assignee. The Ticket Policy will grant the terms of the Policy to the holder of that Ticket. The holder of the Ticket MAY remain unknown or MAY have to be identified at some later stage.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </rdfs:Class>
  <rdfs:Class rdf:about="http://www.w3.org/ns/odrl/2/UndefinedTerm">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Undefined Term</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">Is used to indicate how to support Actions that are not part of any vocabulary or profile in the policy expression system.</skos:definition>
    <skos:note xml:lang="en">Instances of UndefinedTerm describe strategies for processing unsupported actions.</skos:note>
  </rdfs:Class>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/absolutePosition">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Absolute Asset Position</rdfs:label>
    <skos:definition xml:lang="en">A point in space or time defined with absolute coordinates for the positioning of the target Asset.</skos:definition>
    <skos:note xml:lang="en">Example: The upper left corner of a picture may be constrained to a specific position of the canvas rendering it.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/absoluteSize">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Absolute Asset Size</rdfs:label>
    <skos:definition xml:lang="en">Measure(s) of one or two axes for 2D-objects or measure(s) of one to tree axes for 3D-objects of the target Asset.</skos:definition>
    <skos:note xml:lang="en">Example: The image can be resized in width to a maximum of 1000px.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/absoluteSpatialPosition">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Absolute Spatial Asset Position</rdfs:label>
    <skos:broaderTransitive rdf:resource="http://www.w3.org/ns/odrl/2/absolutePosition"/>
    <skos:definition xml:lang="en">The absolute spatial positions of four corners of a rectangle on a 2D-canvas or the eight corners of a cuboid in a 3D-space for the target Asset to fit.</skos:definition>
    <skos:note xml:lang="en">Example: The upper left corner of a picture may be constrained to a specific position of the canvas rendering it. Note: see also the Left Operand Relative Spatial Asset Position. </skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/absoluteTemporalPosition">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Absolute Temporal Asset Position</rdfs:label>
    <skos:broaderTransitive rdf:resource="http://www.w3.org/ns/odrl/2/absolutePosition"/>
    <skos:definition xml:lang="en">The absolute temporal positions in a media stream the target Asset has to fit.</skos:definition>
    <skos:note xml:lang="en">Use with Actions including the target Asset in a larger media stream. The fragment part of a Media Fragment URI (https://www.w3.org/TR/media-frags/) may be used for the right operand. See the Left Operand realativeTemporalPosition. &lt;br /&gt;Example: The MP3 music file must be positioned between second 192 and 250 of the temporal length of a stream.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/acceptTracking">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Accept Tracking</rdfs:label>
    <skos:definition xml:lang="en">To accept that the use of the Asset may be tracked.</skos:definition>
    <skos:note xml:lang="en">The collected information may be tracked by the Assigner, or may link to a Party with the role 'trackingParty' function.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/action">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain>
      <owl:Class>
        <owl:unionOf>
          <rdf:Description>
            <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Rule"/>
            <rdf:rest>
              <rdf:Description>
                <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
                <rdf:rest rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"/>
              </rdf:Description>
            </rdf:rest>
          </rdf:Description>
        </owl:unionOf>
      </owl:Class>
    </rdfs:domain>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Has Action</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Action"/>
    <skos:definition xml:lang="en">The operation relating to the Asset for which the Rule is being subjected.</skos:definition>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/adHocShare">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Ad-hoc sharing</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of sharing the asset to parties in close proximity to the owner.</skos:definition>
    <skos:note xml:lang="en">This original term and URI from the OMA specification should be used: http://www.openmobilealliance.com/oma-dd/adhoc-share .</skos:note>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/aggregate">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Aggregate</rdfs:label>
    <skos:definition xml:lang="en">To use the Asset or parts of it as part of a composite collection.</skos:definition>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/and">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">And</rdfs:label>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/operand"/>
    <skos:definition xml:lang="en">The relation is satisfied when all of the Constraints are satisfied.</skos:definition>
    <skos:note xml:lang="en">This property MUST only be used for Logical Constraints, and the list of operand values MUST be Constraint instances.</skos:note>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/andSequence">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">And Sequence</rdfs:label>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/operand"/>
    <skos:definition xml:lang="en">The relation is satisfied when each of the Constraints are satisfied in the order specified.</skos:definition>
    <skos:note xml:lang="en">This property MUST only be used for Logical Constraints, and the list of operand values MUST be Constraint instances. The order of the list MUST be preserved. The andSequence operator is an example where there may be temporal conditional requirements between the operands. This may lead to situations where the outcome is unresolvable, such as deadlock if one of the Constraints is unable to be satisfied. ODRL Processing systems SHOULD plan for these scenarios and implement mechanisms to resolve them.</skos:note>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/annotate">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Annotate</rdfs:label>
    <skos:definition xml:lang="en">To add explanatory notations/commentaries to the Asset without modifying the Asset in any other way.</skos:definition>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/anonymize">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Anonymize</rdfs:label>
    <skos:definition xml:lang="en">To anonymize all or parts of the Asset.</skos:definition>
    <skos:note xml:lang="en">For example, to remove identifying particulars for statistical or for other comparable purposes, or to use the Asset without stating the author/source.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/append">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Append</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of adding to the end of an asset.</skos:definition>
    <skos:exactMatch rdf:resource="http://www.w3.org/ns/odrl/2/modify"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/appendTo">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Append To</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of appending data to the Asset without modifying the Asset in any other way.</skos:definition>
    <skos:exactMatch rdf:resource="http://www.w3.org/ns/odrl/2/modify"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/archive">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Archive</rdfs:label>
    <skos:definition xml:lang="en">To store the Asset (in a non-transient form).</skos:definition>
    <skos:note xml:lang="en">Temporal constraints may be used for temporal conditions.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/assignee">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain>
      <owl:Class>
        <owl:unionOf>
          <rdf:Description>
            <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Rule"/>
            <rdf:rest>
              <rdf:Description>
                <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
                <rdf:rest rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"/>
              </rdf:Description>
            </rdf:rest>
          </rdf:Description>
        </owl:unionOf>
      </owl:Class>
    </rdfs:domain>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Assignee</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Party"/>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/function"/>
    <skos:definition xml:lang="en">The Party is the recipient of the Rule.</skos:definition>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/assigneeOf">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Party"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Assignee Of</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
    <skos:definition xml:lang="en">Identifies an ODRL Policy for which the identified Party undertakes the assignee functional role.</skos:definition>
    <skos:note xml:lang="en">When assigneeOf has been asserted between a metadata expression and an ODRL Policy, the Party being identified MUST be inferred to undertake the assignee functional role of all the Rules of that Policy.</skos:note>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/assigner">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain>
      <owl:Class>
        <owl:unionOf>
          <rdf:Description>
            <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Rule"/>
            <rdf:rest>
              <rdf:Description>
                <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
                <rdf:rest rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"/>
              </rdf:Description>
            </rdf:rest>
          </rdf:Description>
        </owl:unionOf>
      </owl:Class>
    </rdfs:domain>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Assigner</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Party"/>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/function"/>
    <skos:definition xml:lang="en">The Party is the issuer of the Rule.</skos:definition>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/assignerOf">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Party"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Assigner Of</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
    <skos:definition xml:lang="en">Identifies an ODRL Policy for which the identified Party undertakes the assigner functional role.</skos:definition>
    <skos:note xml:lang="en">When assignerOf has been asserted between a metadata expression and an ODRL Policy, the Party being identified MUST be inferred to undertake the assigner functional role of all the Rules of that Policy.</skos:note>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/attachPolicy">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Attach policy</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of keeping the policy notice with the asset.</skos:definition>
    <skos:exactMatch rdf:resource="http://creativecommons.org/ns#Notice"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/attachSource">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Attach source</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of attaching the source of the asset and its derivatives.</skos:definition>
    <skos:exactMatch rdf:resource="http://creativecommons.org/ns#SourceCode"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/attribute">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Attribute</rdfs:label>
    <skos:definition xml:lang="en">To attribute the use of the Asset.</skos:definition>
    <skos:note xml:lang="en">May link to an Asset with the attribution information. May link to a Party with the  role “attributedParty” function.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/attributedParty">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Attributed Party</rdfs:label>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/function"/>
    <skos:definition xml:lang="en">The Party to be attributed.</skos:definition>
    <skos:note xml:lang="en">Maybe specified as part of the attribute action.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/attributingParty">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Attributing Party</rdfs:label>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/function"/>
    <skos:definition xml:lang="en">The Party who undertakes the attribution.</skos:definition>
    <skos:note xml:lang="en">Maybe specified as part of the attribute action.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/commercialize">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Commercialize</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of using the asset in a business environment.</skos:definition>
    <skos:exactMatch rdf:resource="http://creativecommons.org/ns#CommercialUse"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/compensate">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Compensate</rdfs:label>
    <skos:definition xml:lang="en">To compensate by transfer of some amount of value, if defined, for using or selling the Asset.</skos:definition>
    <skos:note xml:lang="en">The compensation may use different types of things with a value: (i) the thing is expressed by the value (term) of the Constraint name; (b) the value is expressed by operator, rightOperand, dataType and unit. Typically the assignee will compensate the assigner, but other compensation party roles may be used.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/compensatedParty">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Compensated Party</rdfs:label>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/function"/>
    <skos:definition xml:lang="en">The Party is the recipient of the compensation.</skos:definition>
    <skos:note xml:lang="en">Maybe specified as part of the compensate duty action.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/compensatingParty">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Compensating Party</rdfs:label>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/function"/>
    <skos:definition xml:lang="en">The Party that is the provider of the compensation.</skos:definition>
    <skos:note xml:lang="en">Maybe specified as part of the compensate duty action.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/concurrentUse">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Concurrent Use</rdfs:label>
    <skos:definition xml:lang="en">To create multiple copies of the Asset that are being concurrently used.</skos:definition>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/conflict">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Handle Policy Conflicts</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/ConflictTerm"/>
    <skos:definition xml:lang="en">The conflict-resolution strategy for a Policy.</skos:definition>
    <skos:note xml:lang="en">If no strategy is specified, the default is invalid.</skos:note>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/consentedParty">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Consented Party</rdfs:label>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/function"/>
    <skos:definition xml:lang="en">The Party who obtains the consent.</skos:definition>
    <skos:note xml:lang="en">Maybe specified as part of the obtainConsent action.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/consentingParty">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Consenting Party</rdfs:label>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/function"/>
    <skos:definition xml:lang="en">The Party to obtain consent from.</skos:definition>
    <skos:note xml:lang="en">Maybe specified as part of the obtainConsent action.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/consequence">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Duty"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Consequence</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Duty"/>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/failure"/>
    <skos:definition xml:lang="en">Relates a Duty to another Duty, the latter being a consequence of not fulfilling the former.</skos:definition>
    <skos:note xml:lang="en">The consequence property is utilised to express the repercussions of not fulfilling an agreed Policy obligation or duty for a Permission. If either of these fails to be fulfilled, then this will result in the consequence Duty also becoming a new requirement, meaning that the original obligation or duty, as well as the consequence Duty must all be fulfilled</skos:note>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/constraint">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain>
      <owl:Class>
        <owl:unionOf>
          <rdf:Description>
            <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
            <rdf:rest>
              <rdf:Description>
                <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Rule"/>
                <rdf:rest rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"/>
              </rdf:Description>
            </rdf:rest>
          </rdf:Description>
        </owl:unionOf>
      </owl:Class>
    </rdfs:domain>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Has Constraint</rdfs:label>
    <rdfs:range>
      <owl:Class>
        <owl:unionOf>
          <rdf:Description>
            <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Constraint"/>
            <rdf:rest>
              <rdf:Description>
                <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/LogicalConstraint"/>
                <rdf:rest rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"/>
              </rdf:Description>
            </rdf:rest>
          </rdf:Description>
        </owl:unionOf>
      </owl:Class>
    </rdfs:range>
    <skos:definition xml:lang="en">Constraint applied to a Rule</skos:definition>
    <skos:note xml:lang="en">Constraints on Rules are used to determine if a rule is Active or not. Example: the Permission rule is only active during the year 2018.</skos:note>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/contractedParty">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Contracted Party</rdfs:label>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/function"/>
    <skos:definition xml:lang="en">The Party who is being contracted.</skos:definition>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/contractingParty">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Contracting Party</rdfs:label>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/function"/>
    <skos:definition xml:lang="en">The Party who is offering the contract.</skos:definition>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/copy">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Copy</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <owl:sameAs rdf:resource="http://www.w3.org/ns/odrl/2/reproduce"/>
    <skos:definition xml:lang="en">The act of making an exact reproduction of the asset.</skos:definition>
    <skos:exactMatch rdf:resource="http://www.w3.org/ns/odrl/2/reproduce"/>
  </Action>
  <owl:Thing rdf:about="http://www.w3.org/ns/odrl/2/core">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">ODRL Core Profile</rdfs:label>
    <skos:definition xml:lang="en">Identifier for the ODRL Core Profile</skos:definition>
  </owl:Thing>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/count">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Count</rdfs:label>
    <skos:definition xml:lang="en">Numeric count of executions of the action of the Rule.</skos:definition>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/dataType">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Constraint"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Datatype</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/2000/01/rdf-schema#Datatype"/>
    <skos:definition xml:lang="en">The datatype of the value of the rightOperand or rightOperandReference of a Constraint.</skos:definition>
    <skos:note xml:lang="en">In RDF encodings, use of the rdf:datatype MUST be used. In JSON-LD encoding, the use of @type MUST be used.</skos:note>
  </rdf:Property>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/dateTime">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Datetime</rdfs:label>
    <skos:definition xml:lang="en">The date (and optional time and timezone) of exercising the action of the Rule. Right operand value MUST be an xsd:date or xsd:dateTime as defined by [[xmlschema11-2]].</skos:definition>
    <skos:note xml:lang="en">The use of Timezone information is strongly recommended. The Rule may be exercised before (with operator lt/lteq) or after (with operator gt/gteq) the date(time) defined by the Right operand. &lt;br /&gt;Example: &lt;code&gt;dateTime gteq 2017-12-31T06:00Z&lt;/code&gt; means the Rule can only be exercised after (and including) 6:00AM on the 31st Decemeber 2017 UTC time.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/delayPeriod">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Delay Period</rdfs:label>
    <skos:definition xml:lang="en">A time delay period prior to exercising the action of the Rule. The point in time triggering this period MAY be defined by another temporal Constraint combined by a Logical Constraint (utilising the odrl:andSequence operand). Right operand value MUST be an xsd:duration as defined by [[xmlschema11-2]].</skos:definition>
    <skos:note xml:lang="en">Only the eq, gt, gteq operators SHOULD be used. &lt;br /&gt;Example: &lt;code&gt;delayPeriod eq P60M&lt;/code&gt; indicates a delay of 60 Minutes before exercising the action.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/delete">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Delete</rdfs:label>
    <skos:definition xml:lang="en">To permanently remove all copies of the Asset after it has been used.</skos:definition>
    <skos:note xml:lang="en">Use a constraint to define under which conditions the Asset must be deleted.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/deliveryChannel">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Delivery Channel</rdfs:label>
    <skos:definition xml:lang="en">The delivery channel used for exercising the action of the Rule.</skos:definition>
    <skos:note xml:lang="en">Example: the asset may be distributed only on mobile networks.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/derive">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Derive</rdfs:label>
    <skos:definition xml:lang="en">To create a new derivative Asset from this Asset and to edit or modify the derivative.</skos:definition>
    <skos:note xml:lang="en">A new asset is created and may have significant overlaps with the original Asset. (Note that the notion of whether or not the change is significant enough to qualify as a new asset is subjective). To the derived Asset a next policy may be applied.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/device">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Device</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">An identified device used for exercising the action of the Rule.</skos:definition>
    <skos:exactMatch rdf:resource="http://www.w3.org/ns/odrl/2/systemDevice"/>
    <skos:note>See System Device.</skos:note>
  </LeftOperand>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/digitize">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Digitize</rdfs:label>
    <skos:definition xml:lang="en">To produce a digital copy of (or otherwise digitize) the Asset from its analogue form.</skos:definition>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/display">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Display</rdfs:label>
    <skos:definition xml:lang="en">To create a static and transient rendition of an Asset.</skos:definition>
    <skos:note xml:lang="en">For example, displaying an image on a screen. If the action is to be performed to a wider audience than just the Assignees, then the Recipient constraint is recommended to be used.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/play"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/distribute">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Distribute</rdfs:label>
    <skos:definition xml:lang="en">To supply the Asset to third-parties.</skos:definition>
    <skos:note xml:lang="en">It is recommended to use nextPolicy to express the allowable usages by third-parties.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/duty">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Permission"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Has Duty</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Duty"/>
    <skos:definition xml:lang="en">Relates an individual Duty to a Permission.</skos:definition>
    <skos:note xml:lang="en">A Duty is a pre-condition which must be fulfilled in order to receive the Permission.</skos:note>
  </rdf:Property>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/elapsedTime">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Elapsed Time</rdfs:label>
    <skos:definition xml:lang="en">A continuous elapsed time period which may be used for exercising of the action of the Rule. Right operand value MUST be an xsd:duration as defined by [[xmlschema11-2]].</skos:definition>
    <skos:note>Only the eq, lt, lteq operators SHOULD be used. See also Metered Time. &lt;br /&gt;Example: &lt;code&gt;elpasedTime eq P60M&lt;/code&gt; indicates a total elapsed time of 60 Minutes.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/ensureExclusivity">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Ensure Exclusivity</rdfs:label>
    <skos:definition xml:lang="en">To ensure that the Rule on the Asset is exclusive.</skos:definition>
    <skos:note xml:lang="en">If used as a Duty, the assignee should be explicitly indicated as the party that is ensuring the exclusivity of the Rule.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Operator rdf:about="http://www.w3.org/ns/odrl/2/eq">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Equal to</rdfs:label>
    <skos:definition xml:lang="en">Indicating that a given value equals the right operand of the Constraint.</skos:definition>
  </Operator>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/event">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Event</rdfs:label>
    <skos:definition xml:lang="en">An identified event setting a context for exercising the action of the Rule.</skos:definition>
    <skos:note xml:lang="en">Events are temporal periods of time, and operators can be used to signal before (lt), during (eq) or after (gt) the event. &lt;br /&gt;Example: May be taken during the “FIFA World Cup 2020” only.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/execute">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Execute</rdfs:label>
    <skos:definition xml:lang="en">To run the computer program Asset.</skos:definition>
    <skos:note xml:lang="en">For example, machine executable code or Java such as a game or application.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/export">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Export</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of transforming the asset into a new form.</skos:definition>
    <skos:exactMatch rdf:resource="http://www.w3.org/ns/odrl/2/transform"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/extract">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Extract</rdfs:label>
    <skos:definition xml:lang="en">To extract parts of the Asset and to use it as a new Asset.</skos:definition>
    <skos:note xml:lang="en">A new asset is created and may have very little in common with the original Asset. (Note that the notion of whether or not the change is significant enough to qualify as a new asset is subjective). To the extracted Asset a next policy may be applied.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/reproduce"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/extractChar">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Extract character</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of extracting (replicating) unchanged characters from the asset.</skos:definition>
    <skos:note xml:lang="en">This original term and URI from the ONIX specification should be used: http://www.editeur.org/onix-pl/extract-char .</skos:note>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/extractPage">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Extract page</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of extracting (replicating) unchanged pages from the asset.</skos:definition>
    <skos:note xml:lang="en">This original term and URI from the ONIX specification should be used: http://www.editeur.org/onix-pl/extract-page .</skos:note>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/extractWord">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Extract word</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of extracting (replicating) unchanged words from the asset.</skos:definition>
    <skos:note xml:lang="en">This original term and URI from the ONIX specification should be used: http://www.editeur.org/onix-pl/extract-word .</skos:note>
  </Action>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/failure">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Rule"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Failure</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Rule"/>
    <skos:definition xml:lang="en">Failure is an abstract property that defines the violation (or unmet) relationship between Rules.</skos:definition>
    <skos:note xml:lang="en">The parent property to sub-properties that express explicit failure contexts.</skos:note>
  </rdf:Property>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/fileFormat">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">File Format</rdfs:label>
    <skos:definition xml:lang="en">A transformed file format of the target Asset.</skos:definition>
    <skos:note xml:lang="en">Example: An asset may be transformed into JPEG format.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/function">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain>
      <owl:Class>
        <owl:unionOf>
          <rdf:Description>
            <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Rule"/>
            <rdf:rest>
              <rdf:Description>
                <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
                <rdf:rest rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"/>
              </rdf:Description>
            </rdf:rest>
          </rdf:Description>
        </owl:unionOf>
      </owl:Class>
    </rdfs:domain>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Function</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Party"/>
    <skos:definition xml:lang="en">Function is an abstract property whose sub-properties define the functional roles which may be fulfilled by a party in relation to a Rule.</skos:definition>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/give">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Give</rdfs:label>
    <skos:definition xml:lang="en">To transfer the ownership of the Asset to a third party without compensation and while deleting the original asset.</skos:definition>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/transfer"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/grantUse">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Grant Use</rdfs:label>
    <skos:definition xml:lang="en">To grant the use of the Asset to third parties.</skos:definition>
    <skos:note xml:lang="en">This action enables the assignee to create policies for the use of the Asset for third parties. The nextPolicy is recommended to be agreed with the third party. Use of temporal constraints is recommended.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Operator rdf:about="http://www.w3.org/ns/odrl/2/gt">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Greater than</rdfs:label>
    <skos:definition xml:lang="en">Indicating that a given value is greater than the right operand of the Constraint.</skos:definition>
  </Operator>
  <Operator rdf:about="http://www.w3.org/ns/odrl/2/gteq">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Greater than or equal to</rdfs:label>
    <skos:definition xml:lang="en">Indicating that a given value is greater than or equal to the right operand of the Constraint.</skos:definition>
  </Operator>
  <Operator rdf:about="http://www.w3.org/ns/odrl/2/hasPart">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Has part</rdfs:label>
    <skos:definition xml:lang="en">A set-based operator indicating that a given value contains the right operand of the Constraint.</skos:definition>
  </Operator>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/hasPolicy">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Asset"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Target Policy</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
    <skos:definition xml:lang="en">Identifies an ODRL Policy for which the identified Asset is the target Asset to all the Rules.</skos:definition>
    <skos:note xml:lang="en">The Asset being identified MUST be inferred to be the target Asset of all of the Rules of the Policy.</skos:note>
  </rdf:Property>
  <UndefinedTerm rdf:about="http://www.w3.org/ns/odrl/2/ignore">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Ignore Undefined Actions</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The Action is to be ignored and is not part of the policy – and the policy remains valid.</skos:definition>
    <skos:note xml:lang="en">Used to support actions not known to the policy system.</skos:note>
  </UndefinedTerm>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/implies">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Action"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Implies</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Action"/>
    <skos:definition xml:lang="en">An Action asserts that another Action is not prohibited to enable its operational semantics.</skos:definition>
    <skos:note xml:lang="en">The property asserts that an instance of Action entails that the other instance of Action is not prohibited.</skos:note>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/include">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Include</rdfs:label>
    <skos:definition xml:lang="en">To include other related assets in the Asset.</skos:definition>
    <skos:note xml:lang="en">For example: bio picture must be included in the attribution. Use of a relation sub-property is required for the related assets.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/includedIn">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#TransitiveProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Action"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Included In</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Action"/>
    <skos:definition xml:lang="en">An Action transitively asserts that another Action that encompasses its operational semantics.</skos:definition>
    <skos:note xml:lang="en">The purpose is to explicitly assert that the semantics of the referenced instance of an other Action encompasses (includes) the semantics of this instance of Action. The includedIn property is transitive, and as such, the Actions form ancestor relationships.</skos:note>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/index">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Index</rdfs:label>
    <skos:definition xml:lang="en">To record the Asset in an index.</skos:definition>
    <skos:note xml:lang="en">For example, to include a link to the Asset in a search engine database.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/industry">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Industry Context</rdfs:label>
    <skos:definition xml:lang="en">A defined industry sector setting a context for exercising the action of the Rule.</skos:definition>
    <skos:note xml:lang="en">Example: publishing or financial industry.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/inform">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Inform</rdfs:label>
    <skos:definition xml:lang="en">To inform that an action has been performed on or in relation to the Asset.</skos:definition>
    <skos:note xml:lang="en">May link to a Party with the role 'informedParty' function.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/informedParty">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Informed Party</rdfs:label>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/function"/>
    <skos:definition xml:lang="en">The Party to be informed of all uses.</skos:definition>
    <skos:note xml:lang="en">Maybe specified as part of the inform action.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/informingParty">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Informing Party</rdfs:label>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/function"/>
    <skos:definition xml:lang="en">The Party who provides the inform use data.</skos:definition>
    <skos:note xml:lang="en">Maybe specified as part of the inform action.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/inheritAllowed">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#DatatypeProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Inheritance Allowed</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">Indicates if the Policy entity can be inherited.</skos:definition>
    <skos:note xml:lang="en">A boolean value.</skos:note>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/inheritFrom">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Inherits From</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
    <skos:definition xml:lang="en">Relates a (child) policy to another (parent) policy from which terms are inherited.</skos:definition>
    <skos:note xml:lang="en">The child policy will inherit Rules from the parent policy</skos:note>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/inheritRelation">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Inherit Relation</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">Indentifies the type of inheritance.</skos:definition>
    <skos:note xml:lang="en">For example, this may indicate the business scenario, such as subscription, or prior arrangements between the parties (that are not machine representable).</skos:note>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/install">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Install</rdfs:label>
    <skos:definition xml:lang="en">To load the computer program Asset onto a storage device which allows operating or running the Asset.</skos:definition>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <ConflictTerm rdf:about="http://www.w3.org/ns/odrl/2/invalid">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Void Policy</rdfs:label>
    <skos:definition xml:lang="en">The policy is void.</skos:definition>
    <skos:note xml:lang="en">Used to indicate the policy is void for Conflict Strategy.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </ConflictTerm>
  <Operator rdf:about="http://www.w3.org/ns/odrl/2/isA">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Is a</rdfs:label>
    <skos:definition xml:lang="en">A set-based operator indicating that a given value is an instance of the right operand of the Constraint.</skos:definition>
  </Operator>
  <Operator rdf:about="http://www.w3.org/ns/odrl/2/isAllOf">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Is all of</rdfs:label>
    <skos:definition xml:lang="en">A set-based operator indicating that a given value is all of the right operand of the Constraint.</skos:definition>
  </Operator>
  <Operator rdf:about="http://www.w3.org/ns/odrl/2/isAnyOf">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Is any of</rdfs:label>
    <skos:definition xml:lang="en">A set-based operator indicating that a given value is any of the right operand of the Constraint.</skos:definition>
  </Operator>
  <Operator rdf:about="http://www.w3.org/ns/odrl/2/isNoneOf">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Is none of</rdfs:label>
    <skos:definition xml:lang="en">A set-based operator indicating that a given value is none of the right operand of the Constraint.</skos:definition>
  </Operator>
  <Operator rdf:about="http://www.w3.org/ns/odrl/2/isPartOf">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Is part of</rdfs:label>
    <skos:definition xml:lang="en">A set-based operator indicating that a given value is contained by the right operand of the Constraint.</skos:definition>
  </Operator>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/language">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Language</rdfs:label>
    <skos:definition xml:lang="en">A natural language used by the target Asset.</skos:definition>
    <skos:note xml:lang="en">Example: the asset can only be translated into Greek. Must use [[bcp47]] codes for language values.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/lease">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Lease</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of making available the asset to a third-party for a fixed period of time with exchange of value.</skos:definition>
  </Action>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/leftOperand">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Constraint"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Has Left Operand</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/LeftOperand"/>
    <skos:definition xml:lang="en">The left operand in a constraint expression.</skos:definition>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/lend">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Lend</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of making available the asset to a third-party for a fixed period of time without exchange of value.</skos:definition>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/license">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">License</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of granting the right to use the asset to a third-party.</skos:definition>
    <skos:exactMatch rdf:resource="http://www.w3.org/ns/odrl/2/grantUse"/>
  </Action>
  <Operator rdf:about="http://www.w3.org/ns/odrl/2/lt">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Less than</rdfs:label>
    <skos:definition xml:lang="en">Indicating that a given value is less than the right operand of the Constraint.</skos:definition>
  </Operator>
  <Operator rdf:about="http://www.w3.org/ns/odrl/2/lteq">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Less than or equal to</rdfs:label>
    <skos:definition xml:lang="en">Indicating that a given value is less than or equal to the right operand of the Constraint.</skos:definition>
  </Operator>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/media">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Media Context</rdfs:label>
    <skos:definition xml:lang="en">Category of a media asset setting a context for exercising the action of the Rule.</skos:definition>
    <skos:note xml:lang="en">Example media types: electronic, print, advertising, marketing. Note: The used type should not be an IANA MediaType as they are focused on technical characteristics. </skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/meteredTime">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Metered Time</rdfs:label>
    <skos:definition xml:lang="en">An accumulated amount of one to many metered time periods which were used for exercising the action of the Rule. Right operand value MUST be an xsd:duration as defined by [[xmlschema11-2]].</skos:definition>
    <skos:note>Only the eq, lt, lteq operators SHOULD be used. See also Elapsed Time. &lt;br /&gt;Example: &lt;code&gt;meteredTime lteq P60M&lt;/code&gt; indicates an accumulated period of 60 Minutes or less.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/modify">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Modify</rdfs:label>
    <skos:definition xml:lang="en">To change existing content of the Asset. A new asset is not created by this action.</skos:definition>
    <skos:note xml:lang="en">This action will modify an asset which is typically updated from time to time without creating a new asset. If the result from modifying the asset should be a new asset the actions derive or extract should be used. (Note that the notion of whether or not the change is significant enough to qualify as a new asset is subjective).</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/move">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Move</rdfs:label>
    <skos:definition xml:lang="en">To move the Asset from one digital location to another including deleting the original copy.</skos:definition>
    <skos:note xml:lang="en">After the Asset has been moved, the original copy must be deleted.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Operator rdf:about="http://www.w3.org/ns/odrl/2/neq">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Not equal to</rdfs:label>
    <skos:definition xml:lang="en">Indicating that a given value is not equal to the right operand of the Constraint.</skos:definition>
  </Operator>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/nextPolicy">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Next Policy</rdfs:label>
    <skos:definition xml:lang="en">To grant the specified Policy to a third party for their use of the Asset.</skos:definition>
    <skos:note xml:lang="en">Useful for downstream policies.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/obligation">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Obligation</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Duty"/>
    <skos:definition xml:lang="en">Relates an individual Duty to a Policy.</skos:definition>
    <skos:note xml:lang="en">The Duty is a requirement which must be fulfilled.</skos:note>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/obtainConsent">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Obtain Consent</rdfs:label>
    <skos:definition xml:lang="en">To obtain verifiable consent to perform the requested action in relation to the Asset.</skos:definition>
    <skos:note xml:lang="en">May be used as a Duty to ensure that the Assigner or a Party is authorized to approve such actions on a case-by-case basis. May link to a Party with the role “consentingParty” function.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/operand">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/LogicalConstraint"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Operand</rdfs:label>
    <skos:definition xml:lang="en">Operand is an abstract property for a logical relationship.</skos:definition>
    <skos:note xml:lang="en">Sub-properties of operand are used for Logical Constraints.</skos:note>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/operator">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Constraint"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Has Operator</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Operator"/>
    <skos:definition xml:lang="en">The operator function applied to operands of a Constraint</skos:definition>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/or">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Or</rdfs:label>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/operand"/>
    <skos:definition xml:lang="en">The relation is satisfied when at least one of the Constraints is satisfied.</skos:definition>
    <skos:note xml:lang="en">This property MUST only be used for Logical Constraints, and the list of operand values MUST be Constraint instances.</skos:note>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/output">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Rule"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Output</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Asset"/>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/relation"/>
    <skos:definition xml:lang="en">The output property specifies the Asset which is created from the output of the Action.</skos:definition>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/partOf">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain>
      <owl:Class>
        <owl:unionOf>
          <rdf:Description>
            <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Asset"/>
            <rdf:rest>
              <rdf:Description>
                <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Party"/>
                <rdf:rest rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"/>
              </rdf:Description>
            </rdf:rest>
          </rdf:Description>
        </owl:unionOf>
      </owl:Class>
    </rdfs:domain>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Part Of</rdfs:label>
    <rdfs:range>
      <owl:Class>
        <owl:unionOf>
          <rdf:Description>
            <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/AssetCollection"/>
            <rdf:rest>
              <rdf:Description>
                <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/PartyCollection"/>
                <rdf:rest rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"/>
              </rdf:Description>
            </rdf:rest>
          </rdf:Description>
        </owl:unionOf>
      </owl:Class>
    </rdfs:range>
    <skos:definition xml:lang="en">Identifies an Asset/PartyCollection that the Asset/Party is a member of.</skos:definition>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/pay">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Pay</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of paying a financial amount to a party for use of the asset.</skos:definition>
    <skos:exactMatch rdf:resource="http://www.w3.org/ns/odrl/2/compensate"/>
  </Action>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/payAmount">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Payment Amount</rdfs:label>
    <skos:definition xml:lang="en">The amount of a financial payment. Right operand value MUST be an xsd:decimal. </skos:definition>
    <skos:note xml:lang="en">Can be used for compensation duties with the unit property indicating the currency of the payment.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/payeeParty">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Payee Party</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The Party is the recipient of the payment.</skos:definition>
    <skos:exactMatch rdf:resource="http://www.w3.org/ns/odrl/2/compensatedParty"/>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </rdf:Property>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/percentage">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Asset Percentage</rdfs:label>
    <skos:definition xml:lang="en">A percentage amount of the target Asset relevant for exercising the action of the Rule. Right operand value MUST be an xsd:decimal from 0 to 100.</skos:definition>
    <skos:note xml:lang="en">Example: Extract less than or equal to 50%.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <ConflictTerm rdf:about="http://www.w3.org/ns/odrl/2/perm">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Prefer Permissions</rdfs:label>
    <skos:definition xml:lang="en">Permissions take preference over prohibitions.</skos:definition>
    <skos:note xml:lang="en">Used to determine policy conflict outcomes.</skos:note>
  </ConflictTerm>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/permission">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Has Permission</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Permission"/>
    <skos:definition xml:lang="en">Relates an individual Permission to a Policy.</skos:definition>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/play">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Play</rdfs:label>
    <skos:definition xml:lang="en">To create a sequential and transient rendition of an Asset.</skos:definition>
    <skos:note>For example, to play a video or audio track. If the action is to be performed to a wider audience than just the Assignees, then the Recipient constraint is recommended to be used.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <RightOperand rdf:about="http://www.w3.org/ns/odrl/2/policyUsage">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Policy Rule Usage</rdfs:label>
    <skos:definition xml:lang="en">Indicates the actual datetime the action of the Rule was exercised.</skos:definition>
    <skos:note xml:lang="en">This can be used to express constraints with a LeftOperand relative to the time the rule is exercised. Operators indicate before (lt, lteq), during (eq) or after (gt, gteq) the usage of the rule. &lt;br /&gt;Example: &lt;code&gt;event lt policyUsage&lt;/code&gt; expresses that the identified event must have happened before the action of the rule is exercised.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </RightOperand>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/present">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Present</rdfs:label>
    <skos:definition xml:lang="en">To publicly perform the Asset.</skos:definition>
    <skos:note>The asset can be performed (or communicated) in public.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/preview">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Preview</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of providing a short preview of the asset.</skos:definition>
    <skos:note xml:lang="en">Use a time constraint with the appropriate action.</skos:note>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/print">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Print</rdfs:label>
    <skos:definition xml:lang="en">To create a tangible and permanent rendition of an Asset.</skos:definition>
    <skos:note xml:lang="en">For example, creating a permanent, fixed (static), and directly perceivable representation of the Asset, such as printing onto paper.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/product">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Product Context</rdfs:label>
    <skos:definition xml:lang="en">Category of product or service setting a context for exercising the action of the Rule.</skos:definition>
    <skos:note xml:lang="en">Example: May only be used in the XYZ Magazine.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/profile">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Profile</rdfs:label>
    <skos:definition xml:lang="en">The identifier(s) of an ODRL Profile that the Policy conforms to.</skos:definition>
    <skos:note xml:lang="en">The profile property is mandatory if the Policy is using an ODRL Profile.</skos:note>
  </rdf:Property>
  <ConflictTerm rdf:about="http://www.w3.org/ns/odrl/2/prohibit">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Prefer Prohibitions</rdfs:label>
    <skos:definition xml:lang="en">Prohibitions take preference over permissions.</skos:definition>
    <skos:note xml:lang="en">Used to determine policy conflict outcomes.</skos:note>
  </ConflictTerm>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/prohibition">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Has Prohibition</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Prohibition"/>
    <skos:definition xml:lang="en">Relates an individual Prohibition to a Policy.</skos:definition>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/proximity">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#DatatypeProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">proximity</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">An value indicating the closeness or nearness.</skos:definition>
    <skos:note xml:lang="en">This original term and URI from the OMA specification should be used: http://www.openmobilealliance.com/oma-dd/proximity .</skos:note>
  </rdf:Property>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/purpose">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Purpose</rdfs:label>
    <skos:definition xml:lang="en">A defined purpose for exercising the action of the Rule.</skos:definition>
    <skos:note xml:lang="en">Example: Educational use.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/read">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Read</rdfs:label>
    <skos:definition xml:lang="en">To obtain data from the Asset.</skos:definition>
    <skos:note xml:lang="en">For example, the ability to read a record from a database (the Asset).</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/recipient">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Recipient</rdfs:label>
    <skos:definition xml:lang="en">The party receiving the result/outcome of exercising the action of the Rule.</skos:definition>
    <skos:note xml:lang="en">The Right Operand must identify one or more specific Parties or category/ies of the Party.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/refinement">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain>
      <owl:Class>
        <owl:unionOf>
          <rdf:Description>
            <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Action"/>
            <rdf:rest>
              <rdf:Description>
                <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/AssetCollection"/>
                <rdf:rest>
                  <rdf:Description>
                    <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/PartyCollection"/>
                    <rdf:rest rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"/>
                  </rdf:Description>
                </rdf:rest>
              </rdf:Description>
            </rdf:rest>
          </rdf:Description>
        </owl:unionOf>
      </owl:Class>
    </rdfs:domain>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Refinement</rdfs:label>
    <rdfs:range>
      <owl:Class>
        <owl:unionOf>
          <rdf:Description>
            <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Constraint"/>
            <rdf:rest>
              <rdf:Description>
                <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/LogicalConstraint"/>
                <rdf:rest rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"/>
              </rdf:Description>
            </rdf:rest>
          </rdf:Description>
        </owl:unionOf>
      </owl:Class>
    </rdfs:range>
    <skos:definition xml:lang="en">Constraint used to refine the semantics of an Action, or Party/Asset Collection</skos:definition>
    <skos:note xml:lang="en">Example: the Action print is only permitted on 50% of the asset.</skos:note>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/relation">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain>
      <owl:Class>
        <owl:unionOf>
          <rdf:Description>
            <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Rule"/>
            <rdf:rest>
              <rdf:Description>
                <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
                <rdf:rest rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"/>
              </rdf:Description>
            </rdf:rest>
          </rdf:Description>
        </owl:unionOf>
      </owl:Class>
    </rdfs:domain>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Relation</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Asset"/>
    <skos:definition xml:lang="en">Relation is an abstract property which creates an explicit link between an Action and an Asset.</skos:definition>
    <skos:note xml:lang="en">Sub-properties of relation are used to define the nature of that link.</skos:note>
  </rdf:Property>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/relativePosition">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Relative Asset Position</rdfs:label>
    <skos:definition xml:lang="en">A point in space or time defined with coordinates relative to full measures the positioning of the target Asset.</skos:definition>
    <skos:note xml:lang="en">Example: The upper left corner of a picture may be constrained to a specific position of the canvas rendering it.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/relativeSize">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Relative Asset Size</rdfs:label>
    <skos:definition xml:lang="en">Measure(s) of one or two axes for 2D-objects or measure(s) of one to tree axes for 3D-objects - expressed as percentages of full values - of the target Asset.</skos:definition>
    <skos:note xml:lang="en">Example: The image can be resized in width to a maximum of 200%. Note: See the Left Operand absoluteSize. </skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/relativeSpatialPosition">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Relative Spatial Asset Position</rdfs:label>
    <skos:broaderTransitive rdf:resource="http://www.w3.org/ns/odrl/2/relativePosition"/>
    <skos:definition xml:lang="en">The relative spatial positions - expressed as percentages of full values - of four corners of a rectangle on a 2D-canvas or the eight corners of a cuboid in a 3D-space of the target Asset.</skos:definition>
    <skos:note xml:lang="en">See also Absolute Spatial Asset Position.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/relativeTemporalPosition">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Relative Temporal Asset Position</rdfs:label>
    <skos:broaderTransitive rdf:resource="http://www.w3.org/ns/odrl/2/relativePosition"/>
    <skos:definition xml:lang="en">A point in space or time defined with coordinates relative to full measures the positioning of the target Asset.</skos:definition>
    <skos:note xml:lang="en">See also Absolute Temporal Asset Position. &lt;br /&gt;Example: The MP3 music file must be positioned between the positions at 33% and 48% of the temporal length of a stream. </skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/remedy">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Prohibition"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Remedy</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Duty"/>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/failure"/>
    <skos:definition xml:lang="en">Relates an individual remedy Duty to a Prohibition.</skos:definition>
    <skos:note xml:lang="en">The remedy property expresses an agreed Duty that must be fulfilled in case that a Prohibition has been violated by being exercised.</skos:note>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/reproduce">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Reproduce</rdfs:label>
    <skos:definition xml:lang="en">To make duplicate copies the Asset in any material form.</skos:definition>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/resolution">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Rendition Resolution</rdfs:label>
    <skos:definition xml:lang="en">Resolution of the rendition of the target Asset.</skos:definition>
    <skos:note xml:lang="en">Example: the image may be printed at 1200dpi.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/reviewPolicy">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Review Policy</rdfs:label>
    <skos:definition xml:lang="en">To review the Policy applicable to the Asset.</skos:definition>
    <skos:note xml:lang="en">Used when human intervention is required to review the Policy. May link to an Asset which represents the full Policy information.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/rightOperand">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#DatatypeProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Constraint"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Has Right Operand</rdfs:label>
    <rdfs:range>
      <owl:Class>
        <owl:unionOf>
          <rdf:Description>
            <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/RightOperand"/>
            <rdf:rest>
              <rdf:Description>
                <rdf:first rdf:resource="http://www.w3.org/2000/01/rdf-schema#Literal"/>
                <rdf:rest>
                  <rdf:Description>
                    <rdf:first rdf:resource="http://www.w3.org/2001/XMLSchema#anyURI"/>
                    <rdf:rest rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"/>
                  </rdf:Description>
                </rdf:rest>
              </rdf:Description>
            </rdf:rest>
          </rdf:Description>
        </owl:unionOf>
      </owl:Class>
    </rdfs:range>
    <skos:definition xml:lang="en">The value of the right operand in a constraint expression.</skos:definition>
    <skos:note xml:lang="en">When used with set-based operators, a list of values may be used.</skos:note>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/rightOperandReference">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Constraint"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Has Right Operand Reference</rdfs:label>
    <skos:definition xml:lang="en">A reference to a web resource providing the value for the right operand of a Constraint.</skos:definition>
    <skos:note xml:lang="en">An IRI that MUST be dereferenced to obtain the actual right operand value. When used with set-based operators, a list of IRIs may be used</skos:note>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/scope">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Scope</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The identifier of a scope that provides context to the extent of the entity.</skos:definition>
    <skos:note xml:lang="en">Used to define scopes for Assets and Parties.</skos:note>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/secondaryUse">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Secondary Use</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of using the asset for a purpose other than the purpose it was intended for.</skos:definition>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/sell">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Sell</rdfs:label>
    <skos:definition xml:lang="en">To transfer the ownership of the Asset to a third party with compensation and while deleting the original asset.</skos:definition>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/transfer"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/share">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Share</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of the non-commercial reproduction and distribution of the asset to third-parties.</skos:definition>
    <skos:exactMatch rdf:resource="http://creativecommons.org/ns#Sharing"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/shareAlike">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Share-alike</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of distributing any derivative asset under the same terms as the original asset.</skos:definition>
    <skos:exactMatch rdf:resource="http://creativecommons.org/ns#ShareAlike"/>
  </Action>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/source">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain>
      <owl:Class>
        <owl:unionOf>
          <rdf:Description>
            <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/AssetCollection"/>
            <rdf:rest>
              <rdf:Description>
                <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/PartyCollection"/>
                <rdf:rest rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"/>
              </rdf:Description>
            </rdf:rest>
          </rdf:Description>
        </owl:unionOf>
      </owl:Class>
    </rdfs:domain>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Source</rdfs:label>
    <skos:definition xml:lang="en">Reference to a Asset/PartyCollection</skos:definition>
    <skos:note xml:lang="en">Used by AssetCollection and PartyCollection when constraints are applied.</skos:note>
  </rdf:Property>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/spatial">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Geospatial Named Area</rdfs:label>
    <skos:definition xml:lang="en">A named and identified geospatial area with defined borders which is used for exercising the action of the Rule. An IRI MUST be used to represent this value.</skos:definition>
    <skos:note xml:lang="en">A code value for the area and source of the code must be presented in the Right Operand. &lt;br /&gt;Example: the [[iso3166]] Country Codes or the Getty Thesaurus of Geographic Names. </skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/spatialCoordinates">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Geospatial Coordinates</rdfs:label>
    <skos:broaderTransitive rdf:resource="http://www.w3.org/ns/odrl/2/spatial"/>
    <skos:definition xml:lang="en">A set of coordinates setting the borders of a geospatial area used for exercising the action of the Rule. The coordinates MUST include longitude and latitude, they MAY include altitude and the geodetic datum.</skos:definition>
    <skos:note xml:lang="en">The default values are the altitude of earth's surface at this location and the WGS 84 datum.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/status">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Constraint"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Status</rdfs:label>
    <skos:definition xml:lang="en">the value generated from the leftOperand action or a value related to the leftOperand set as the reference for the comparison.</skos:definition>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/stream">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Stream</rdfs:label>
    <skos:definition xml:lang="en">To deliver the Asset in real-time.</skos:definition>
    <skos:note>The Asset maybe utilised in real-time as it is being delivered. If the action is to be performed to a wider audience than just the Assignees, then the Recipient constraint is recommended to be used.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <UndefinedTerm rdf:about="http://www.w3.org/ns/odrl/2/support">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Support Undefined Actions</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The Action is to be supported as part of the policy – and the policy remains valid.</skos:definition>
    <skos:note xml:lang="en">Used to support actions not known to the policy system.</skos:note>
  </UndefinedTerm>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/synchronize">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Synchronize</rdfs:label>
    <skos:definition xml:lang="en">To use the Asset in timed relations with media (audio/visual) elements of another Asset.</skos:definition>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/system">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">System</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">An identified computing system used for exercising the action of the Rule.</skos:definition>
    <skos:exactMatch rdf:resource="http://www.w3.org/ns/odrl/2/systemDevice"/>
    <skos:note>See System Device</skos:note>
  </LeftOperand>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/systemDevice">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">System Device</rdfs:label>
    <skos:definition xml:lang="en">An identified computing system or computing device used for exercising the action of the Rule.</skos:definition>
    <skos:exactMatch rdf:resource="http://www.w3.org/ns/odrl/2/device"/>
    <skos:exactMatch rdf:resource="http://www.w3.org/ns/odrl/2/system"/>
    <skos:note xml:lang="en">Example: The system device can be identified by a unique code created from the used hardware.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/target">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain>
      <owl:Class>
        <owl:unionOf>
          <rdf:Description>
            <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Rule"/>
            <rdf:rest>
              <rdf:Description>
                <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
                <rdf:rest rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"/>
              </rdf:Description>
            </rdf:rest>
          </rdf:Description>
        </owl:unionOf>
      </owl:Class>
    </rdfs:domain>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Target</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/Asset"/>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/relation"/>
    <skos:definition xml:lang="en">The target property indicates the Asset that is the primary subject to which the Rule action directly applies.</skos:definition>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/textToSpeech">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Text-to-speech</rdfs:label>
    <skos:definition xml:lang="en">To have a text Asset read out loud.</skos:definition>
    <skos:note>If the action is to be performed to a wider audience than just the Assignees, then the recipient constraint is recommended to be used.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/timeInterval">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Recurring Time Interval</rdfs:label>
    <skos:definition xml:lang="en">A recurring period of time before the next execution of the action of the Rule. Right operand value MUST be an xsd:duration as defined by [[xmlschema11-2]].</skos:definition>
    <skos:note>Only the eq operator SHOULD be used. &lt;br /&gt;Example: &lt;code&gt;timeInterval eq P7D&lt;/code&gt; indicates a recurring 7 day period.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/timedCount">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#DatatypeProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Timed Count</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/2000/01/rdf-schema#Literal"/>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The number of seconds after which timed metering use of the asset begins.</skos:definition>
    <skos:note xml:lang="en">This original term and URI from the OMA specification should be used: http://www.openmobilealliance.com/oma-dd/timed-count .</skos:note>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/trackedParty">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Tracked Party</rdfs:label>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/function"/>
    <skos:definition xml:lang="en">The Party whose usage is being tracked.</skos:definition>
    <skos:note xml:lang="en">May be specified as part of the acceptTracking action.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/trackingParty">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Tracking Party</rdfs:label>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/function"/>
    <skos:definition xml:lang="en">The Party who is tracking usage.</skos:definition>
    <skos:note xml:lang="en">May be specified as part of the acceptTracking action.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/transfer">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Transfer Ownership</rdfs:label>
    <skos:definition xml:lang="en">To transfer the ownership of the Asset in perpetuity.</skos:definition>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/transform">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Transform</rdfs:label>
    <skos:definition xml:lang="en">To convert the Asset into a different format.</skos:definition>
    <skos:note xml:lang="en">Typically used to convert the Asset into a different format for consumption on/transfer to a third party system.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/translate">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Translate</rdfs:label>
    <skos:definition xml:lang="en">To translate the original natural language of an Asset into another natural language.</skos:definition>
    <skos:note xml:lang="en">A new derivative Asset is created by that action.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/uid">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:domain>
      <owl:Class>
        <owl:unionOf>
          <rdf:Description>
            <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Policy"/>
            <rdf:rest>
              <rdf:Description>
                <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Asset"/>
                <rdf:rest>
                  <rdf:Description>
                    <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Rule"/>
                    <rdf:rest>
                      <rdf:Description>
                        <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Party"/>
                        <rdf:rest>
                          <rdf:Description>
                            <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/Constraint"/>
                            <rdf:rest>
                              <rdf:Description>
                                <rdf:first rdf:resource="http://www.w3.org/ns/odrl/2/LogicalConstraint"/>
                                <rdf:rest rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"/>
                              </rdf:Description>
                            </rdf:rest>
                          </rdf:Description>
                        </rdf:rest>
                      </rdf:Description>
                    </rdf:rest>
                  </rdf:Description>
                </rdf:rest>
              </rdf:Description>
            </rdf:rest>
          </rdf:Description>
        </owl:unionOf>
      </owl:Class>
    </rdfs:domain>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Unique Identifier</rdfs:label>
    <skos:definition xml:lang="en">An unambiguous identifier</skos:definition>
    <skos:note xml:lang="en">Used by the Policy, Rule, Asset, Party, Constraint, and Logical Constraint Classes.</skos:note>
  </rdf:Property>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/undefined">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Handle Undefined Term</rdfs:label>
    <rdfs:range rdf:resource="http://www.w3.org/ns/odrl/2/UndefinedTerm"/>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">Relates the strategy used for handling undefined actions to a Policy.</skos:definition>
    <skos:note xml:lang="en">If no strategy is specified, the default is invalid.</skos:note>
  </rdf:Property>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/uninstall">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Uninstall</rdfs:label>
    <skos:definition xml:lang="en">To unload and delete the computer program Asset from a storage device and disable its readiness for operation.</skos:definition>
    <skos:note xml:lang="en">The Asset is no longer accessible to the assignees after it has been used.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/unit">
    <rdfs:domain rdf:resource="http://www.w3.org/ns/odrl/2/Constraint"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Unit</rdfs:label>
    <skos:definition xml:lang="en">The unit of measurement of the value of the rightOperand or rightOperandReference of a Constraint.</skos:definition>
  </rdf:Property>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/unitOfCount">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Unit Of Count</rdfs:label>
    <skos:definition xml:lang="en">The unit of measure used for counting the executions of the action of the Rule.</skos:definition>
    <skos:note xml:lang="en">Note: Typically used with Duties to indicate the unit entity to be counted of the Action. &lt;br /&gt;Example: A duty to compensate and a unitOfCount constraint of 'perUser' would indicate that the compensation by multiplied by the 'number of users'.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/use">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Use</rdfs:label>
    <skos:definition xml:lang="en">To use the Asset</skos:definition>
    <skos:note xml:lang="en">Use is the most generic action for all non-third-party usage. More specific types of the use action can be expressed by more targetted actions.</skos:note>
  </Action>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/version">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Version</rdfs:label>
    <skos:definition xml:lang="en">The version of the target Asset.</skos:definition>
    <skos:note xml:lang="en">Example: Single Paperback or Multiple Issues or version 2.0 or higher.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <LeftOperand rdf:about="http://www.w3.org/ns/odrl/2/virtualLocation">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Virtual IT Communication Location</rdfs:label>
    <skos:definition xml:lang="en">An identified location of the IT communication space which is relevant for exercising the action of the Rule.</skos:definition>
    <skos:note xml:lang="en">Example: an Internet domain or IP address range.</skos:note>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
  </LeftOperand>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/watermark">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Watermark</rdfs:label>
    <skos:definition xml:lang="en">To apply a watermark to the Asset.</skos:definition>
    <skos:scopeNote xml:lang="en">Non-Normative</skos:scopeNote>
    <includedIn rdf:resource="http://www.w3.org/ns/odrl/2/use"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/write">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Write</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of writing to the Asset.</skos:definition>
    <skos:exactMatch rdf:resource="http://www.w3.org/ns/odrl/2/modify"/>
  </Action>
  <Action rdf:about="http://www.w3.org/ns/odrl/2/writeTo">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Write to</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
    <skos:definition xml:lang="en">The act of adding data to the Asset.</skos:definition>
    <skos:exactMatch rdf:resource="http://www.w3.org/ns/odrl/2/modify"/>
  </Action>
  <rdf:Property rdf:about="http://www.w3.org/ns/odrl/2/xone">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
    <rdfs:isDefinedBy rdf:resource="http://www.w3.org/ns/odrl/2/"/>
    <rdfs:label xml:lang="en">Only One</rdfs:label>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/ns/odrl/2/operand"/>
    <skos:definition xml:lang="en">The relation is satisfied when only one, and not more, of the Constaints is satisfied</skos:definition>
    <skos:note xml:lang="en">This property MUST only be used for Logical Constraints, and the list of operand values MUST be Constraint instances.</skos:note>
  </rdf:Property>
</rdf:RDF>
"""