ld_licenses_rdf = """@prefix l4lod: <http://ns.inria.fr/l4lod/v2/> .
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
@prefix cc: <http://creativecommons.org/ns#> .
@prefix odrs: <http://schema.theodi.org/odrs#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://api.kasabi.com/dataset/nasa/apis/sparql> a odrl:Asset ;
    rdfs:label "NASA Space Flight & Astronaut data" ;
    rdfs:comment "Conversion of various NASA datasets into RDF, starting with the spacecraft data from the NSSDC master catalog." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/6592775249673133604133156838395276133156838395276> .

<http://cali.priloo.univ-nantes.fr/api/licenses> a odrl:Asset ;
    rdfs:label "CaLi Classifiaction" ;
    rdfs:comment "CaLi Classifiaction of licenses for the linked Data." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336041529177465061342556133156838395276> .

<http://dacura.cs.tcd.ie/sparql> a odrl:Asset ;
    rdfs:label "US Political Violence" ;
    rdfs:comment "A dataset comprising reports of political violence events causing death between 1780 and 2010 in the United States of America." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/5096279539387512726706942505975647712-4061970458552090152> .

<http://data.linkedct.org/sparql> a odrl:Asset ;
    rdfs:label "LinkedCT" ;
    rdfs:comment "Linked Clinical Trials." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/509627953938751272-9092176396027616413-4061970458552090152> .

<http://data.rism.info/sparql> a odrl:Asset ;
    rdfs:label "RISM Authority data" ;
    rdfs:comment "Authority data used in the (RISM catalogue, dataset description). It contains information about persons, organisations and literary works." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336046706942505975647712133156838395276> .

<http://dbpedia.org/sparql> a odrl:Asset ;
    rdfs:label "DBpedia" ;
    rdfs:comment "DBpedia.org is a community effort to extract structured information from Wikipedia and to make this information available on the Web. DBpedia allows you to ask sophisticated queries against Wikipedia and to link other datasets on the Web to Wikipedia data." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/6592775249673133604-9092176396027616413133156838395276> .

<http://drugs.linkeddata.finki.ukim.mk/> a odrl:Asset ;
    rdfs:label "LinkedDrugs: Linked Drug Product Data on a Global Scale" ;
    rdfs:comment "The LinkedDrugs dataset with drug product data from different countries." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336046706942505975647712133156838395276> .

<http://enipedia.tudelft.nl/sparql> a odrl:Asset ;
    rdfs:label "Enipedia - Energy Industry Data" ;
    rdfs:comment "Enipedia is an active exploration into the applications of wikis and the semantic web for energy and industry issues. Through this we seek to create a collaborative environment for discussion, while also providing the tools that allow for data from different sources to be connected, queried, and visualized from different perspectives." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/6592775249673133604133156838395276133156838395276> .

<http://foodpedia.tk/sparql> a odrl:Asset ;
    rdfs:label "FOODpedia" ;
    rdfs:comment "At this moment FOODpedia contains information about only Russian food products and ingredients that was crawled from GoodsMatrix web site. Also it has links to ingredients from AGROVOC." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336046706942505975647712133156838395276> .

<http://imgpedia.dcc.uchile.cl/sparql> a odrl:Asset ;
    rdfs:label "IMGpedia" ;
    rdfs:comment "IMGpedia is a large-scale linked dataset that incorporates visual information of the images from the Wikimedia Commons dataset: it brings together descriptors of the visual content of 15 million images, 450 million visual-similarity relations between those images, links to image metadata from DBpedia Commons, and links to the DBpedia resources associated with individual images." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336046706942505975647712133156838395276> .

<http://l3s.de/tweetsKB/endpoint/> a odrl:Asset ;
    rdfs:label "TweetsKB - A Public and Large-Scale RDF Corpus of Annotated Tweets" ;
    rdfs:comment "TweetsKB is a public RDF corpus of anonymized data for a large collection of annotated tweets. The dataset currently contains data for more than 1.5 billion tweets, spanning almost 5 years (January 2013 - November 2017). Metadata information about the tweets as well as extracted entities, sentiments, hashtags and user mentions are exposed in RDF using established RDF/S vocabularies. For the sake of privacy, we anonymize the usernames and we do not provide the text of the tweets. However, through the tweet IDs, actual tweet content and further information can be fetched." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336046706942505975647712133156838395276> .

<http://ldf.fi/warsa/sparql> a odrl:Asset ;
    rdfs:label "WarSampo" ;
    rdfs:comment "This dataset includes harmonized data of different kinds concerning the Second World War in Finland, separated in different graphs representing events, actors, places, photographs, and other aspects and documentation of the war. To test and demonstrate its usefulness, this data service is in use in the semantic portal WarSampo explained in more detail in the project page." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336046706942505975647712133156838395276> .

<http://linkeddata.ge.imati.cnr.it:8890/sparql> a odrl:Asset ;
    rdfs:label "EARTh" ;
    rdfs:comment "The Environmental Applications Reference Thesaurus (EARTh) has been compiled and is maintained by the CNR-IIA-EKOLab to facilitate the indexing, retrieval, harmonizing and integration of human- and machine-readable environmental information from disparate sources, across the cultural and linguistic barriers. Ownership of such material always remains with the CNR-IIA-EKOLab." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/5096279539387512726706942505975647712-4061970458552090152> .

<http://lod-a-lot.lod.labs.vu.nl/LOD-a-lot> a odrl:Asset ;
    rdfs:label "LOD-a-lot" ;
    rdfs:comment "A Queryable Dump of the LOD Cloud" ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/6592775249673133604133156838395276133156838395276> .

<http://lodstats.aksw.org/sparql> a odrl:Asset ;
    rdfs:label "LODStats" ;
    rdfs:comment "LODStats: The Data Web Census Dataset." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/6592775249673133604-9092176396027616413133156838395276> .

<http://purl.org/NET/rdflicense> a odrl:Asset ;
    rdfs:label "RDFLicense" ;
    rdfs:comment "This dataset contains 126 licenses (suitable for general works, data, etc.) expressed as RDF.This work is the joint effort of OEG-UPM (VÃ­ctor RodrÃ­guez-Doncel) and INRIA (Serena Villata). The editors have not acted in behalf of any of the license issuers, do not claim the legal value of this RDF-version of the licenses, and explicitly decline any responsibility in their use." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336046706942505975647712133156838395276> .

<http://sparql.msc2010.org/> a odrl:Asset ;
    rdfs:label "Mathematics Subject Classification" ;
    rdfs:comment "The Mathematics Subject Classification (MSC2010)." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/509627953938751272-9092176396027616413-4061970458552090152> .

<http://spatial.ucd.ie/lod/sparql> a odrl:Asset ;
    rdfs:label "OSM Semantic Network" ;
    rdfs:comment "The OSM Semantic Network is a Semantic Web resource extracted from the OpenStreetMap Wiki website, encoded as a SKOS vocabulary." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/6592775249673133604-9092176396027616413133156838395276> .

<http://taxref.mnhn.fr/sparql> a odrl:Asset ;
    rdfs:label "TAXREF-LD: Linked Data French Taxonomic Register" ;
    rdfs:comment "TAXREF-LD is the Linked Data representation of TAXREF, the French national taxonomical register for fauna, flora and fungus, that covers mainland France and overseas territories. It accounts for over 500000 scientific names." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/5096279539387512726706942505975647712-4061970458552090152> .

<http://vocabulary.semantic-web.at/PoolParty/sparql/AustrianSkiTeam> a odrl:Asset ;
    rdfs:label "Alpine Ski Racers of Austria" ;
    rdfs:comment "Austrian top-skiers active in world cup." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/6592775249673133604-9092176396027616413133156838395276> .

<http://www.influencetracker.com:8890/sparql> a odrl:Asset ;
    rdfs:label "Influence Tracker Dataset" ;
    rdfs:comment "Datasets regarding the Influence Tracker service." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336046706942505975647712133156838395276> .

<https://ckannet-storage.commondatastorage.googleapis.com/2014-11-23T07:56:29.726Z/roadaccidents.ttl> a odrl:Asset ;
    rdfs:label "Fatal Traffic Accidents in greek roads" ;
    rdfs:comment "Fatal Traffic Accidents in greek roads (From 01-Jan-2010 to 11-Aug-2014)" ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/6592775249673133604-9092176396027616413133156838395276> .

<https://data.opendatasoft.com/explore/api/tpf/autolib-disponibilite-temps-reel@parisdata> a odrl:Asset ;
    rdfs:label "Autolib - DisponibilitÃ© temps rÃ©el" ;
    rdfs:comment "DonnÃ©es de disponibilitÃ©s des voitures et bornes des stations Autolib." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/6592775249673133604-9092176396027616413133156838395276> .

<https://data.opendatasoft.com/explore/api/tpf/bicycle-crash-data-chapel-hill-region@townofchapelhill> a odrl:Asset ;
    rdfs:label "Bicycle Crashes" ;
    rdfs:comment "This data set maps the locations of crashes involving bikes in the Chapel Hill Region of North Carolina." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/6592775249673133604133156838395276133156838395276> .

<https://data.opendatasoft.com/explore/api/tpf/coal-production-by-provinces@kapsarc> a odrl:Asset ;
    rdfs:label "Coal Production By Province" ;
    rdfs:comment "Coal production by month from PK Thinker." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/31459231771756486426706942505975647712-774852002940443510> .

<https://data.opendatasoft.com/explore/api/tpf/demand-data-at-province@kapsarc> a odrl:Asset ;
    rdfs:label "Demand Data at Province" ;
    rdfs:comment "This dataset contains China Demand Data at Province 2004-2017 Power Knowledge Thinker Demand, Export API data for more datasets to advance energy economics research." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/31459231771756486426706942505975647712-774852002940443510> .

<https://data.opendatasoft.com/explore/api/tpf/durham-bike-parking@durham> a odrl:Asset ;
    rdfs:label "Durham Bike Racks" ;
    rdfs:comment "Dataset of bike racks in the City of Durham" ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/6592775249673133604-9092176396027616413133156838395276> .

<https://data.opendatasoft.com/explore/api/tpf/extra-vehicular-activity@datastro> a odrl:Asset ;
    rdfs:label "Extra-Vehicular Activity" ;
    rdfs:comment "Activities done by an astronaut outside a spacecraft beyond the Earth's appreciable atmosphere. Data for US and Russia." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/31459231771756486426706942505975647712-774852002940443510> .

<https://data.opendatasoft.com/explore/api/tpf/jcdecaux_bike_data@public> a odrl:Asset ;
    rdfs:label "JCDecaux Bike Stations Data" ;
    rdfs:comment "JCDecaux bike stations availability data. This dataset is updated in real time. You can access these data directly from the JCDecaux Developer site: https://developer.jcdecaux.com/#/home." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336046706942505975647712133156838395276> .

<https://data.opendatasoft.com/explore/api/tpf/places-disponibles-parkings-saemes@saemes> a odrl:Asset ;
    rdfs:label "Places disponibles parkings Saemes" ;
    rdfs:comment "Ce jeu de donnÃ©es prÃ©sente les places disponibles en temps rÃ©el des parkings exploitÃ©s par Saemes Ã  Paris et en Ile-de-France." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336046706942505975647712133156838395276> .

<https://data.opendatasoft.com/explore/api/tpf/power-supply-and-consumption0@kapsarc> a odrl:Asset ;
    rdfs:label "Power Supply and Consumption" ;
    rdfs:comment "This dataset contains China Power Supply and Consumption 2006-2017 Power Knowledge Thinker , Export API data for more datasets to advance energy economics research." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/31459231771756486426706942505975647712-774852002940443510> .

<https://data.opendatasoft.com/explore/api/tpf/public-bike-pumps@bristol> a odrl:Asset ;
    rdfs:label "Public bike pumps Bristol" ;
    rdfs:comment "Location of free to use bycyle pumps Bristol City Council" ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336046706942505975647712133156838395276> .

<https://datahub.ckan.io/dataset/c8bb2280-5919-4fbb-85b1-52d03d403e21/resource/38b05231-715e-411e-9c04-4752d08dfa6d/download/specialitydatahub.rdf> a odrl:Asset ;
    rdfs:label "Russian Universities Specialities" ;
    rdfs:comment "This ontology describes a degree of higher education and the direction of bachelor's and master's degrees in the Russian Federation and their compliance with the various official lists. It is assumed that a given ontology can be used in various applications of the Semantic Web in Russian higher education." ;
    odrl:hasPolicy <http://cali.priloo.univ-nantes.fr/api/ld/licenses/6592775249673133604-9092176396027616413133156838395276> .

<http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336041529177465061342556133156838395276> a odrl:Policy ;
    rdfs:label "MIT" ;
    l4lod:licensingTerms <https://opensource.org/licenses/MIT> ;
    odrl:Duty cc:Notice ;
    odrl:Permission cc:CommericalUse,
        cc:DerivativeWorks,
        cc:Distribution,
        cc:Reproduction,
        odrl:modify ;
    odrl:target <http://cali.priloo.univ-nantes.fr/api/licenses> .

<http://cali.priloo.univ-nantes.fr/api/ld/licenses/509627953938751272-9092176396027616413-4061970458552090152> a odrl:Policy ;
    rdfs:label "CC BY-NC-SA" ;
    l4lod:licensingTerms <https://creativecommons.org/licenses/by-nc-sa/3.0/legalcode> ;
    odrl:Duty cc:Attribution,
        cc:Notice,
        cc:ShareAlike ;
    odrl:Permission cc:DerivativeWorks,
        cc:Distribution,
        cc:Reproduction,
        odrl:modify ;
    odrl:Prohibition cc:CommericalUse ;
    odrl:target <http://data.linkedct.org/sparql>,
        <http://sparql.msc2010.org/> .

<http://cali.priloo.univ-nantes.fr/api/ld/licenses/5096279539387512726706942505975647712-4061970458552090152> a odrl:Policy ;
    rdfs:label "CC BY-NC" ;
    l4lod:licensingTerms <https://creativecommons.org/licenses/by-nc/3.0/legalcode> ;
    odrl:Duty cc:Attribution,
        cc:Notice ;
    odrl:Permission cc:DerivativeWorks,
        cc:Distribution,
        cc:Reproduction,
        odrl:modify ;
    odrl:Prohibition cc:CommericalUse ;
    odrl:target <http://dacura.cs.tcd.ie/sparql>,
        <http://linkeddata.ge.imati.cnr.it:8890/sparql>,
        <http://taxref.mnhn.fr/sparql> .

<http://cali.priloo.univ-nantes.fr/api/ld/licenses/6592775249673133604133156838395276133156838395276> a odrl:Policy ;
    rdfs:label "CC-Ze",
        "ODC-PDDL",
        "Public-domain" ;
    l4lod:licensingTerms <https://creativecommons.org/publicdomain/zero/1.0/legalcode>,
        <https://www.opendatacommons.org/licenses/pddl/1-0> ;
    odrl:Permission cc:CommericalUse,
        cc:DerivativeWorks,
        cc:Distribution,
        cc:Reproduction,
        odrl:modify ;
    odrl:target <http://api.kasabi.com/dataset/nasa/apis/sparql>,
        <http://enipedia.tudelft.nl/sparql>,
        <http://lod-a-lot.lod.labs.vu.nl/LOD-a-lot>,
        <https://data.opendatasoft.com/explore/api/tpf/bicycle-crash-data-chapel-hill-region@townofchapelhill> .

<http://cali.priloo.univ-nantes.fr/api/ld/licenses/31459231771756486426706942505975647712-774852002940443510> a odrl:Policy ;
    rdfs:label "CC BY-NC-ND" ;
    l4lod:licensingTerms <https://creativecommons.org/licenses/by-nc-nd/3.0/legalcode> ;
    odrl:Duty cc:Attribution,
        cc:Notice ;
    odrl:Permission cc:Distribution,
        cc:Reproduction ;
    odrl:Prohibition cc:CommericalUse,
        cc:DerivativeWorks,
        odrl:modify ;
    odrl:target <https://data.opendatasoft.com/explore/api/tpf/coal-production-by-provinces@kapsarc>,
        <https://data.opendatasoft.com/explore/api/tpf/demand-data-at-province@kapsarc>,
        <https://data.opendatasoft.com/explore/api/tpf/extra-vehicular-activity@datastro>,
        <https://data.opendatasoft.com/explore/api/tpf/power-supply-and-consumption0@kapsarc> .

<http://cali.priloo.univ-nantes.fr/api/ld/licenses/6592775249673133604-9092176396027616413133156838395276> a odrl:Policy ;
    rdfs:label "CC BY-SA",
        "GFDL",
        "ODC-ODbL" ;
    l4lod:licensingTerms <https://opendatacommons.org/licenses/odbl/1.0> ;
    odrl:Duty cc:Attribution,
        cc:Notice,
        cc:ShareAlike ;
    odrl:Permission cc:CommericalUse,
        cc:DerivativeWorks,
        cc:Distribution,
        cc:Reproduction,
        odrl:modify ;
    odrl:target <http://dbpedia.org/sparql>,
        <http://lodstats.aksw.org/sparql>,
        <http://spatial.ucd.ie/lod/sparql>,
        <http://vocabulary.semantic-web.at/PoolParty/sparql/AustrianSkiTeam>,
        <https://ckannet-storage.commondatastorage.googleapis.com/2014-11-23T07:56:29.726Z/roadaccidents.ttl>,
        <https://data.opendatasoft.com/explore/api/tpf/autolib-disponibilite-temps-reel@parisdata>,
        <https://data.opendatasoft.com/explore/api/tpf/durham-bike-parking@durham>,
        <https://datahub.ckan.io/dataset/c8bb2280-5919-4fbb-85b1-52d03d403e21/resource/38b05231-715e-411e-9c04-4752d08dfa6d/download/specialitydatahub.rdf> .

<http://cali.priloo.univ-nantes.fr/api/ld/licenses/65927752496731336046706942505975647712133156838395276> a odrl:Policy ;
    rdfs:label "CC BY",
        "Etalab-ol-lo",
        "GPL3",
        "ODC-By",
        "UK-open-government" ;
    l4lod:licensingTerms <http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/>,
        <https://creativecommons.org/licenses/by/3.0/legalcode>,
        <https://github.com/etalab/licence-ouverte/blob/master/open-licence.md>,
        <https://opendatacommons.org/licenses/by/1-0/>,
        <https://www.gnu.org/licenses/gpl-3.0> ;
    odrl:Duty cc:Attribution,
        cc:Notice ;
    odrl:Permission cc:CommericalUse,
        cc:DerivativeWorks,
        cc:Distribution,
        cc:Reproduction,
        odrl:modify ;
    odrl:target <http://data.rism.info/sparql>,
        <http://drugs.linkeddata.finki.ukim.mk/>,
        <http://foodpedia.tk/sparql>,
        <http://imgpedia.dcc.uchile.cl/sparql>,
        <http://l3s.de/tweetsKB/endpoint/>,
        <http://ldf.fi/warsa/sparql>,
        <http://purl.org/NET/rdflicense>,
        <http://www.influencetracker.com:8890/sparql>,
        <https://data.opendatasoft.com/explore/api/tpf/jcdecaux_bike_data@public>,
        <https://data.opendatasoft.com/explore/api/tpf/places-disponibles-parkings-saemes@saemes>,
        <https://data.opendatasoft.com/explore/api/tpf/public-bike-pumps@bristol> ."""
