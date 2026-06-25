import functools
import time

@functools.lru_cache(maxsize=None)
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1)+fib(n-2)

# print(fib(20))

def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("Done for 20")

print(fx(2))
print("Done for 2")

print(fx(6))
print("Done for 6")