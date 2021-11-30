import pandas as pd
import hashlib
import json
import requests
import os
from PIL import Image

map = {
    "67444344d50f0d4e048f8767f6c60efa": "4256312",
    "b7a2141f42c4ef39c80df69ab159afea": "4256313",
}

reps = {
    "https://api.jsonbin.io/b/61179cb1e1b0604017afca2b/1": "https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/wakozukan/chukaizuhen/data/curation/4256312.json",
    "https://api.jsonbin.io/b/61179ec2d5667e403a427a40/1": "https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/wakozukan/chukaizuhen/data/curation/4256313.json",
    "https://nakamura196.github.io/iiif0/iiif/4256312": "https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/wakozukan/chukaizuhen/data/iiif/4256312",
    "https://diyhistory.org/hi/omekac/oa/collections/42/manifest.json" : "https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/wakozukan/chukaizuhen/data/iiif/4256312/manifest.json"
}

def r(data):
    for rep in reps:
        data = data.replace(rep, reps[rep])

    return data



for path in map:
    key = map[path]
    ipath = "data/curation/" + path + ".json"

    with open(ipath) as f:
        curation = json.load(f)

    cid = curation["@id"]
    cid = r(cid)

    curation["@id"] = cid

    selection = curation["selections"][0]

    sid = selection["@id"]
    selection["@id"] = r(sid)

    wid = selection["within"]["@id"]
    selection["within"]["@id"] = r(wid)

    members = selection["members"]

    for member in members:

        id = member["@id"]
        id = r(id)
        member["@id"] = id

    with open("../static/data/curation/" + key + ".json" , 'w') as outfile:
        json.dump(curation, outfile, ensure_ascii=False,
            indent=4, sort_keys=True, separators=(',', ': '))