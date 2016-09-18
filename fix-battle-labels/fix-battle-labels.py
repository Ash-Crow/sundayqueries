#!/usr/bin/env python3

from SPARQLWrapper import SPARQLWrapper, JSON

endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"

sparql = SPARQLWrapper(endpoint)
sparql.setQuery("""
SELECT ?item ?label WHERE {{
  ?item wdt:P31/wdt:P279* wd:Q178561 .
  ?item rdfs:label ?label . FILTER(LANG(?label) = "fr") .
  FILTER(STRSTARTS(?label, "Siège ")) .
}}
""")  # Link to query: http://tinyurl.com/z8bd26h

sparql.setReturnFormat(JSON)

results = sparql.query().convert()

for result in results["results"]["bindings"]:
    qid = result['item']['value'].split('/')[-1]
    label = result['label']['value']

    print(qid, label)