from celery import Celery
import time


app = Celery('tasks', broker='amqp://localhost//', result_backend='db+sqlite:////tmp/test.db')

@app.task
def reverse(string):
    time.sleep(10)
    return string[::-1]