myDict = {
    'Fruits':'Apple',
    'Game': 'Chess',
    'person': {'Name': 'Suresh'}
}

print(myDict['Game'])
print(myDict['person']['Name'])
print(list(myDict.keys()))
print(myDict.items())
print(myDict.values())


update_Dict = {
    "Lovish": 'Friend',
    'shubham': 'Friend'
}

myDict.update(update_Dict)
print(myDict)

print(myDict.get('Fruits'))
