a = {1, 3, 4, 2, 1}
print(type(a))
print(a)


b = set()
b.add(4)
b.add(5)

print(b)

print(b.add({4:5}))

print(len(b))

print(b.pop())


Dict_Book ={
  "Pankha": "Fan",
  "Dabba": "Box"

}

print('Option are', Dict_Book.keys())
a = input('Enter Hindi word\n')
# print("The meaning of your word is:", Dict_Book[a])
print("The meaning of your word is:", Dict_Book.get(a))

s= {18}
print(type(int(s))) # Error is int() argument must be a string, a bytes-like object or a real number, not 'set'
print(type(str(s)))


s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))

s = {}
print(type(s))

Dict_language = {}
Name = input("Enter your name:")
language = input("Enter your favourite langauge:")
Dict_language[Name] = language
Name = input("Enter your name:")
language = input("Enter your favourite langauge:")
Dict_language[Name] = language
print(Dict_language)

s = {8, 7, 12, "Viky", [1,2]} # Error is unhashable type: 'list'
print(s[1])
