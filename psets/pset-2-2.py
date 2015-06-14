#!/usr/bin/env python
# -*- coding: utf-8 -*-

# All your changes should be in the 'extract_airports' function
# It should return a list of airport codes, excluding any combinations like "All"


from bs4 import BeautifulSoup


HTML_PAGE = "options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        soup = BeautifulSoup(html)

        airport_select = soup.find(id="AirportList")

        for airport in airport_select.contents:
            if airport != "\n":
                val = airport["value"]
                if len(val) < 4 and val != "All":
                    data.append(val)

    return data


def test():
    data = extract_airports(HTML_PAGE)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data


if __name__ == '__main__':
    test()
