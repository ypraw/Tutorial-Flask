import connection as dbs
import warnings
warnings.filterwarnings('error')

mysqli = dbs.MysqlUserDB(DBrootHost='127.0.0.1', DBrootUser='root',
                         DBrootPass='', DBrootDatabase='flasktutorial')
# mysqli.CreateDB(DBrootDatabase='nganu1')
# mysqli.GrantsAccess("flasktutorial")
db = mysqli.getDB()
# 900150983cd24fb0d6963f7d28e17f72
# 0cc175b9c0f1b6a831c399e269772661

# try:
#    db.execute("INSERT INTO tb_user VALUES(?,%s,%s,%s,%s,%s)",
#               ('', 'anu', 'yeay', 'user1', paswd, "mugeni@gmail.com"))
# except Warning as warn:
#    print("attention %s", warn)

try:
    db.execute("select * from tb_content")
    result = db.fetchone()
    print(result)
except db.Error as error:
    print(error)
mysqli.delCon()
