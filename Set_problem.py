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
