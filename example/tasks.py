from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.task import periodic_task
from celery.schedules import crontab
import time


@shared_task
def sleepy(duration):
    time.sleep(duration)
    print("Done")

@periodic_task(run_every=crontab(minute=1))
def my_first_task():
    print("My first task!!!")

    