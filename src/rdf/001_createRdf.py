from rdflib import URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF, XSD
from SPARQLWrapper import SPARQLWrapper
from bs4 import BeautifulSoup
import requests
import json
import os
all = Graph()

with open("../../static/data/curation/top.json") as f:
    df = json.load(f)

selections = df["selections"]

parent = "term"
tag = "keyword"

for selection in selections:
    members = selection["members"]

    manifest = selection["within"]["@id"]

    for member in members:
        item = Graph()

        id = member["label"]
        label = member["label"]

        subjectStr = "https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/wakozukan/chukaizuhen/api/{}/{}/{}.json".format(parent, tag, id).replace(" ", "_")

        subject = URIRef(subjectStr)

        # label

        stmt = (subject, RDFS.label, Literal(label))
        item.add(stmt)

        # type

        t = "https://jpsearch.go.jp/term/type/Keyword"

        stmt = (subject, RDF.type, URIRef(t))
        item.add(stmt)

        # desc

        metadata = member["metadata"][0]

        d = metadata["label"] + ": " + metadata["value"]
        stmt = (subject, URIRef("http://schema.org/description"), Literal(d))
        item.add(stmt)

        # thumb

        stmt = (subject, URIRef("http://schema.org/image"), URIRef(member["thumbnail"]))
        item.add(stmt)

        # iiif

        iiif = manifest + "#canvas=" + member["@id"]
        stmt = (subject, URIRef("http://schema.org/relatedLink"), URIRef(iiif))
        item.add(stmt)

        ###

        path = "../../static/api/{}/{}/{}.json".format(parent, tag, id)
        os.makedirs(os.path.dirname(path), exist_ok=True)

        item.serialize(destination=path, format='json-ld')

        for stmt in item:
            all.add(stmt)

all.serialize(destination="../../static/api/data.ttl", format='turtle')