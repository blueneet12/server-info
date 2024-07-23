import subprocess

def get_cpu_info_dmidecode():
    try:
        # Run the `dmidecode` command to get CPU information
        result = subprocess.run(['dmidecode', '-t', 'processor'], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"dmidecode error: {e}"
    except FileNotFoundError:
        return "dmidecode not found. Install it with `sudo apt install dmidecode`."

def get_cpu_info_proc_cpuinfo():
    try:
        # Read the content of /proc/cpuinfo
        with open('/proc/cpuinfo', 'r') as file:
            cpu_info = file.read()
        return cpu_info
    except Exception as e:
        return f"Error reading /proc/cpuinfo: {e}"

def get_cpu_info_hwinfo():
    try:
        # Run the `hwinfo` command to get CPU information
        result = subprocess.run(['hwinfo', '--cpu'], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"hwinfo error: {e}"
    except FileNotFoundError:
        return "hwinfo not found. Install it with `sudo apt install hwinfo`."

def get_cpu_info_inxi():
    try:
        # Run the `inxi` command to get CPU information
        result = subprocess.run(['inxi', '-C'], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"inxi error: {e}"
    except FileNotFoundError:
        return "inxi not found. Install it with `sudo apt install inxi`."

def main():
    print("CPU Information using dmidecode:")
    print(get_cpu_info_dmidecode())
    print("\nCPU Information using /proc/cpuinfo:")
    print(get_cpu_info_proc_cpuinfo())
    print("\nCPU Information using hwinfo:")
    print(get_cpu_info_hwinfo())
    print("\nCPU Information using inxi:")
    print(get_cpu_info_inxi())

if __name__ == "__main__":
    main()
