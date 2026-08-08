username = 'Marry'
password = 'Swordfish'

if username == 'Marry':
    print("Hello, Marry")
    if password == "Swordfish":
        print("Access granted.")
    else:
        print("Wrong Password.")
else:
    print("username is not match.")


print("Enter GB or TB for advertised unit:")
unit = input('>')

if unit == 'TB' or unit == 'tb':
    discrepancy = 1000000000 /1099511627776

elif unit == 'GB' or unit == 'gb':
    discrepancy = 100000000/ 1073741824

print('Enter the advertised capcity:')
advertised_capcity = input('>')
advertised_capcity = float(advertised_capcity)

real_capcity = str(round(advertised_capcity * discrepancy , 2))
print('The actual capcity is'+ real_capcity + '' + unit)
