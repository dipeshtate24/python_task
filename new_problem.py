import time 

t = time.strftime('%H:%M:%S')
hours = int(time.strftime('%H'))

if hours > 0 and hours < 12:
    print("Good Morning")
elif hours > 12 and hours < 5:
    print("Good Afternoon") 
elif hours > 5 and hours < 8:
    print("Good Evening")
else:
    print("Good Night")