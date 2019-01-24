from redis import Redis
from datetime import timedelta
from rq_scheduler import Scheduler
from tasks import count_words_at_url


# задаём соединение с Redis по умолчанию
redis_conn = Redis()
scheduler = Scheduler(connection=redis_conn)
scheduler.enqueue_in(timedelta(seconds=5), count_words_at_url, 'https://khashtamov.com/')