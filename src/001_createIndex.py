import pandas as pd
import hashlib
import json
import requests
import os
from PIL import Image
import glob
import datetime
today = datetime.datetime.now()

cr_path = "../static/data/curation/top.json"
with open(cr_path) as f:
    df = json.load(f)

selections = df["selections"]

index = []

for selection in selections:
    manifest = selection["within"]["@id"]
    members = selection["members"]

    for member in members:
        member_id = member["@id"]

        uuid = hashlib.md5(member_id.encode('utf-8')).hexdigest()

        objectID = uuid

        item = {
            "objectID": objectID,
            "label" : member["label"],
            "分類": [member["metadata"][0]["value"]],
            "_updated": format(today, '%Y-%m-%d'),
            "manifest": manifest,
            "member": member_id,
            "thumbnail": member["thumbnail"],
            "（国立公文書館メタデータ）階層" : ["内閣文庫 > 漢書 > 史の部"],
            "（国立公文書館メタデータ）請求番号" : ["２９１－００８４"],
            "（国立公文書館メタデータ）人名": ["著者:鄭若曾（明）"],
            "（国立公文書館メタデータ）数量": ["19冊"],
            "（国立公文書館メタデータ）書誌事項": ["刊本（序刊） ,明嘉靖 ,明嘉靖41年"],
            "（国立公文書館メタデータ）利用制限の区分": ["公開"],
            "（国立公文書館メタデータ）言語": ["中国語"],
            "（国立公文書館メタデータ）巻数": ["１３巻"],
            "（国立公文書館メタデータ）旧蔵者": ["昌平坂学問所"],
            "（国立公文書館メタデータ）関連事項": ["山本北山旧蔵"],
            "（国立公文書館メタデータ）メタデータ二次利用の可否": ["可：CC0（CC0 1.0 全世界 パブリック・ドメイン提供）"],
        }

        if "4256312" in manifest:
            url = "https://www.digital.archives.go.jp/img/4256312"
            no = "0018"
        else:
            url = "https://www.digital.archives.go.jp/item/4256313"
            no = "0019"

        item["URL"] = [url]
        item["（国立公文書館メタデータ）冊次"] = [no]
        

        with open("../static/data/item/{}.json".format(objectID), 'w') as outfile:
            json.dump(item, outfile, ensure_ascii=False,
                indent=4, sort_keys=True, separators=(',', ': '))

        fulltext = ""
        for key in item:
            text = str(item[key])
            if not text.startswith("http"):
                fulltext += " " + text

        item["fulltext"] = fulltext # [fulltext]

        index.append(item)

    

with open("../static/data/index.json", 'w') as outfile:
    json.dump(index, outfile, ensure_ascii=False,
            indent=4, sort_keys=True, separators=(',', ': '))