def divide(a,b):
    try:
        result = a/b
        return result

    except ZeroDivisionError :
        return "Error : Cannot divide by zero"

    except TypeError :
        return "Error : Invalid input type "

    finally :
        print("Execution completed")

print(divide(10,2))
print(divide(10,0))































































