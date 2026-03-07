## Connecting two strings 
greeting = "Good morning, "
name = "Mukesh"
print(greeting+name)


## Slicing number 
a = "Apple"
print(a[0])
print(a[0:6])
print(a[-4:-1])
print(a[1:5:2])

## string are immutable
a[1] = "d"
print(a)

# string with function
a = "Apple"
b = "banana"
print(len(a))
print(a.endswith('le'))
print(a.startswith('Ap'))
print(a.count('p'))
print(b.capitalize())
print(b.upper())
print(a.lower())
print(b.title())
print(b.index('b'))
print(b.replace('banana', 'orange'))


## Practice
## Take name from user and print with goodafternoon
name = input("Enter name:")
print("Good Afternoon\t" + name)

## fill below letter
name = "kim"
date = '12-1-2026'
letter = '''Dear <|Name|> ,\n \tyou are selected! \n \t Date: <|date|>'''
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|date|>", date)
print(letter)


## find the double space from sentence
sentence = "Today i create one painting."
print(sentence.find("  "))

## replace 3 space problem with single space
sentence = "Today i   create one painting."
print(sentence.replace("   ", " "))