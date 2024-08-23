# Find the factorial of the given number

"""
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
num = int(input("Enter num: "))

print(factorial(num))
"""

# By for loop

num = 4
Factorial = 1

for i in range(1, num+1):
    Factorial = Factorial * i

print(Factorial)