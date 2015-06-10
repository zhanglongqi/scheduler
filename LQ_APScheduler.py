__author__ = 'longqi'
"""
Demonstrates how  to schedule a job that executes on 0.001 second intervals.
"""

import time
import os

from apscheduler.schedulers.background import BackgroundScheduler


class Tick():
    real_time_interval = []
    last_time = time.time()

    def tick(self):
        Tick.real_time_interval.append(time.time() - Tick.last_time)
        Tick.last_time = time.time()

        # print('Tick! The time is: %s' % datetime.now())


t1 = Tick()

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(t1.tick, 'interval', seconds=0.1)
    last_time = time.time()
    scheduler.start()
    print(scheduler.running)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    time.sleep(1)
    print(Tick.real_time_interval)
    print(sum(Tick.real_time_interval) / len(Tick.real_time_interval))
