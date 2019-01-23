import time

from rq import Queue
from redis import Redis
from tasks import count_words_at_url


# задаём соединение с Redis по умолчанию
redis_conn = Redis()
queue = Queue(connection=redis_conn)
# кладём выполнение нашей задачи в очередь
job = queue.enqueue(count_words_at_url, 'https://khashtamov.com/')
print(job.result)   # функция возвратит None, так как задача скорее всего не будет выполнена к этому момент
# подождём 4 секунды
time.sleep(4)
print(job.result)   # => результат выполнения функции (кол-во слов)