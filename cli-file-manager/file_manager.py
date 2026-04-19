def create_file(filename):
    try:
        with open(filename, "w") as f:
            print(f"✅ File '{filename}' created successfully")
    except Exception as e:
        print(f"❌ Error: {e}")


def write_file(filename, content):
    try:
        with open(filename, "a") as f:
            f.write(content + "\n")
            print("✅ Content written successfully")
    except Exception as e:
        print(f"❌ Error: {e}")


def read_file(filename):
    try:
        with open(filename, "r") as f:
            print("\n📄 File Content:\n")
            print(f.read())
    except FileNotFoundError:
        print("❌ File not found")
    except Exception as e:
        print(f"❌ Error: {e}")


def delete_file(filename):
    import os
    try:
        os.remove(filename)
        print("🗑️ File deleted successfully")
    except FileNotFoundError:
        print("❌ File not found")
    except Exception as e:
        print(f"❌ Error: {e}")