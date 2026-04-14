
square = lambda x: x * x
print("Square:", square(5))


add = lambda a, b: a + b
print("Add:", add(3, 4))


mul = lambda a, b, c: a * b * c
print("Multiply:", mul(2, 3, 4))


nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
print("Squares List:", squares)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci:", fibonacci(6))

fact_lambda = lambda n: 1 if n == 1 else n * fact_lambda(n - 1)
print("Lambda Factorial:", fact_lambda(5))


fib_lambda = lambda n: n if n <= 1 else fib_lambda(n-1) + fib_lambda(n-2)
print("Lambda Fibonacci:", fib_lambda(6))


def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

print("Sum 1 to n:", sum_n(5))

def reverse_string(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])

print("Reverse:", reverse_string("Python"))


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print("Is Palindrome:", is_palindrome("madam"))