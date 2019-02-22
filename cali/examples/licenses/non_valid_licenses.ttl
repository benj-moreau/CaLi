@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
@prefix cc: <http://creativecommons.org/ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/License/1> a odrl:Policy ;
    rdfs:label "not valid:CommercialUse should not be a Duty" ;
    odrl:Duty cc:Notice,
        odrl:attachSource,
        odrl:stateChange,
        cc:CommericalUse ;
    odrl:Permission cc:DerivativeWorks,
        odrl:derive,
        odrl:distribute,
        odrl:modify,
        odrl:reproduce ;
    odrl:Prohibition odrl:holdLiable .

<http://example.org/License/2> a odrl:Policy ;
    rdfs:label "not valid:ShareAlike should not be a Prohibition" ;
    odrl:Duty cc:Notice,
        odrl:attachSource,
        odrl:stateChange;
    odrl:Permission cc:DerivativeWorks,
        odrl:derive,
        odrl:distribute,
        odrl:modify,
        odrl:reproduce ;
    odrl:Prohibition cc:ShareAlike .

<http://example.org/License/3> a odrl:Policy ;
    rdfs:label "not valid:Use is included in Commerical use" ;
    odrl:Duty cc:Notice,
        odrl:attachSource,
        odrl:stateChange;
    odrl:Permission cc:CommericalUse,
        odrl:derive,
        odrl:distribute,
        odrl:modify,
        odrl:reproduce ;
    odrl:Prohibition odrl:use .
