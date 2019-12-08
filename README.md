# Squirrel Tracker_Group_sq_jc5298_zw2633

One Paragraph of project description goes here

## Background 
Eccentric billionaire Joffrey Hosencratz just purchased the web development company you work for. You’ve met him once in an elevator and he was impressed with your skill in developing web applications with the Django framework. He also relayed that his most recent trip to Sedona, AZ has left him in a bit of trouble. See, he fancies the show Rick and Morty and a particular scene coupled with a traumatic childhood squirrel experience and a bad crystal bath experience in Sedona as left him wanting. 

## Overview 

Squirrel Tracker: This is a web application with the Django framework to visualize the sighting data of squirrels in Central Park 

## Data Resource 
The data is collected from 2018 Central Park Squirrel Census and is legally added, updated and viewed in our Squirrel Tracker Web App

```
Import the data 
$ python manage.py import_squirrel_data /path/to/file.csv 
Export the data 
$ python manage.py export_squirrel_data /path/to/file.csv
```

## Implement Description 

Part1: MAP

A view that shows a map that displays the location of the squirrel sightings on an OpenStreets map.
```
Located at: /map
Methods Supported: GET
Reference: Use Leafletjs library for plotting 
```
A view that lists all squirrel sightings with links to edit each

Part2:Sightings

A view that lists all squirrel sightings with links to edit each
```
Located at: /sightings
Methods Supported: GET
```

A view to update a particular sighting
```
Located at: /sightings/<unique-squirrel-id>
Methods Supported: GET & POST
```

A view to create a new sighting
```
Located at: /sightings/add
Methods Supported: GET & POST
```

A view with general stats about the sightings
```
Located at: /sightings/stats
Method: GET
```
## Contributor
```
Group Name: Project Group sq, Section 2
UNI for group members: jc5298, zw2633
Link to server running app: https://radiant-indexer-255500.appspot.com

```
## Other 
For some reasons, The deployments was failed by processed, but we created a copy of Github including all original file without any update, and the deployments was succeeded by Google App Engine 



