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




number = int(input("Enter number:"))

try :
    number = int(input("Enter number:"))
    print(f"You entered: {number}")

except ValueError:
    print("That's not a number!!")



try :
    number = int(input("Enter number :"))
    result = 100 / number
    print(result)
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception as e :
    print(f"something unexpected : {e}")


try :
    number = int(input("Enter number :"))
    result = 100 / number
except ZeroDivisionError :
    print("Can't divide by zero")
except ValueError:
    print("That's not a number!")
else :
    print(f"Result : {result}")
finally :
    print("Program finished")



def check_age(age: int) -> int:
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150 :
        raise ValueError("Age is unrealistically high !")
    return age

try :
    check_age(-5)
except ValueError as e :
    print(f"Error : {e}")


















































