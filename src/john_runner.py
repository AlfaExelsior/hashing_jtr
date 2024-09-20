import hashlib
import subprocess

def create_password_file(filename="passwords.txt"):
    passwords = ["password123", "letmein", "querty"]
    salt = "$1$xyz$"

    with open(filename, "w") as file:
        for password in passwords:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            file.write(f"{hashed_password}\n")
    
    print(f"Password hashes written to {filename}")

def run_john(filename="passwords.txt"):
    try:
        process = subprocess.Popen(
            ['john', filename, '--format=raw-sha256'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()
        
        if process.returncode == 0:
            return stdout
        else:
            return stderr
    except FileNotFoundError:
        print("John the Ripper is not installed.")
    
if __name__ == "__main__":
    create_password_file()
    run_john()