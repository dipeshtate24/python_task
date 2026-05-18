def fatorical(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * fatorical(n-1)

print(fatorical(5))

def fibonacci(n):
    if n == 0:      
        return 0
    if n == 1:      
        return 1
    else:          
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(5):
    print(fibonacci(i), end=" ")