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
* Size of JSON file: 150.7 MB

Note: A sample of the XML OSM data is available: finalproject/data/sample.osm

#####Reason for Selection
My two younger brothers attend Tufts University in Somerville, MA. I often visit and thought the dense urban neighborhood would be interesting to review.

#####XML Data Overview
Note: I wrote 4 modules to assist in data review and transformation:
* streetauditor.py
* summarize.py
* tagauditor.py
* transformer.py

######Tag element "K" attribute analysis
I wrote a recursive algorithm to parse compund k attribute values (multple words separated by a ":") found in "tag" elements.

This breakdown provides an interesting look into the type and frequency of data provided in the "tag" element.

Note: the "root" property is the frequency count for the parent key.

See the k attribute analysis file in: finalprojects/data/k-breakdown.json

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

#####Top 5 Contributing Users
Query:
```
db.somer.aggregate([
    { "$group" : { "_id" : "$created.user", "total" : { "$sum" : 1 } } },
    { "$sort" : { "total" : -1 } },
    { "$limit" : 5 }
])
```
Result:

| User              | Count    |
| ----------------- | -------- |
| crschmidt         |  370001  |
| jremillard-massgis|  93258   |
| OceanVortex       |  83486   |
| ingalls_imports   |  29064   |
| morganwahl        |  27541   |

######Top 10 amenity types:
MongoDB Query:
```
db.somer.aggregate([
    { "$group" : { "_id" : "$amenity", "total" : { "$sum" : 1 } } },
    { "$sort" : { "total" : -1 } },
    { "$limit" : 10 }
])
```
Result:

| Amenity          | Count    |
| ---------------- | -------- |
| null             | 689454   |
| parking          | 660      |
| bench            | 415      |
| restaurant       | 268      |
| school           | 199      |
| place_of_worship | 184      |
| bicycle_parking  | 166      |
| hydrant          | 124      |
| library          | 110      |
| cafe"            | 85       |

######Top 10 Cuisine Types:
MongoDB Query:
```
db.somer.aggregate([
    { "$group" : { "_id" : "$cuisine", "total" : { "$sum" : 1 } } },
    { "$sort" : { "total" : -1 } },
    { "$limit" : 10 }
])
```
Results:

| Cuisine     | Count |
| ----------- | ----- |
| pizza       | 30    |
| chinese     | 22    |
| mexican     | 19    |
| american    | 18    |
| italian     | 16    |
| sandwich    | 16    |
| indian      | 15    |
| coffee_shop | 14    |
| burger      | 11    |
| thai        | 8     |

####Problems encountered in map
#####Problem #1: Street Names
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

###Task 4. Additional Ideas

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