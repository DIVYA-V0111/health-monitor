import psutil
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90

# Log file
LOG_FILE = "monitor.log"

# Email settings
SENDER_EMAIL = "divyavenkatesh91080@gmail.com"
RECEIVER_EMAIL = "divyavenkatesh91080@gmail.com"
APP_PASSWORD = "owztvrhnfqxhzrph"

def send_email(subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        log_message("Alert email sent successfully!")
    except Exception as e:
        log_message(f"Failed to send email: {e}")

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
        send_email(
            "ALERT CPU - Health Monitor",
            f"CPU usage is high: {cpu}%\nTime: {datetime.datetime.now()}"
        )
    if memory > MEMORY_THRESHOLD:
        log_message(f"ALERT! Memory usage is high: {memory}%")
        send_email(
            "ALERT Memory - Health Monitor",
            f"Memory usage is high: {memory}%\nTime: {datetime.datetime.now()}"
        )
    if disk > DISK_THRESHOLD:
        log_message(f"ALERT! Disk usage is high: {disk}%")
        send_email(
            "ALERT Disk - Health Monitor",
            f"Disk usage is high: {disk}%\nTime: {datetime.datetime.now()}"
        )

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
