import MySQLdb as mysql
import hashlib
import sys
import warnings


class MysqlUserDB:
    warnings.filterwarnings('error')

    def __init__(self, DBrootHost, DBrootUser, DBrootPass, DBrootDatabase):
        self.DBrootHost = DBrootHost
        self.DBrootUser = DBrootUser
        self.DBrootPass = DBrootPass
        self.DBrootDatabase = DBrootDatabase

        try:
            print("Checking connection of MYSQL ...")
            self.con = mysql.connect(DBrootHost, DBrootUser, DBrootPass,
                                     DBrootDatabase)
            self.cursor = self.con.cursor()
            self.cursor.execute('Select version()')
            print("Connected to Mysql Database")
        except mysql.Error as error:
            print("Error %s\n Stop.\n" % error)
            sys.exit()

    def CreateDB(self, DBrootHost):
        print("Creating database...")
        try:
            self.cursor.execute('create database if not exists ' + DBrootHost)
            self.cursor.execute('show databases like %s' % DBrootHost)
            dbs = self.cursor.fetchone()
            print('Database created: %s' % dbs)
        except Warning as warn:
            print("Warning: %s \nStop.\n" % warn)
            sys.exit()

    def GrantsAccess(self, DBrootUser, DBrootPass, DBrootDatabase):
        print("Accesing Account ...")
        try:
            self.cursor.execute("SELECT user,db FROM mysql.db WHERE db ='%s'"
                                % (DBrootDatabase))
            result = self.cursor.fetchone()
            print("Access Granted", result)
        except Warning as warn:
            print("Warning %s" % warn)
        except mysql.Error as error:
            print("error %s \n stop" % error)
            sys.exit()

    def __del__(self):
        print("Finishing operation ...")
        self.cursor.close()
        self.con.close()
        print("Finished")

    def computeMD5hash(string):
        m = hashlib.md5()
        m.update(string.encode('utf-8'))
        return m.hexdigest()
