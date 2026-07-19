
# # # sentence = ('a clash of KINGS', 'a an the of')
# # # vowls = ['a', 'e', 'i', 'o', 'u']
# # # result = []
# # # def title_case(title, minor_words):
# # #     title = title.capitalize().split()
# # #     minor_words = minor_words.lower().split()
# # #     return ' '.join([word if word in minor_words else word.capitalize() for word in title])


# # # def title_case(title, minor_words=''):
# # #     minor = minor_words.lower().split()
# # #     words = title.lower().split()

# # #     result = []

# # #     for i, word in enumerate(words):
# # #         if i == 0 or word not in minor:
# # #             result.append(word.title())
# # #         else:
# # #             result.append(word)

# # #     return " ".join(result)


# # # print(title_case('a clash of KINGS', 'a an the of'))

# # # title_case('a clash of KINGS', 'a an the of')

# # # def factorial(n):
# # #     if n < 0 or n > 12:
# # #         raise ValueError("Input must be between 0 and 12")

# # #     if n == 0 or n == 1:
# # #         return 1

# # #     return n * factorial(n - 1)

# # # def factorial(n):
# # #     if n < 0 or n > 12:
# # #         raise ValueError
# # #     return 1 if n <= 1 else n*factorial(n-1)

# # # print(factorial(35))


# # # name_shuffler ='john McClane'
# # # result = []
# # # for value in name_shuffler.split():
# # #     result.append(value)

# # # a = result[0]
# # # b = result[1]
# # # result[0] = b
# # # result[1] = a
# # # # print(result)
# # # print(' '.join(result))

# # # def name_shuffler(str_):
# # #     return ' '.join(str_.split(' ')[::-1])


# # def expanded_form(num):
# #     result = []
    
# #     for index, digit in enumerate(str(num)):
# #         if digit != '0':
# #             zeros = len(str(num)) - index - 1
# #             result.append(digit + ('0' * zeros))

        
# #     return ' + '.join(result)

# # print(expanded_form(12), '10 + 2')
# # print(expanded_form(42), '40 + 2');
# # print(expanded_form(70304), '70000 + 300 + 4');

# # matrix = []
# # for i in range(1, 5+1):
# #     row_list = []
# #     for j in range(1, 5+1):
# #         row_list.append(i * j)
# #     matrix.append(row_list)
# # print(matrix)

# num = 9119

# # for i in str(digit):
# #     print(str(int(i)**2), end="")

# # def square_digits(num):
# #     result =""
# #     for i in str(num):
# #         result += str(int(i)**2)
# #     return int(result)

# # word = "2 years old"
# # for key, value in enumerate(word):
# #     if key == 0:
# #         print(int(value[key]))

# # arr1 = [1,2,3,4]
# # arr2 = [5,6,7,8]
# # p = sorted(set(arr1))
# # q = sorted(set(arr2))
# # print(p+q)
# # def merge_arrays(arr1, arr2):
# #     return sorted(set(arr1+arr2))

# import cv2
# import os

# video_path = "input.mp4"
# output_dir = "frames"

# os.makedirs(output_dir, exist_ok=True)

# cap = cv2.VideoCapture(video_path)

# # Original video FPS
# video_fps = cap.get(cv2.CAP_PROP_FPS)

# # Extract at 5 FPS
# target_fps = 5
# frame_interval = int(video_fps / target_fps)

# frame_count = 0
# saved_count = 0

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     if frame_count % frame_interval == 0:
#         output_path = os.path.join(
#             output_dir,
#             f"frame_{saved_count:06d}.jpg"
#         )
#         cv2.imwrite(output_path, frame)
#         saved_count += 1

#     frame_count += 1

# cap.release()

# print(f"Saved {saved_count} frames to '{output_dir}'")


# def to_binary_as_decimal(b):
#     if b == 0:
#         return 0

#     result = 0
#     place = 1

#     while b > 0:
#         result += (b % 2) * place
#         b //= 2
#         place *= 10

#     return result

# print(to_binary_as_decimal(5))

# from datetime import datetime
# def check_coupon(entered_code, correct_code, current_date: str, expiration_date: str) -> bool:
#     print(type(current_date))
    
#     if not all([entered_code, correct_code, current_date, expiration_date]):
#         return False
    
#     current_date = datetime.strptime(current_date, '%B %d, %Y').date()
#     expiration_date = datetime.strptime(expiration_date, '%B %d, %Y').date()
#     return  (entered_code == correct_code and type(entered_code) is type(correct_code) and current_date <= expiration_date)

# print(check_coupon(0,False,'September 5, 2014','September 25, 2014'))


# def round_to_next5(n):
#     if n % 5 == 0:
#         return n
#     else:
#         return n + (5 - n%5)
# print(round_to_next5(2))

def rain_amount(mm):
    print(type(mm))
    if (mm <= 40):
        return f"You need to give your plant {40 - mm } mm of water"
    else:
        return "Your plant has had more than enough water for today!"
    
print(rain_amount(39))