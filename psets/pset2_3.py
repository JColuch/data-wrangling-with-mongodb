#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Let's assume that you combined the code from the previous 2 exercises
# with code from the lesson on how to build requests, and downloaded all the data locally.
# The files are in a directory "data", named after the carrier and airport:
# "{}-{}.html".format(carrier, airport), for example "FL-ATL.html".
# The table with flight info has a table class="dataTDRight".
# There are couple of helper functions to deal with the data files.
# Please do not change them for grading purposes.
# All your changes should be in the 'process_file' function
# This is example of the datastructure you should return
# Each item in the list should be a dictionary containing all the relevant data
# Note - year, month, and the flight data should be integers
# You should skip the rows that contain the TOTAL data for a year
# data = [{"courier": "FL",
#         "airport": "ATL",
#         "year": 2012,
#         "month": 12,
#         "flights": {"domestic": 100,
#                     "international": 100}
#         },
#         {"courier": "..."}
# ]


from bs4 import BeautifulSoup
from zipfile import ZipFile
import os


DATADIR = "data"


def open_zip(datadir):
    with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
        myzip.extractall()


def process_all(datadir):
    files = os.listdir(datadir)
    return files


def process_file(f):
    # This is example of the datastructure you should return
    # Each item in the list should be a dictionary containing all the relevant data
    # Note - year, month, and the flight data should be integers
    # You should skip the rows that contain the TOTAL data for a year
    # data = [{"courier": "FL",
    #         "airport": "ATL",
    #         "year": 2012,
    #         "month": 12,
    #         "flights": {"domestic": 100,
    #                     "international": 100}
    #         },
    #         {"courier": "..."}
    # ]
    data = []
    info = {}
    info["courier"], info["airport"] = f[:6].split("-")
    
    with open("{}/{}".format(DATADIR, f), "r") as html:

        soup = BeautifulSoup(html)
        table_elm = soup.find("table", {"class": "dataTDRight"})
    
        table_rows = table_elm.find_all("tr")

        #Set flag value for first row
        is_first_row = True
        #iterate through each row
        for row in table_rows:
            #Skip first headers row
            if is_first_row:
                is_first_row = False
                continue
            
            row_data = row.find_all("td")

            #Skip any row that is a "total" row
            month = row_data[1].text
            if month == "TOTAL":
                continue
            month = int(month)
            courier = info["courier"]
            airport = info["airport"]
            year = int(row_data[0].text)
            domestic = int(row_data[2].text.replace(",",""))
            international = int(row_data[3].text.replace(",",""))

            #Assemble data obj
            row_obj = {
                "courier": courier,
                "airport": airport,
                "year": year,
                "month": month,
                "flights": {"domestic": domestic,
                         "international": international}
            }

            data.append(row_obj)

    return data


def test():
    print "Running a simple test..."
    open_zip(DATADIR)
    files = process_all(DATADIR)
    data = []
    for f in files:
        data += process_file(f)
    assert len(data) == 399
    for entry in data[:3]:
        assert type(entry["year"]) == int
        assert type(entry["month"]) == int
        assert type(entry["flights"]["domestic"]) == int
        assert len(entry["airport"]) == 3
        assert len(entry["courier"]) == 2
    assert data[-1]["airport"] == "ATL"
    assert data[-1]["flights"] == {'international': 108289, 'domestic': 701425}
    
    print "... success!"


if __name__ == "__main__":
    test()
