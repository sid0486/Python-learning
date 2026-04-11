def greet():
    print("hello")

greet()


# . Function with Parameters:
def greet(name):
    print(f'hello {name}')

greet("Sid")

def add(a, b):
    return a + b

result = add(2, 3)
print(result)


def add(a, b):
    print(a + b)   # ❌ not reusable

def add(a, b):
    return a + b   # ✅ reusable


# DEFAULT ARGUMENTS : if no value given default used 

def greet(name="User"):
    print(f"Hello {name}")

greet()        # User
greet("Sid")   # Sid


# KEYWORD ARGUMENTS : Pass arguments by name (order doesn’t matter)

def student(name, age):
    print(name, age)

student(age=21, name="Sid")


# POSITIONAL ARGUMENTS : order matter 
def student (name ,age):
    print(name ,age)

student("sid",21)


# *ARGS (MULTIPLE VALUES):
def total (*nums):
    return sum(nums)
print(total(1,2,3,4,5))


# **kwargs (KEY-VALUE DATA):Accept dictionary-like input

def info(**data):
    print(data)

info (name = "sid",age = 21)


# nested function :
def outer():
    def inner():
        print("Inner")
    inner()

outer()

# VARIABLE SCOPE (IMPORTANT)  : Local vs Global

x = 10   # global

def test():
    x = 5   # local
    print(x)

test()
print(x)


# RECURSION (FUNCTION CALLS ITSELF) :

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))

# LAMBDA FUNCTION:
square = lambda x: x*x
print(square(5))

# HIGHER ORDER FUNCTION (ADVANCED) :Function takes another function
def apply(func, value):
    return func(value)

print(apply(lambda x: x*x, 5))














