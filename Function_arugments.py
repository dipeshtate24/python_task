def average(a, b, c=1):
    print("The average is", (a+b+c)/2)

average(9, 6)

def average(*number):
    sum = 0
    for i in number:
        sum += i
    print('Average is', sum/len(number))

average(5, 6, 7, 1)


def name(**name):
    print("Hello,",name['fname'], name['mname'], name['lname'])

name(mname="hari", fname="sinchan", lname='Nohara' )