import sys
import bs4
import hashlib
import json
import bs4
import requests
import time
import os
import urllib.parse
import csv
import glob

static_dir = "/Users/nakamurasatoru/git/d_toyo/app/static/data/es"

files = glob.glob(static_dir + "/*.json")

actions = []

for file in files:

    json_open = open(file, 'r')
    df = json.load(json_open)

    filename = file.split("/")[-1].split(".")[0]

    for obj in df:

        id = obj["_id"]

        source = obj["_source"]

        fulltext = source["_label"]

        thumbnail = source["_thumbnail"]
        thumbnail = thumbnail.replace("https://iiif.dl.itc.u-tokyo.ac.jp/iiif/tmp/toyo/suikei/", "https://img.toyobunko-lab.jp/iiif/premodern_chinese/suikeichuzu/")
        thumbnail = thumbnail.replace("https://iiif.dl.itc.u-tokyo.ac.jp/iiif/tmp/", "https://img.toyobunko-lab.jp/iiif/premodern_chinese/suikeichuzu/")

        item = {
            "label" : source["_label"],
            "manifest" : source["_manifest"],
            "member" : source["_member"],
            "objectID" : id,
            "thumbnail" : thumbnail,
            "group": [filename]
        }

        for key in source:
            if "_" not in key:
                item[key] = source[key]
                for e in source[key]:
                    fulltext += ", " + str(e)

        item["fulltext"] = fulltext

        actions.append(item)

        with open("../static/data/item/{}.json".format(id), 'w') as outfile:
            json.dump(item, outfile, ensure_ascii=False,
                        indent=4, sort_keys=True, separators=(',', ': '))

   
with open("../static/data/index.json", 'w') as outfile:
    json.dump(actions, outfile, ensure_ascii=False,
                indent=4, sort_keys=True, separators=(',', ': '))