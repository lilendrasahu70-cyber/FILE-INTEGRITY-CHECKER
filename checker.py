
import hashlib
import json
import os

HASH_FILE = "hashes.json"


# Function to calculate hash
def calculate_hash(filepath):

    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:

        while chunk := file.read(4096):

            sha256.update(chunk)

    return sha256.hexdigest()


# Save hashes of multiple files
def save_hashes(file_list):

    data = {}

    for filepath in file_list:

        if os.path.exists(filepath):

            file_hash = calculate_hash(filepath)

            data[filepath] = file_hash

            print(f"{filepath} hash saved.")

        else:

            print(f"{filepath} not found.")

    with open(HASH_FILE, "w") as file:

        json.dump(data, file, indent=4)

    print("\nAll hashes saved successfully.")


# Check integrity of multiple files
def check_integrity():

    if not os.path.exists(HASH_FILE):

        print("No hash database found.")
        return

    with open(HASH_FILE, "r") as file:

        saved_data = json.load(file)

    print("\n===== CHECKING FILE INTEGRITY =====\n")

    for filepath, old_hash in saved_data.items():

        if not os.path.exists(filepath):

            print(f"{filepath} : FILE DELETED")
            continue

        current_hash = calculate_hash(filepath)

        if old_hash == current_hash:

            print(f"{filepath} : SAFE")

        else:

            print(f"{filepath} : MODIFIED")


# Main Menu
print("\n===== FILE INTEGRITY CHECKER =====")

print("\n1. Save File Hashes")
print("2. Check File Integrity")

choice = input("\nEnter your choice: ")


# SAVE HASHES
if choice == "1":

    files = input(
        "\nEnter file names separated by comma:\n"
    )

    file_list = [file.strip() for file in files.split(",")]

    save_hashes(file_list)


# CHECK INTEGRITY
elif choice == "2":

    check_integrity()

else:

    print("\nInvalid choice")