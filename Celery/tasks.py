from celery import Celery
import time


app = Celery('tasks', 
	celery_broker_url='amqp://localhost//', 
	celery_result_backend='db+mysql://root:123456789@localhost/test2',
	# sqlalchemy_backend_uri='db+mysql://root:123456789@localhost/test2'
)


@app.task
def reverse(string):
    time.sleep(10)
    return string[::-1]