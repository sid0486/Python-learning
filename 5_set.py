"""
set_operations.py

Basic set operations in Python:
- add / remove
- union
- intersection
- difference
- duplicate removal
"""


def basic_operations():
    s = {1, 2, 3}

    s.add(4)
    s.remove(2)

    print("After add/remove:", s)


def set_operations():
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    print("Union:", a | b)
    print("Intersection:", a & b)
    print("Difference (a - b):", a - b)


def remove_duplicates():
    nums = [1, 2, 2, 3, 4, 4, 5]
    unique = list(set(nums))
    print("Unique values:", unique)



def main():
    print("=== Basic Operations ===")
    basic_operations()

    print("\n=== Set Operations ===")
    set_operations()

    print("\n=== Remove Duplicates ===")
    remove_duplicates()



if __name__ == "__main__":
    main()