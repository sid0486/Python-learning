from file_manager import *

while True:
    print("\n===== CLI File Manager =====")
    print("1. Create File")
    print("2. Write to File")
    print("3. Read File")
    print("4. Delete File")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter file name: ")
        create_file(name)

    elif choice == "2":
        name = input("Enter file name: ")
        content = input("Enter content: ")
        write_file(name, content)

    elif choice == "3":
        name = input("Enter file name: ")
        read_file(name)

    elif choice == "4":
        name = input("Enter file name: ")
        delete_file(name)

    elif choice == "5":
        print("👋 Exiting...")
        break

    else:
        print("❌ Invalid choice")