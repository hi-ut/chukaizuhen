import pandas as pd
import hashlib
import json
import requests
import os
from PIL import Image
import glob

cr_path = "../../static/chukaizuhen/data/curation/top.json"
with open(cr_path) as f:
    df = json.load(f)

selections = df["selections"]

for selection in selections:
    manifest = selection["within"]["@id"]
    members = selection["members"]

    for member in members:
        member_id = member["@id"]

        uuid = hashlib.md5(member_id.encode('utf-8')).hexdigest()

        opath = "../../static/chukaizuhen/data/files/medium/" + uuid + ".jpg"

        if not os.path.exists(opath):

            spl = member_id.split("/")

            parent = spl[-3]
            index = spl[-1].split("#")[0].replace("p", "")
            index = index.zfill(2)

            xywh = member_id.split("#xywh=")[1].split(",")

            x = int(xywh[0])
            y = int(xywh[1])
            w = int(xywh[2])
            h = int(xywh[3])

            

            path = "/Users/nakamurasatoru/git/d_dzi/iiif0/docs/files/original/chukaizuhen/{}/{}-{}.jp2".format(parent, parent, index)


            im = Image.open(path)
            im_crop = im.crop((x, y, x+w, y+h))

            w, h = im_crop.size

            width = 200
            height = int(h * 200 / w)

            im_crop = im_crop.resize((width, height))

            im_crop.save(opath)

        member["thumbnail"] = "https://www.hi.u-tokyo.ac.jp/collection/digitalgallery/wakozukan/chukaizuhen/data/files/medium/" + uuid + ".jpg"


with open(cr_path, 'w') as outfile:
    json.dump(df, outfile, ensure_ascii=False,
            indent=4, sort_keys=True, separators=(',', ': '))