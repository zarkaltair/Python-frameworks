class Configuration():
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:123456789@localhost/test1'
    SECRET_KEY = 'something very secret'

    ### Flask Security ###
    SECURITY_PASSWORD_SALT = 'salt'
    SECIROTY_PASSWORD_HASH = 'bcrypt'