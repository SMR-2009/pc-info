import platform
import socket
import os
import psutil
import json
from datetime import datetime

def get_system_info():
    try:
        info = {
            "timestamp": datetime.now().isoformat(),
            "platform": platform.system(),
            "platform-release": platform.release(),
            "platform-version": platform.version(),
            "architecture": platform.machine(),
            "hostname": socket.gethostname(),
            "ip-address": socket.gethostbyname(socket.gethostname()),
            "mac-address": ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                                     for ele in range(0, 8 * 6, 8)][::-1]),
            "processor": platform.processor(),
            "ram": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
            "disk": f"{round(psutil.disk_usage('/').total / (1024 ** 3), 2)} GB"
        }
    except Exception as e:
        info = {"error": str(e)}

    return info

if __name__ == "__main__":
    data = get_system_info()
    output_path = os.path.join(os.getenv("APPDATA"), "pc_info_script", "last_info.json")

    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Failed to save system info: {e}")
