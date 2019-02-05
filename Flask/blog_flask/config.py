# configuration file for our app
class Configuration():
    # debug mod it is mod for monitoring to app
    DEBUG = True
    # disable track modifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # url to our database, consist of login and password from db
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:123456789@localhost/test1'
    # secret key for our app
    SECRET_KEY = 'something very secret'

    ### Flask Security ###

    # security information
    SECURITY_PASSWORD_SALT = 'salt'
    # method crypro hash
    SECIROTY_PASSWORD_HASH = 'bcrypt'