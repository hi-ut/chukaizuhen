import pandas as pd
import hashlib
import json
import requests
import os
from PIL import Image

images = {
    "https://diyhistory.org/hi/omekac/oa/collections/42/manifest.json" : "/Users/nakamurasatoru/git/d_dzi/iiif0/docs/files/original/chukaizuhen/4256312/4256312-",
    "https://diyhistory.org/hi/omekac/oa/collections/43/manifest.json" : "/Users/nakamurasatoru/git/d_dzi/iiif0/docs/files/original/chukaizuhen/4256313/4256313-"
}

prefix = "https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/wakozukan/chukaizuhen"

for manifest in images:
    value = images[manifest]
    id = value.split("/")[-2]
    print(id)

    odir = "../static/data/iiif/" + id

    os.makedirs(odir, exist_ok=True)

    opath = odir + "/manifest.json"

    with open(opath) as f:
        manifest = json.load(f)

    canvases = manifest["sequences"][0]["canvases"]

    for canvas in canvases:
        del canvas["otherContent"]
        del canvas["metadata"]

    with open(opath, 'w') as outfile:
        json.dump(manifest, outfile, ensure_ascii=False,
            indent=4, sort_keys=True, separators=(',', ': '))