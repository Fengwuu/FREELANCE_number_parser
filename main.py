import requests
from bs4 import BeautifulSoup
import re

print('Hello! Here you can scan indian phone numbers. All what I need - city and number.')

city = input('Enter Indian city, that you need.') #asking for some information
file = open("numbers.txt", "w")
first_number = int(input('Input first number, that you need (0+)'))
last_number = int(input('Input last number, that you need (9999-)'))

for x in range (first_number, last_number+1): # numbers, +1 because range decrement last integer.
    r = requests.get('https://mobilenumbertracker.com/mobilenumberlocation/'+str(x))

    soup = BeautifulSoup(r.text, 'html.parser')

    divs = soup.find_all('p') # information in p html tag
    words = re.findall(r'{}'.format(city), str(divs)) # sorting by city
    
    try:
        print('City: ' + words[0] + ' Number: ' + str(x)) # try is required, necessary because there are numbers that do not...
        file.write("Number: "  + str(x) +  ", City: " + words[0] + '\n')  #...  allow tracking information, which breaks the script
    except:
        print (str(x) + ' Not found in this city!')
      

file.close()
print('Program finished! Look at numbers.txt in this directory. Bye-Bye')