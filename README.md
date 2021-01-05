# Road-Construction-and-Navigation

## Installation
1. python -m venv venv
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py runserver

## Urls
1. Home : home/
2. Construct Road : add_road/
3. Destroy Road : del_road/
4. Reconstruct : reconstruct/
5. Navigate : navigate/
6. Destroy Network : clear/

## Description
- Represented road network as an undirected Weighted Graph & built an application to serve user requests for route navigation
- Optimized building time for network re-construction by applying Prim's Algorithm for identification of Minimum Spanning Tree
- Implemented Dijkstra’s Algorithm for calculations of the shortest route from source junction to destination entered by a user 
