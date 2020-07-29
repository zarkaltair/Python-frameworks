from apscheduler.schedulers.blocking import BlockingScheduler


scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job is run every three minutes.')

@scheduler.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduler_job():
    print('This job is run every weekday at 5pm.')

scheduler.start()

