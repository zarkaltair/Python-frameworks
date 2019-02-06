from flask import Flask
from celery_example import make_celery
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='amqp://localhost//',
    CELERY_RESULT_BACKEND='db+mysql://root:123456789@localhost/test2',
    SQLALCHEMY_DATABASE_URI='db+mysql://root:123456789@localhost/test2'
)
celery = make_celery(app)
db = SQLAlchemy(app)


class Results(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.String(50))


@app.route('/process/<name>')
def process(name):
    reverse.delay(name)
    return 'I sent an async request!'


@app.route('/insertData')
def insertData():
    return insert()


@celery.task(name='celery_example.reverse')
def reverse(string):
    return string[::-1]


def insert():
    for i in xrange(500):
        data = ''.join(choice('ABCDE') for i in range(10))
        result = Results(data=data)
        db.session.add(result)
    
    db.session.commit()

    return 'Done!'

if __name__ == '__main__':
    app.run(debug=True)