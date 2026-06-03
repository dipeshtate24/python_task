def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('Is 415-555-4242 a phone number?', is_phone_number('415-555-4242'))
print(is_phone_number('415-555-4242'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    segment = message[i:i+12]
    if is_phone_number(segment):
        print('Phone number found: ' + segment)
print('Done')


import re
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')  # This regex has no groups.
print(pattern.findall('Cell: 415-555-9999 Work: 212-555-0000'))


import re
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')  # This regex has no groups.
print(pattern.findall('Cell: 415-555-9999 Work: 212-555-0000'))

pattern = re.compile(r'[aeiou]')
print(pattern.findall('RoboCop eat baby food'))

pattern = re.compile(r'\d+\s\w+')
print(pattern.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans,' \
' 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

at_re = re.compile(r'.at')
print(at_re.findall('The cat in the hat sat on the flat mat.'))

pattern = re.compile(r'42!?')
print(pattern.search('42!'))

pattern = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
match1 =  pattern.search('My number is 415-555-4242')
print(match1.group())

consonant_pattern = re.compile(r'[^aeiouAEIOU]')
print(consonant_pattern.findall('RoboCop eats BABY FOOD.'))

agent_pattern = re.compile(r'Agent \w+')
print(agent_pattern.sub('CENSORED', 'Agent Alice contacted Agent Bob'))


pattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?  # Separator
    \d{3}  # First three digits
    (\s|-|\.)  # Separator
    \d{4}  # Last four digits
    (\s*(ext|x|ext\.)\s*\d{2,5})?  # Extension
    )''', re.VERBOSE)


pattern = "was"

text =''' it was strong typical cyclone in the south.'''

result = re.search(pattern, text)
print(result)

pattern = r"[A-Z]yclone"

text ='''it was strong typical Cyclone in the south'''

matches = re.finditer(pattern, text)

for match in matches:
    print(match)
    
