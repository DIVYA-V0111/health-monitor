import psutil
import datetime
import os

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90

# Log file
LOG_FILE = "monitor.log"

def get_cpu():
    return psutil.cpu_percent(interval=1)

def get_memory():
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk():
    disk = psutil.disk_usage('/')
    return disk.percent

def log_message(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)
    with open(LOG_FILE, "a") as f:
        f.write(log_entry + "\n")

def check_alerts(cpu, memory, disk):
    if cpu > CPU_THRESHOLD:
        log_message(f"ALERT! CPU usage is high: {cpu}%")
    if memory > MEMORY_THRESHOLD:
        log_message(f"ALERT! Memory usage is high: {memory}%")
    if disk > DISK_THRESHOLD:
        log_message(f"ALERT! Disk usage is high: {disk}%")

def monitor():
    log_message("--- Health Check Started ---")
    cpu = get_cpu()
    memory = get_memory()
    disk = get_disk()
    log_message(f"CPU Usage: {cpu}%")
    log_message(f"Memory Usage: {memory}%")
    log_message(f"Disk Usage: {disk}%")
    check_alerts(cpu, memory, disk)
    log_message("--- Health Check Complete ---")

if __name__ == "__main__":
    monitor()
