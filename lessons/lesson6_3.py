#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Your task is to explore the data a bit more.
Before you process the data and add it into MongoDB, you should
check the "k" value for each "<tag>" and see if they can be valid keys in MongoDB,
as well as see if there are any other potential problems.

We have provided you with 3 regular expressions to check for certain patterns
in the tags. As we saw in the quiz earlier, we would like to change the data model
and expand the "addr:street" type of keys to a dictionary like this:
{"address": {"street": "Some value"}}
So, we have to see if we have such tags, and if we have any tags with problematic characters.
Please complete the function 'key_type'.
"""


import xml.etree.ElementTree as ET
import pprint
import re


LOWER = re.compile(r'^([a-z]|_)*$')
LOWER_COLON = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
PROBLEM_CHARS = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def key_type(element, keys):
    """Count xml element "tag" tags that contain unwanted chars"""
    if element.tag == "tag":
        k = element.get("k")

        if re.search(PROBLEM_CHARS, k):
            keys["problem_chars"] += 1
        elif re.search(LOWER, k):
            keys["lower"] += 1
        elif re.search(LOWER_COLON, k):
            keys["lower_colon"] += 1
        else:
            keys["other"] += 1

    return keys


def process_map(filename):
    """Process XML tags in file"""
    keys = {"lower": 0, "lower_colon": 0, "problem_chars": 0, "other": 0}

    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys


def test():
    """Test process_map function"""
    # You can use another testfile 'map.osm' to look at your solution.
    # Note that the assertions will be incorrect then.
    keys = process_map('example.osm')
    pprint.pprint(keys)
    assert keys == {'lower': 5, 'lower_colon': 0, 'other': 1, 'problemchars': 1}


if __name__ == "__main__":
    test()
