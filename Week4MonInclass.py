#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Name: Siyi Guo
import requests
import json

# Problem 1
def download_and_save_json():
    url = "https://gbfs.citibikenyc.com/gbfs/en/station_status.json"
    response = requests.get(url)
    data = response.json()
    
    with open('citibike_data.txt', 'w') as file:
        json.dump(data, file)
    
    print("JSON data has been downloaded and saved as citibike_data.txt")


# In[2]:


# Problem 2
def display_first_five_rows():
    url = "https://gbfs.citibikenyc.com/gbfs/en/station_status.json"
    response = requests.get(url)
    data = response.json()
    
    station_statuses = data['data']['stations']
    
    print("First five rows of JSON data:")
    for row in station_statuses[:5]:
        print(row)


# In[3]:


# Problem 3
def get_last_modified_date():
    url = "https://gbfs.citibikenyc.com/gbfs/en/station_status.json"
    response = requests.get(url)
    
    last_modified = response.headers.get('Last-Modified', 'No Last-Modified Date Can Be Found')
    print("Last Modification Date:", last_modified)


# In[4]:


def main():
    download_and_save_json()
    display_first_five_rows()
    get_last_modified_date()

if __name__ == "__main__":
    main()

