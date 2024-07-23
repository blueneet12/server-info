import platform
import psutil
import json

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
        "cpu_freq": cpu_freq._asdict() if cpu_freq else "N/A",
        "memory": psutil.virtual_memory()._asdict(),
        "disk_partitions": [p._asdict() for p in psutil.disk_partitions()],
        "disk_usage": {p.mountpoint: psutil.disk_usage(p.mountpoint)._asdict() for p in psutil.disk_partitions()},
        "network_interfaces": {k: v[0]._asdict() for k, v in psutil.net_if_addrs().items()},
    }
    return info

if __name__ == "__main__":
    server_info = get_server_info()
    print(json.dumps(server_info, indent=4))
