# Sends a notification on the desktop with the current time
# Requires installation of notify2 library ("pip3 install notify2")
# Linux Only

import notify2
from time import sleep
from datetime import datetime

notify2.init("Desktop Notifier")
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    n = notify2.Notification("The time is",
                             current_time
                             )
    n.show()
    sleep(5)
