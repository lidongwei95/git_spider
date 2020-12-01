#!/usr/bin/python3
#coding=utf-8
# 定时任务

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os,sys


def job_start():
    ntime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open ("time_s.log", "a") as f:
        f.write("uos_launch: %s " % ntime)
    os.system("cd /home/worker/killall_script")
    os.system("bash -x Get_the_uisee_window.sh")

def job_stop():
    ntime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open ("time_s.log", "a") as f:
        f.write("uos_stop: %s" % ntime)
    os.system("cd /home/worker/killall_script")
    os.system("bash -x stop_safety.sh")


# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job_start, 'cron', day_of_week='1-5', hour=15, minute=40)
scheduler.add_job(job_stop, 'cron', day_of_week='1-5', hour=16, minute=00)
scheduler.start()
