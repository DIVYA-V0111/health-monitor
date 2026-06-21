# Server Health Monitor

A Python-based system monitoring tool that tracks CPU, memory, and disk usage on Linux servers and sends email alerts when thresholds are exceeded.

## Features
- Real-time monitoring of CPU, Memory, and Disk usage
- Automated email alerts when usage exceeds thresholds
- Logs all metrics with timestamps to a log file
- Runs automatically every minute using cron jobs

## Tech Stack
- Python 3
- psutil library
- Linux (Ubuntu)
- Bash/Cron
- Git/GitHub
- SMTP Email Alerting

## How It Works
1. Script runs every minute via cron job
2. Collects CPU, memory and disk metrics using psutil
3. Logs all metrics to monitor.log with timestamps
4. If any metric exceeds threshold, sends an email alert automatically

## Thresholds
- CPU Usage > 80% → Alert
- Memory Usage > 80% → Alert
- Disk Usage > 90% → Alert

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/DIVYA-V0111/health-monitor.git
cd health-monitor

### 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install psutil

### 4. Configure email alerts
Edit monitor.py and update:
- SENDER_EMAIL = "your-gmail@gmail.com"
- RECEIVER_EMAIL = "your-gmail@gmail.com"
- APP_PASSWORD = "your-app-password"

### 5. Run manually
python3 monitor.py

### 6. Set up cron job (auto run every minute)
crontab -e
Add this line:
* * * * * cd /home/user/health-monitor && /home/user/health-monitor/venv/bin/python3 /home/user/health-monitor/monitor.py

## Project Structure
health-monitor/
├── monitor.py       # Main monitoring script
├── monitor.log      # Auto-generated log file
├── .gitignore       # Git ignore file
└── README.md        # Project documentation

## Thank You
