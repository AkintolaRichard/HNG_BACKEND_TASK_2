#!/usr/bin/python

import csv
import json
import hashlib
import sys
import os

filename = sys.argv[1]

team = ''
seriesNum = 0
fileName = ''
name = ''
description = ''
gender = ''
uuid = ''





header = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    first = next(csvreader)
    first.append("")
    header = next(csvreader)
    header.append("Hash")
    
    team = first[0].capitalize()
    for i in range(20):
        aRow = next(csvreader)
        seriesNum = aRow[0]
        fileName = aRow[1]
        name = aRow[2]
        description = aRow[3]
        gender = aRow[4]
        uuid = aRow[6]
        toJson = {
            "format": "CHIP-007",
            "name": name,
            "minting_tool": team,
            "sensitive_content": False,
            "series_number": seriesNum,
            "series_total": 526,
            "attributes": {
                "trait_type": "gender",
                "value": gender
            },
            "collection": {
                "name": "Zuri NFT Tickets for Free Lunch",
                "id": uuid,
                "attributes": [
                    {
                        "type": "description",
                        "value": "Rewards for accomplishments during HNGi9."
                    }
                ]
            }
        }
        jsonName = f"{fileName}.json"
        with open(jsonName, "w") as outfile:
            json.dump(toJson, outfile)
        sha256_hash = hashlib.sha256()
        hash = ""
        with open(jsonName, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
            hash = sha256_hash.hexdigest()
        aRow.append(hash)
        rows.append(aRow)
    
    
    for row in csvreader:
        if row[1] == "" or row[2] == "":
            row.append("")
            continue
        if row[0].lower().startswith("team"):
            team = row[0]
            row.append("")
            continue
        team = team.capitalize()
        seriesNum = row[0]
        fileName = row[1]
        name = row[2]
        description = row[3]
        gender = row[4]
        uuid = row[6]
        toJson = {
            "format": "CHIP-007",
            "name": name,
            "minting_tool": team,
            "sensitive_content": False,
            "series_number": seriesNum,
            "series_total": 526,
            "attributes": {
                "trait_type": "gender",
                "value": gender
            },
            "collection": {
                "name": "Zuri NFT Tickets for Free Lunch",
                "id": uuid,
                "attributes": [
                    {
                        "type": "description",
                        "value": "Rewards for accomplishments during HNGi9."
                    }
                ]
            }
        }
        jsonName = f"{fileName}.json"
        with open(jsonName, "w") as outfile:
            json.dump(toJson, outfile)
        sha256_hash = hashlib.sha256()
        hash = ""
        with open(jsonName, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
            hash = sha256_hash.hexdigest()
        row.append(hash)
        rows.append(row)
        
        
        oldFileName = os.path.splitext(filename)[0]
        newFileName = f"{oldFileName}.output.csv"
        with open(newFileName, "w") as csvfile:
            csvwriter = csv.writer(csvfile)

            #csvwriter.writerow(first)

            csvwriter.writerow(header)
            
            for row in rows:
            	csvwriter.writerow(row)

print("Done")




