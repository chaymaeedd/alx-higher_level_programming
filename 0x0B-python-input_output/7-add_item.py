#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file.
"""

import sys
import os.path
from typing import List
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_item(args: List[str]) -> List[str]:
    """
    Adds all arguments to a Python list.
    """
    filename = "add_item.json"
    items = []
    if os.path.exists(filename):
        items = load_from_json_file(filename)
    items += args
    save_to_json_file(items, filename)
    return items

if __name__ == "__main__":
    args = sys.argv[1:]
    add_item(args)

