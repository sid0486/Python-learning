

# 1. Write to file (creates file if not exists)
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Hello Siddhi 🚀\n")
    file.write("Learning File Handling\n")


# 2. Append data
with open("data.txt", "a", encoding="utf-8") as file:
    file.write("New line added\n")


# 3. Read full file
with open("data.txt", "r", encoding="utf-8") as file:
    print("📖 Full Content:\n")
    print(file.read())


# 4. Read line by line
print("\n📌 Line by Line:")
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())


# 5. Read as list
with open("data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print("\n📋 List Output:", lines)


# 6. Error Handling
try:
    with open("not_exist.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("❌ File not found")