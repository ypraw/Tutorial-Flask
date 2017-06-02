import connection as dbs
import warnings
warnings.filterwarnings('error')

mysqli = dbs.MysqlUserDB(DBrootHost='127.0.0.1', DBrootUser='root',
                         DBrootPass='', DBrootDatabase='flasktutorial')
# mysqli.CreateDB(DBrootDatabase='nganu1')
mysqli.GrantsAccess("flasktutorial")
db = mysqli.getDB()
paswd = mysqli.computeMD5hash("admin")
try:
    db.execute("INSERT INTO tb_user VALUES(%s,%s,%s,%s,%s,%s)",
               ('2', 'mugeni', 'yeay', 'user1', paswd, "mugeni@gmail.com"))
except Warning as warn:
    print("attention %s", warn)
mysqli.delCon()
