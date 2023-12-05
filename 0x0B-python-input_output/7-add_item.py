#!/usr/bin/python3
'''Load, add, save module'''
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
import sys


args_list = []
for i in range(len(sys.argv)):
    if i == 0:
        continue
    args_list.append(sys.argv[i])
try:
    obj = load_from_json_file("add_item.json")
except FileNotFoundError:
    obj = []
obj += args_list
save_to_json_file(obj, "add_item.json")
