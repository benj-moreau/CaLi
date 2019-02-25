@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix odrl:  <http://www.w3.org/ns/odrl/2/> .
@prefix cali:  <http://cali.priloo.univ-nantes.fr/ontology#> .

odrl:Permission  a  cali:DeonticState  ;
          rdfs:label        "Permission" ;
          rdfs:comment      "The ability to perform an Action over an Asset." ;
          cali:lessRestrictiveThan      odrl:Permission,
                      odrl:Prohibition,
                      odrl:Duty .

odrl:Prohibition  a  cali:DeonticState  ;
          rdfs:label        "Prohibition" ;
          rdfs:comment      "The inability to perform an Action over an Asset." ;
          cali:lessRestrictiveThan      odrl:Prohibition,
                      odrl:Duty .

odrl:Duty  a  cali:DeonticState  ;
          rdfs:label        "Duty" ;
          rdfs:comment      "The obligation to perform an Action" ;
          cali:lessRestrictiveThan      odrl:Duty .
