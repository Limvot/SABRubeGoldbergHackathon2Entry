import json
import requests
#import urllib2

url = 'http://restcountries.eu/rest/v1/'
data = requests.get(url).json()
firstLetter = {}
countryCode = {} 
for i in data:
    letter = i['name'][0]
    if letter not in firstLetter:
        firstLetter[letter] = [i]
    else:
        firstLetter[letter].append(i)
    cCode = i['callingCodes'][0]
    countryCode[cCode] = i

underscoreCountry = firstLetter['A'][1]
firstLetter['_']  = [underscoreCountry]
countryCode[underscoreCountry['callingCodes'][0]] = underscoreCountry

def encode(toEncode):
    numList = "" 
    for i in toEncode.upper():
        numList = numList + firstLetter[i][0]['callingCodes'][0]
    return numList

def splitStr(tosplit, interval):
    i = 0
    strList = []
    while(i+interval <= len(tosplit)):
        strList.append(tosplit[i:i+interval]);
        i += interval
    return strList

def decode(toDecode):
    output = ""
    for i in splitStr(toDecode, 3):
        if countryCode[i] == underscoreCountry:
            output += "_"
        else:
            output += countryCode[i]['name'][0]
    return output
    
#for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    #if i in firstLetter:
        #print(firstLetter[i][0]['name'])
    #else:
        #print(i + " has no country!")

print(encode("HELLO"))
print(decode(encode("HELLO")))


