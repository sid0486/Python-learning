
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("❌ Cannot divide by zero")


def average(nums):
    return sum(nums) / len(nums)

print("Average:", average([10, 20, 30]))


def find_max(nums):
    max_val = nums[0]
    for n in nums:
        print("Checking:", n)
        if n > max_val:
            max_val = n
    return max_val

print("Max:", find_max([3, 7, 2, 9, 1]))


import logging

logging.basicConfig(level=logging.INFO)

def divide(a, b):
    logging.info(f"Dividing {a} by {b}")
    return a / b

try:
    print(divide(10, 2))
except Exception as e:
    logging.error(e)


def withdraw(balance, amount):
    assert amount <= balance, "❌ Insufficient balance"
    return balance - amount

print("Remaining:", withdraw(1000, 500))


try:
    nums = [1, 2, 3]
    print(nums[5])
except IndexError:
    print("❌ Index out of range")