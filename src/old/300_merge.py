import pandas as pd
import hashlib
import json
import requests
import os
from PIL import Image
import glob

def r(data):
    map = {
        "https://diyhistory.org/hi/omekac/oa/collections/43/manifest.json": "https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/wakozukan/chukaizuhen/data/iiif/4256313/manifest.json",
        "https://nakamura196.github.io/iiif0/iiif/4256313": "https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/wakozukan/chukaizuhen/data/iiif/4256313",
        "https://nakamura196.github.io/iiif0/iiif/4256312": "https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/wakozukan/chukaizuhen/data/iiif/4256312"
    }

    for key in map:
        data = data.replace(key, map[key])

    return data

files = glob.glob("../static/data/curation/*.json")

manifests = {}

# selections = []

with open("/Users/nakamurasatoru/git/d_hi_ezu/chukaizuhen/static/data/index.json") as f:
    index = json.load(f)

metadata = {}

for item in index:
    member = r(item["member"])
    metadata[member] = [
        {
            "label" : "分類",
            "value": item["分類"][0]
        },
    {
        "label": "タイトル",
        "value" : item["label"]
    }]

print(metadata)

for file in files:

    if "top.json" in file:
        continue

    with open(file) as f:
        curation = json.load(f)

    selection = curation["selections"][0]

    selection["within"]["@id"] = r(selection["within"]["@id"])

    members = selection["members"]

    for member in members:
        member["@id"] = r(member["@id"])

        print(member["@id"])

        member["metadata"] = metadata[member["@id"]]
        member["label"] = metadata[member["@id"]][1]["value"]

        if "description" in member:
            del member["description"]

    manifest = selection["within"]["@id"]
    if manifest not in manifests:
        manifests[manifest] = {
            "@id": selection["@id"],
            "@type": "sc:Range",
            "members": {},
            "within" : selection["within"]
        }

    count = 0

    for member in members:
        spl = member["@id"].split("/")
        id = spl[-3]
        index = int(spl[-1].split("#")[0].replace("p", ""))



        manifests[manifest]["members"][id+"-"+str(index).zfill(4) + "-" + str(count).zfill(4)] = member

        count += 1
    # selections.append(selection)

selections = []
ids = ["4256312", "4256313"]
for id in ids:
    manifest = "https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/wakozukan/chukaizuhen/data/iiif/{}/manifest.json".format(id)
    map = manifests[manifest]["members"]

    members = []
    for key in sorted(map):
        members.append(map[key])

    manifests[manifest]["members"] = members

    selections.append(manifests[manifest])

curation = {
    "@context": [
        "http://iiif.io/api/presentation/2/context.json",
        "http://codh.rois.ac.jp/iiif/curation/1/context.json"
    ],
    "@id": "https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/wakozukan/chukaizuhen/data/curation/top.json",
    "@type": "cr:Curation",
    "label": "Automatic curation by IIIF Converter",
    "selections": selections,
    "viewingHint": "grid"
}

with open("../static/data/curation/top.json", 'w') as outfile:
    json.dump(curation, outfile, ensure_ascii=False,
        indent=4, sort_keys=True, separators=(',', ': '))