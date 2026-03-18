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





print("hello")

