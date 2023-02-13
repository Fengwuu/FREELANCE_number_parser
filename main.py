import requests
from bs4 import BeautifulSoup
import re

print('Hello! Here you can scan indian phone numbers. All what I need - city and number.')
a = 'Delhi'
file = open("numbers.txt", "w")
for x in range (7000, 7100): # numbers
    r = requests.get('https://mobilenumbertracker.com/mobilenumberlocation/'+str(x))

    soup = BeautifulSoup(r.text, 'html.parser')
    divs = soup.find_all('p') # information in p html tag
    words = re.findall(r'Delhi', str(divs)) # sorting by city
    
    try:
        print('City: ' + words[0] + ' Number: ' + str(x)) 
        file.write("Number: "  + str(x) +  ", City: " + words[0] + '\n')
        
    except:
        print (str(x) + ' Not found in this city!')
      
file.close()
print('Program finished! Look at numbers.txt in this directory. Bye-Bye')