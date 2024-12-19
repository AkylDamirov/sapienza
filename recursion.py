# Write a recursive function to compute the factorial of a number.
def factorial(number):
    if number==0:
        return 1
    return number * factorial(number-1)

# print(factorial(5))

#fibonacci
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-1) + fib(n-2)

# print(fib(5))

#check if its palindrome
def palindrome(s):
    if len(s)<=1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])

print(palindrome('s'))





