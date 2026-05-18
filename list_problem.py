a = [1, 2, 4, 56, 6]
print(a[0])

a[3] = 5
print(a)

a.sort()
print(a)

a.reverse()
print(a)

print(a[::-1])

a.append(8)
print(a)

a.remove(56)
print(a)

a.pop()
print(a)

a.insert(3, 88)
print(a)

fruits = ['apple', 'banana', 'apple', 'orange']
print(fruits.count('apple'))


lst = [i*i for i in range(10)]
print(lst)

lst = [i*i for i in range(10) if i % 2 == 0]
print(lst)