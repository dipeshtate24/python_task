with open('another.txt', 'r') as f:
    a = f.read()

with open('another.txt', 'w') as f:
    a = f.write('I like mangoes.')

print(a)


with open('another.txt', 'r') as f:
    a = f.readline(5)

with open('another.txt', 'a') as f:
    a = f.write('i am appending')

print(a)

f=open('find_word.txt')
a = f.read()
if "Twinkle" in a:
    print("Given word in present in the file.")
else:
    print("Given word not present in the file.")

f.close()

new_number = 78

with open('number.txt','r') as f:
    a = int(f.read())
if new_number > 0 and new_number > a :
    with open('number.txt', 'w') as f:
        f.write(str(new_number))


for i in range(2, 21):
    with open(f'Mulitiplication_of_{i}.txt', 'w') as f:
        for j in range(1,11):
            f.write(f"{i}*{j}={i * j}\n")
    break

words = ['donkey', 'kaddu', 'mote']


with open('word.txt') as f:
    content = f.read()

for word in words:
    content = content.replace(word, f"{'#' * len(word)}")

    with open('word.txt', 'w') as f:
        f.write(content)


with open('log.txt') as f:
    content = f.read()

word = 'python'
if word in content.lower():
    print("python is present.")
else:
    print("python is not present.")

word = 'python'
content = True
i = 1
with open('log.txt') as f:
    while content:
        content = f.readline()

        if word in content.lower():
            print(f"python is present in line {i}")
        i += 1
        

with open('this.txt') as f:
    content = f.read()

with open('copy.txt', 'w') as f:
    f.write(content)

with open('this.txt') as f:
    content1 = f.read()

with open('copy.txt') as f:
    content2 = f.read()

if content1 == content2:
    print("Both file content is identical.")
else:
    print("Both file content is identical.")

filename = "clean_file.txt"

with open(filename, 'w') as f:
    f.write("")

import os 
oldname = "clean_file2.txt"
new_filename = "renamed_by_python.txt"
with open(oldname) as f:
     content = f.read()

with open(new_filename, 'w') as f:
     f.write(content)

os.remove(oldname)
