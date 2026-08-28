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


s1 = {1, 2, 4, 5, 6}
s2 ={3, 5, 6}
print(s1.union(s2))
s1.update(s2)
print(s1, s2)

city1 = {"Tokyo", "Madrid", "Dehli", "Berlin"}
city2 = {"Tokyo", "Soul", "Madrid"}
cities = city1.intersection(city2)
print(cities)
city1.intersection_update(city2)
print(city1)
cities1 = city1.difference(city2)
print(cities1)
print(city1.isdisjoint(city2))
print(city1.issuperset(city2))
print(city1.issubset(city2))
