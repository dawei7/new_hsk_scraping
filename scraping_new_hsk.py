from bs4 import BeautifulSoup
import requests
import json
import csv

"""

#Some header settings to get everything in english, with US IP
headers = {'Accept-Language': 'en','X-FORWARDED-FOR': '2.21.184.0'}

counter = 1
my_dictionary = dict()

for i in range(1,10):
    url = f"https://pandarin.net/new-hsk/level{i}/" #loop through hsk pages
    
    #url request by given url paramter and soup conversion
    url_request = requests.get(url, headers=headers)
    soup = BeautifulSoup(url_request.text,features="html.parser")
    
    my_soup = soup.find_all('ul',attrs={'class': 'hsk-items --simplified'})[0].find_all('li')

    for item in my_soup:
        char = item.find_all('span')[0].text #first item is simplified
        pinyin = item.find_all('strong')[0].text #pinyin
        translation = item.find_all('p')[0].text.strip() #translation
        hsk_level = i #HSK level from loop

        my_dictionary[counter]=[char,pinyin,translation,hsk_level] #Dictionary of lists
        counter+= 1

print(len(my_dictionary))

# Serializing json 
json_object = json.dumps(my_dictionary) #All HSK characters


# Writing to dict_hsk.json
with open("dict_hsk.json", "w") as outfile:
    outfile.write(json_object)


"""

# Opening JSON file
with open('dict_hsk.json') as json_file:
    data = json.load(json_file)
  
    # Print the first 10 items
    counter = 0
    for key, item in data.items():
        print(f"{key}: {item}\n")
        counter+=1
        if counter>9: # Get first 10 items as a test
            break

#Save as a CSV-File

with open("dict_hsk.csv", 'w',newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(["id","char","pinyin","translation","hsk_level"]) #Header
    for key, item in data.items():
        writer.writerow([key,item[0],item[1],item[2],item[3]])