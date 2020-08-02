# 配置文件, 防止耦合
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    # SECRET KEY
    SECRET_KEY = 'A-VERT-LONG-SECRET-KEY'

    # RECAPTCHA PUBLIC KEY
    # RECAPTCHA_PUBLIC_KEY = 'A-VERT-LONG-SECRET-KEY'
    # RECAPTCHA_PRIVATE_KEY = 'RECAPTCHA_PUBLIC_KEY'

    # Databse configuration
    SQLALCHEMY_DATABASE_URI = 'mysql://root:xjyxjy0723@localhost:3306/LightChat'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Gmail Config
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = '490601115@qq.com'
    MAIL_PASSWORD = '****************'