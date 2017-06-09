import connection as dbs
import warnings
warnings.filterwarnings('error')

mysqli = dbs.MysqlUserDB(DBrootHost='127.0.0.1', DBrootUser='root',
                         DBrootPass='', DBrootDatabase='pos')

db = mysqli.getDB()

# Create pass admin in md5
paswd = mysqli.computeMD5hash("admin")
try:
    db.execute("INSERT INTO tb_user VALUES(%s,%s,%s,%s,%s,%s)",
               (None, 'anu', 'yeay', 'user2', paswd, "mugeni@gmail.com"))
except Warning as warn:
    print("attention %s", warn)

mysqli.delCon()
