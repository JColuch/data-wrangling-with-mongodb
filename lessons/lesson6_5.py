#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the
    changes needed to fix the unexpected street types to the appropriate ones
    in the expected list. You have to add mappings only for the actual problems
    you find in this OSMFILE, not a generalized solution, since that may and
    will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should
    return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""


import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint


OSMFILE = "example.osm"
STREET_TYPE_RE = re.compile(r'\b\S+\.?$', re.IGNORECASE)
EXPECTED = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place",
            "Square", "Lane", "Road", "Trail", "Parkway", "Commons"]
MAPPING = {
    "St": "Street",
    "St.": "Street",
    "Ave": "Avenue",
    "Rd.": "Road"
}


def audit_street_type(street_types, street_name):
    """Determine type of stree of street name and increment count
    in street types.
    """
    match = STREET_TYPE_RE.search(street_name)
    if match:
        street_type = match.group()
        if street_type not in EXPECTED:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    """Return true if element 'k' tag represents a street."""
    return elem.attrib['k'] == "addr:street"


def audit(osmfile):
    """Audit osm xml file street names."""
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])

    return street_types


def update_name(name, mapping):
    """Transform streetname to desired format"""
    match = re.search(STREET_TYPE_RE, name)
    if match:
        match = match.group(0)

    new_name = mapping[match]

    name = re.sub(match, new_name, name)

    return name


def test():
    """Test audit function"""
    st_types = audit(OSMFILE)
    assert len(st_types) == 3
    pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, MAPPING)
            print name, "=>", better_name
            if name == "West Lexington St.":
                assert better_name == "West Lexington Street"
            if name == "Baldwin Rd.":
                assert better_name == "Baldwin Road"


if __name__ == '__main__':
    test()
