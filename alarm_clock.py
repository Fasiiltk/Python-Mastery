# alarm_clock.py
import time
from datetime import datetime

alarm_time = input("Enter alarm time (HH:MM): ")
while True: 
    current_time = datetime.now().strftime("%H:%M")
    if current_time == alarm_time:
        print("Wake up!")
        break
    print(f"Current time: {current_time}")
    time.sleep(60)  # Check every minute
    
