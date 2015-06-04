__author__ = 'longqi'
"""
Demonstrates how  to schedule a job that executes on 0.001 second intervals.
"""

from datetime import datetime
import time
import asyncio
import os

from apscheduler.schedulers.background import BackgroundScheduler

real_time_interval = []

last_time = time.time()


def tick():
    global last_time
    real_time_interval.append(time.time() - last_time)
    last_time = time.time()

    # print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'interval', seconds=0.001)
    last_time = time.time()
    scheduler.start()
    print(scheduler.running)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))


    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        time.sleep(1)
        raise KeyboardInterrupt
    except (KeyboardInterrupt, SystemExit):
        print(real_time_interval)
        print(sum(real_time_interval) / len(real_time_interval))
        pass
