import platform
import psutil
import subprocess
import json

def get_cpu_frequency():
    try:
        with open("/proc/cpuinfo") as f:
            for line in f:
                if "MHz" in line:
                    # Convert MHz to GHz
                    return f"{float(line.split(':')[1].strip()) / 1000} GHz"
    except Exception as e:
        return str(e)
    return "N/A"

def get_memory_info():
    try:
        result = subprocess.run(['free', '-h'], stdout=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

def get_server_info():
    cpu_freq = psutil.cpu_freq()
    info = {
        "system": platform.system(),
        "node_name": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": psutil.cpu_count(logical=False),
        "logical_cpus": psutil.cpu_count(logical=True),
        "cpu_freq": cpu_freq._asdict() if cpu_freq else get_cpu_frequency(),
        "memory": psutil.virtual_memory()._asdict(),
        "swap_memory": psutil.swap_memory()._asdict(),
        "disk_partitions": [p._asdict() for p in psutil.disk_partitions()],
        "disk_usage": {p.mountpoint: psutil.disk_usage(p.mountpoint)._asdict() for p in psutil.disk_partitions()},
        "network_interfaces": {k: v[0]._asdict() for k, v in psutil.net_if_addrs().items()},
        "detailed_memory_info": get_memory_info(),
    }
    return info

if __name__ == "__main__":
    server_info = get_server_info()
    print(json.dumps(server_info, indent=4))
