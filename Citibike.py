#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import zipfile
import urllib.request
import os

def download_data(url, save_path):
    try:
        urllib.request.urlretrieve(url, save_path)
        print(f"File downloaded to {save_path}")
        
        with zipfile.ZipFile(save_path, 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(save_path))
        print(f"File extracted to {os.path.dirname(save_path)}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

def read_data(file_path):
    return pd.read_csv(file_path)

def count_rides_per_station(trip_data):
    return trip_data['start_station_name'].value_counts().sort_index()

def format_output(ride_counts):
    output = []
    for station, count in ride_counts.items():
        output.append(f"{station}: {count}")
    return output

def main():
    url = 'https://s3.amazonaws.com/tripdata/JC-202401-citibike-tripdata.csv.zip'
    
    save_path = 'JC-202401-citibike-tripdata.csv.zip'
    
    download_data(url, save_path)
    
    csv_file_path = os.path.join(os.path.dirname(save_path), 'JC-202401-citibike-tripdata.csv')
    
    trip_data = read_data(csv_file_path)
    
    ride_counts = count_rides_per_station(trip_data)
    
    output = format_output(ride_counts)
    
    for line in output:
        print(line)

if __name__ == "__main__":
    main()


# In[ ]:




