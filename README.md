Data Wrangling with MongoDB
=====================
###Nanodegree Project
School: Udacity

Program: Data Analyst Nanodegree

Project #2

Supporting course(s):

[Data Wrangling with MongoDB](https://www.udacity.com/course/viewer#!/c-ud032)

###Project Overview
You will choose any area of the world in https://www.openstreetmap.org and use data munging techniques, such as assessing the quality of the data for validity, accuracy, completeness, consistency and uniformity, to clean the OpenStreetMap data for a part of the world that you care about.

###Project Depencies
Python 2.7x

###Final Project Review

###Task 1: Lesson 6 Programming Exercises
Lesson 6 programming exercise solutions can be found in the lessons directory.

###Task 2: Process Dataset
Map area: Somerville, Massachusetts, United States

OpenStreetMap: [View Map](https://www.openstreetmap.org/relation/1933746#map=14/42.3954/-71.1037)

Download source: [Overpass API](http://overpass-api.de/api/map?bbox=-71.1429,42.3681,-71.0645,42.4228)

###Task 3: Document Findings
####Data Overview
#####File sizes
* Size of XML file: 133.4 MB
* Size of JSON file: 150.4 MB

#####XML Data Overview
######Top Level XML Elements
Module: summarize.py

Code:
```
summarize.get_top_level_tag_summary(OSM_FILE)
```
Results:
```
{
    'node': 596989,
    'member': 10171,
    'nd': 714378,
    'tag': 227679,
    'bounds': 1,
    'note': 1,
    'meta': 1,
    'relation': 534,
    'way': 95546,
    'osm': 1
}
```

######Number of Unique Contributing Users
Module: summarize.py

Code:
```
summarize.get_number_of_contributors(OSM_FILE)
```
Result: 577

#####MongoDB Data Overview
######Number of documents uploaded
MongoDB Query:
```
db.somer.count()
```
Result: 692535

######Number of nodes
MongoDB Query:
```
db.somer.find( { 'type': 'node' } ).count()
```
Result: 596878

######Number of ways
MongoDB Query:
```
db.somer.find( { 'type': 'way' } ).count()
```
Result: 95532



######Top 10 establishment types:
  * Cafes:
  * Restaurants:
  * Bars:



####Problems encountered in map
#####Street Names
Inconsistent abbreviations for streetnames exist in the data set.

######Examples:
For "Street" the following abbreviations were used:
* "St"
* "st"
* "ST"
* "St."

For "Avenue" the following abbreviations were used:
* "ave"
* "Ave."
* "Ave"

To resolve these inconsistencies I utilized the module streetauditor.py to normalize street names.


#####Inconsistent Postal Codes


#####Incorrect Postal Codes





###Task 4. Additional Ideas


#####Top 5 Appearing Establishments
Query:
```

```
Result:

#####Top Contributing User
Query:
```

```
Result:

#####Mean Number of Contributions Per User
Query:
```

```
Result:

#####Median Number of Contributions Per User
Query:
```

```
Result:


###Resources
All resources used/referenced are listed in the file resources.txt.