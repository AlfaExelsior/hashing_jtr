import subprocess

def run_kali_command(command):
    try:
        result = subprocess.run(command.split(), capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    cmd = input("Enter a Kali Linux command: ")
    print(run_kali_command(cmd))