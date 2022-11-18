#!/usr/bin/python3
"""a script that adds all arguments to a Python
list and save them to a file json"""
import sys
save_to_json_file = __import__("5-save_to_json_file.py").5-save_to_json_file.py
load_from_json_file = __import__("6-load_from_json_file.py").6-load_from_json_file.py

file_name = "add_item.json"
try:
    filelist = load_from_json_file(file_name)
    save_to_json_file(filelist + sys.argv[1:], file_name)
except FileNotFoundError:
    save_to_json_file(sys.argv[1:], file_name)