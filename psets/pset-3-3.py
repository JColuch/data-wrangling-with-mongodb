#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.

Since in the previous quiz you made a decision on which value to keep for the "areaLand" field,
you now know what has to be done.

Finish the function fix_area(). It will receive a string as an input, and it has to return a float
representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you like, but changes to process_file
will not be taken into account.
The rest of the code is just an example on how this function can be used.
"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def fix_area(area):
    # Based on our audit research we know our dataset has 3 types for area
    # Now we can target those 3 types
    #Handle str
    if is_float(area):
        area = float(area)
    #Handle list
    elif area.strip().startswith("{"):
        #Strip brackets
        area = area.replace("{","")
        area = area.replace("}", "")

        #Split string
        val_one, val_two = area.split("|")

        if len(val_one) > len(val_two):
            area = float(val_one)
        else:
            area = float(val_two)
    #Handle NoneType
    else:
        area = None

    return area



def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        #skipping the extra metadata
        for i in range(3):
            l = reader.next()

        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
            data.append(line)

    return data


def test():
    data = process_file(CITIES)

    print "Printing three example results:"
    for n in range(5,8):
        pprint.pprint(data[n]["areaLand"])

    assert data[8]["areaLand"] == 55166700.0
    assert data[3]["areaLand"] == None


if __name__ == "__main__":
    test()