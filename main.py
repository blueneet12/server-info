import subprocess

def get_memory_info():
    try:
        # Reading memory information from /proc/meminfo
        with open('/proc/meminfo', 'r') as file:
            meminfo = file.read()
        return meminfo
    except FileNotFoundError as e:
        print(f"Error occurred: {e}")
        return None

if __name__ == "__main__":
    mem_info = get_memory_info()
    if mem_info:
        print("Memory Information:")
        print(mem_info)
