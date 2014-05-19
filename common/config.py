import sae

onsae = False
## DataBase
DB_DIALECT = 'mysql'
DB_DRIVER = ''
DB_QUERYSTRING = '?charset=utf8'

if onsae:
    DB_USERNAME = sae.const.MYSQL_USER
    DB_PASSWORD = sae.const.MYSQL_PASS
    DB_HOST = sae.const.MYSQL_HOST
    DB_PORT = sae.const.MYSQL_PORT
    DB_DATABASE = sae.const.MYSQL_DB
else:
    DB_USERNAME = ''
    DB_PASSWORD = ''
    DB_HOST = 'localhost'
    DB_PORT = '3306'
    DB_DATABASE = 'test'


SESSION_KEY = 'vkFwRjPgASwNed1sBmXjy+o/OSY0qFsPe1fljeyDE5aSbidWesAp9tNcenWcnmnS'
