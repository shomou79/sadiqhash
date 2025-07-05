import hashlib
import os
import json

def hash_file(filename):
    with open(filename, "rb") as f:
        content = f.read()
        return hashlib.sha256(content).hexdigest()

def sign_file(filename):
    if not os.path.exists(filename):
        print("❌ File not found.")
        return
    digest = hash_file(filename)
    print(f"🔒 File hash: {digest}")
    with open(filename + ".sig", "w") as sig_file:
        sig_file.write(digest)

def verify_file(filename):
    sig_filename = filename + ".sig"
    if not os.path.exists(sig_filename):
        print("❌ Signature file not found.")
        return
    stored = open(sig_filename).read().strip()
    current = hash_file(filename)
    if current == stored:
        print("✅ File is valid. No changes detected.")
    else:
        print("⚠️ File has been modified or tampered with.")

def scan_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("❌ Folder not found.")
        return

    index = {}
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            filepath = os.path.join(root, file)
            # Skip signature or index files
            if filepath.endswith(".sig") or filepath.endswith("sadiqhash_index.json"):
                continue
            digest = hash_file(filepath)
            relative_path = os.path.relpath(filepath, folder_path)
            index[relative_path] = digest
            print(f"✅ Hashed: {relative_path} → {digest}")

    index_file = os.path.join(folder_path, "sadiqhash_index.json")
    with open(index_file, "w") as f:
        json.dump(index, f, indent=2)
    print(f"\n🗂️ All hashes saved in {index_file}")

def verify_folder(folder_path):
    index_file = os.path.join(folder_path, "sadiqhash_index.json")
    if not os.path.exists(index_file):
        print("❌ No index file found for verification.")
        return

    with open(index_file, "r") as f:
        stored_index = json.load(f)

    for rel_path, stored_hash in stored_index.items():
        full_path = os.path.join(folder_path, rel_path)
        if not os.path.exists(full_path):
            print(f"⚠️ MISSING: {rel_path}")
            continue
        current_hash = hash_file(full_path)
        if current_hash == stored_hash:
            print(f"✅ OK: {rel_path}")
        else:
            print(f"⚠️ CHANGED: {rel_path}")

print("=== SadiqHash ===")
print("1. Sign a file")
print("2. Verify a file")
print("3. Scan folder and sign all files")
print("4. Verify folder integrity")

choice = input("Choose (1, 2, 3 or 4): ")

if choice == "1":
    file = input("Enter file name: ")
    sign_file(file)

elif choice == "2":
    file = input("Enter file name: ")
    verify_file(file)

elif choice == "3":
    folder = input("Enter folder path to scan: ")
    scan_folder(folder)

elif choice == "4":
    folder = input("Enter folder path to verify: ")
    verify_folder(folder)

else:
    print("❌ Invalid choice.")
