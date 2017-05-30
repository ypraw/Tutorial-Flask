import MySQLdb
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


@auth.hash_password
def hash_pw(password):
    return md5(password).hexdigest()
