import ctypes
import time

REPEAT_INTERVAL = 60  # 1 hour

while True:
    ctypes.windll.user32.MessageBoxW(
        0,
        "Hey Dips, Drink water!",
        "Hydration Reminder",
        0
    )
    time.sleep(REPEAT_INTERVAL)