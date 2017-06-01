import MySQLdb as mysql
import hashlib


def computeMD5hash(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()


db = mysql.connect("127.0.0.1", "root", "", "flasktutorial")
cur = db.cursor()

cur.execute("Select * from tb_user")
row = cur.fetchone()[4]

if (computeMD5hash('admina') == row):
    print("yeay")
    print(row)
else:
    print("this Fucking shit")

cur.close()
db.close()
