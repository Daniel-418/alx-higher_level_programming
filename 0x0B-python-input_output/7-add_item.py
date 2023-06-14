#!/usr/bin/python3
"""a script that adds all the arguments to a python list"""
import sys
import os
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
args = sys.argv

f = "add_item.json"
try:
    json_list = load_from_json_file(f)
except Exception:
    json_list = []

for i in args[1:]:
    json_list.append(i)

save_to_json_file(json_list, f)
