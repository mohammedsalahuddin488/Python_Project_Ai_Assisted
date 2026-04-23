import time
from plyer import notification


def water_reminder():
    while True:
        notification.notify(
            title="Water Reminder for sallu",
            message="It's time to drink water! Stay hydrated! 💧",
            timeout=10  # seconds
        )
       
        time.sleep(3600)  
water_reminder()
