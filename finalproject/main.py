#!/usr/bin/env python

"""Module contains functions to review, analyze and transform OpenStreetMap
Somerville, MA dataset.
"""


import json
import summarize
import tagauditor
import time
import transformer


OSM_FILE = 'data/somerville-xml.osm'


def main():
    """Run review analysis."""
    #Start naive timer
    start = time.clock()

    # Get breakdown of top level tags in XML.
    # Uncomment to run.
    # print summarize.get_top_level_tag_summary(OSM_FILE)

    # Get number of unique contributors from XML.
    # Uncomment to run.
    # print summarize.get_number_of_contributors(OSM_FILE)

    # Transform OSM XML data to JSON document file.
    # Uncomment to run.
    # transformer.process_map(OSM_FILE)

    # Validate K attributes
    # Uncomment to run.
    #print tagauditor.validate_k_attributes(OSM_FILE)

    #Get breakdown of K attributes to understand problems of data set
    data = tagauditor.get_k_value_breakdown(OSM_FILE)
    file_out = 'data/k-breakdown.json'
    
    with open(file_out, 'w') as f:
        json.dump(data, f, sort_keys=True,
                      indent=4, separators=(',', ': '))

    #Stop naive timer
    end = time.clock()
    print 'Execution time: ' + str(end - start)


if __name__ == '__main__':
    main()
