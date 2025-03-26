#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Name: Siyi Guo
# Problem 1

import csv, requests # Yes, you can use "," to import multiple packages at once
from openpyxl import Workbook
from datetime import datetime
#csv.field_size_limit(1000000)

station_names = {} # Let's first define a blank library, station name

with open('updated_station_name_id.txt', 'r') as file:
    reader = csv.DictReader(file, delimiter='\t')
    for row in reader:
        station_names[row['station_id']] = row['station_name']
# We read a tab seperated txt file. See Example 4-1 and 4-2 as references


bike_data = requests.get('https://gbfs.citibikenyc.com/gbfs/en/station_status.json')
data = bike_data.json()['data']['stations']
# We call the json file from the given website. See Example 5-1.
# "['data']['stations']" is a nested dictionary

station_data = [] #We start with an empty list
for station in data:
    station_id = station['station_id']
    station_name = station_names.get(station_id, 'Unknown Station') # Stations with no names get a defult name, Unknown Station.
    bikes = station.get('num_bikes_available', 0) # What does 0 do?! Think about it!
    e_bikes = station.get('num_ebikes_available', 0)
    scooters = station.get('num_scooters_available', 0)
    station_data.append((station_name, bikes, e_bikes, scooters))
# See Example 5-1 - Example 5-3.

station_data = sorted(station_data)

for station, bikecount, ebikecount, scootercount in station_data[:10]:
    print(f"{station}: {bikecount}, {ebikecount}, {scootercount}") #This is called an f-string works exactly like a regular print function. Try it!


# In[10]:


# Problem 2
# Note: We proceed by using the station_data created in Part 1.

wb = Workbook() # Using the Workbook function of openpyxl library, we creates a new Excel file (called a workbook)
ws = wb.active # We call an active Excel sheet 
ws.append(["Station Name", "Bikes", "EBikes", "Scooters"])  # We provide the column names, the headers. See Example 4-5 as a reference

for row in station_data:
    ws.append(row)  
# This for loop will iterate over station_data and insert data as rows in the Excel sheet.
# This part is an application of Example 4-5 

filename = "Citibike-" + datetime.now().strftime('%Y-%m-%d') + ".xlsx" # Here, we define the filename.
# filename = f"Citibike-{datetime.now().strftime('%???-%???-%???')}.xlsx" # Those who are used to the f-string may use this one!

wb.save("Citibike-2025-03-26-09-35.xlsx”) 
# Usig the save function, the filename we created is given to the Excel file. After this, we have a physical Excel file in our folder. Please check!
# This part is from Example 7-5


# In[ ]:




