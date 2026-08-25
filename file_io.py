f = open('sample.txt', 'r')
data = f.read()
print(data)

f = open('sample.txt', 'w')
p = f.write("let's eat togther.")
print(p)
f.close()

f = open('sample.txt', 'r')
p = f.readline(5)
print(p)
f.close()

f = open('sample.txt')
t = f.readlines()
print(t)

t = f.readlines()
print(t)

f.close()

f = open('another.txt', 'w')
f.write("let's play togther.")
f.close()

f = open('another.txt', 'a')
f.write("I am appending.")
f.close()

f = open('find_word.txt', 'rb')
text = f.read()
print(text)
f.close

f = open('sample.txt', 'r')
i = 0
while True:
    i +=1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of student 1 in Maths:   {m1*2}")
    print(f"Marks of student 2 in English: {m2*2}")
    print(f"Marks of student 3 in Biology: {m3*2}")
    print(line)
    
f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close() 
    
f = open('myfile.txt', 'w')
lines = ['line 12', 'line 22', 'line 32']
for line in lines:
    f.writelines(line +'\n')
f.close() 


