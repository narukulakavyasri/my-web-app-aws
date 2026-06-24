import psutil
from datetime import datetime

cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

report = f"""
{datetime.now()}

CPU Usage : {cpu}%
RAM Usage : {ram}%
Disk Usage : {disk}%

----------------------------------
"""

print(report)

with open("logs/server.log", "a") as file:
    file.write(report)