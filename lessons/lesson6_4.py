#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""


import xml.etree.ElementTree as ET
import pprint


def get_user(element):
    """Return user tag from xml element"""
    return element.get("user")


def process_map(filename):
    """Process XML file for unique user ids"""
    users = set()

    for _, element in ET.iterparse(filename):
        uid = element.get("uid")
        if uid:
            users.add(uid)

    return users


def test():
    """Test process_map function"""
    users = process_map('example.osm')
    pprint.pprint(users)
    assert len(users) == 6


if __name__ == "__main__":
    test()
