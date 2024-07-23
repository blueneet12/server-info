import subprocess

def get_memory_info():
    try:
        result = subprocess.run(['free', '-h'], capture_output=True, text=True, check=True)
        output = result.stdout
        return output
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        return None

if __name__ == "__main__":
    mem_info = get_memory_info()
    if mem_info:
        print(mem_info)
