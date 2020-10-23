#! /usr/bin/env python3
import json
import os
import requests
import sys

txt_directory = 'module2_review/'
destination_directory = 'module2_json/'
try:
    os.mkdir('module2_json/')
except:
    print("Error while making directory:", sys.exc_info()[0])


revlist = []
for file in os.listdir(txt_directory):
    try:
        with open(txt_directory + file, 'r') as review:
            content = []
            for line in review.readlines():
                content.append(line.strip())
            print(content)
            revlist.append({'title': content[0], 'name': content[1], 'date': content[2], 'feedback': ''.join(content[3:len(content)])})
    except:
        print("Problems processing file: " + file + " Error type: ", sys.exc_info()[0])
print(revlist)
with open(destination_directory + 'reviews.json', 'w') as reviews_json:
    json.dump(revlist, reviews_json, indent=2)
# Lines for exam:
# response = requests.post("[URL]]/feedback", json=revlist)
# print(response.status_code)
