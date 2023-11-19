import os
import time
from celery import Celery

celery = Celery(__name__)
celery.conf.broker_url = "redis://redis:6379/0"
celery.conf.result_backend = "redis://redis:6379/0"


@celery.task(name="create_task")
def create_task(a, b, c):
	time.sleep(a)
	return b + c


@celery.task(name="subprocess")
def subprocess(seconds):
	print("Initiating process...")
	import time
	time.sleep(2)
	print("Executing: 20 %")
	time.sleep(3)
	print("Executing: 50 %")
	time.sleep(1)
	print("Executing: 70 %")
	time.sleep(seconds)
	msg = "Process ended sucessfully"
	print("Executing: 100%")
	time.sleep(2)
	print(msg)
	return msg
