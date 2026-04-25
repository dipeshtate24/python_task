
# st = "Samosa is good"
# coding = True
# if coding:
#     if len(st) > 3:
#         st = st[1:] + st[0]
#         print(st)

# else:
#     pass

    # st = input("Enter message > ")
    # words = st.split(' ')
    # coding = True
    # if coding:
    #     new_word = []
    #     for word in words:
    #         if len(word) > 3:
    #             r1 ="uws"
    #             r2 = "igi"
    #             stnew = r1 + word[1:] + word[0] + r2
    #             new_word.append(stnew)

    #         else:
    #             new_word.append(word[::-1])
    #     print(" ".join(new_word))

import random
import string

# st = input("Enter message > ")
# words = st.split(' ')
# coding = input("1 for coding and 0 for decoding > ")
# if coding == '1':
#     new_word = []
#     for word in words:
#         if len(word) > 3:
#             r1 = chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))
#             r2 = chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))
#             stnew = r1 + word[1:] + word[0] + r2
#             new_word.append(stnew)

#         else:
#             new_word.append(word[::-1])
#     print(" ".join(new_word))

# elif coding == '0':
#     nword=[]
#     for word in words:
#         if len(word) > 3:
#             stnew = word[3:-3]
#             stnew = stnew[-1] + stnew[:-1]
#             nword.append(stnew)
#         else:
#             nword.append(word[::-1])
#     print(" ".join(nword))

# else:
#     print('Enter value from 1 or 0')



st = input("Enter message > ")
words = st.split(' ')
coding = input("1 for coding and 0 for decoding > ")
if coding == '1':
    new_word = []
    for word in words:
        if len(word) > 3:
            r1 = ''.join(random.choices(string.ascii_lowercase, k = 3))
            r2 = ''.join(random.choices(string.ascii_lowercase, k = 3))
            stnew = r1 + word[1:] + word[0] + r2
            new_word.append(stnew)

        else:
            new_word.append(word[::-1])
    print(" ".join(new_word))

elif coding == '0':
    nword=[]
    for word in words:
        if len(word) > 3:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nword.append(stnew)
        else:
            nword.append(word[::-1])
    print(" ".join(nword))

else:
    print('Enter value from 1 or 0')