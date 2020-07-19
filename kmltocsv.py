# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 12:38:13 2017
@author: Ana-Maria.Mocanu
"""

from bs4 import BeautifulSoup
import csv
import os

def process_coordinate_string(list_test):
    """
    Take the coordinate string from the KML file, and break it up into [Lat,Lon,Lat,Lon...] for a CSV row and other columns
    """
    ret = []
    ret.append(list_test[0]) # Name 
    coord = list_test[1].split(",") 
    ret.append(coord[1]) # Lat
    ret.append(coord[0]) # Long

    return ret

def load(path1, path2):
    """
    Open the KML. Read the KML. Open a CSV file. Process a coordinate string to be a CSV row.
    """
    with open(path1, encoding='utf8') as f:
        s = BeautifulSoup(f, 'xml')
        with open(path2, 'w', newline='', encoding='utf8') as csvfile:
            #Define the headers
            header = ['Name', 'Latitude', 'Longitude']
            writer = csv.writer(csvfile)
        
            writer.writerow(header)
            total_list = []
            for placemark in s.find_all('Placemark'):
                #added conditions for no values in child tags
                name = placemark.find('name').string  \
                       if placemark.find('name') is not None  \
                       else 'None'
                coords = placemark.find('coordinates').string \
                         if placemark.find('coordinates') is not None  \
                         else 'None'
                #create a list for and append values for each row
                list_test = []
                list_test.extend((name.string, coords.string))
                #print(list_test)
                total_list.append(process_coordinate_string(list_test))
                #print(coords.string)
                #print(total_list)
            writer.writerows(total_list)