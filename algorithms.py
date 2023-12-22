import sys
from PyQt5.QtWidgets import QMessageBox, QAction, QLabel, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium 
import io
from geopy.geocoders import Nominatim
import osmnx as ox
from osmnx import routing

ox.config(log_console=True, use_cache=True)
locator = Nominatim(user_agent = "myapp")

def first_set(coord = [53.211936, 50.177311]) -> bytes:
        map = folium.Map(
            location=coord, zoom_start=13
        )
        data = io.BytesIO()
        popup1 = folium.LatLngPopup()
        map.add_child(popup1)
        map.save(data, close_file=False)
        return data
        

def get_coord(place: str):
    temp = locator.geocode(place)
    if temp:
        temp.point
        return [temp.latitude, temp.longitude]
    else: 
        return None
    
def calculating_time_and_length(graph, shortest_route) -> str:
    length = 0.0
    for i in range(len(shortest_route)-1):
        length += float(graph[shortest_route[i]][shortest_route[i+1]][0]['length'])
    text = "Расчетная дистанция: " + str(float("{:.2f}".format(length))) + "метров"
    
    time = 0.0
    for i in range(len(shortest_route)-1):
        time += float((graph[shortest_route[i]][shortest_route[i+1]][0]['travel_time']))
    text = "Расчетное время: "+ str(float("{:.2f}".format(time))) + "секунд\n" + text
    return text