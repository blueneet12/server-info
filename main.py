import subprocess

def get_lscpu_info():
    try:
        # Run the lscpu command
        result = subprocess.run(['lscpu'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if the command was successful
        if result.returncode != 0:
            print(f"Error running lscpu: {result.stderr}")
            return None
        
        # Parse the output
        lscpu_output = result.stdout
        lscpu_info = {}
        for line in lscpu_output.splitlines():
            if ':' in line:
                key, value = line.split(':')
                lscpu_info[key.strip()] = value.strip()
        
        return lscpu_info
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    info = get_lscpu_info()
    if info:
        print("lscpu information:")
        for key, value in info.items():
            print(f"{key}: {value}")
