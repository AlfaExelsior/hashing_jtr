import hashlib

def hash_string(input_string, hash_function='sha256'):
    hash_obj = getattr(hashlib, hash_function)()
    hash_obj.update(input_string.encode('utf-8'))
    return hash_obj.hexdigest()

if __name__ == "__main__":
    user_input = input("Enter a string to hash: ")
    print(f"SHA-256 Hash: {hash_string(user_input)}")
