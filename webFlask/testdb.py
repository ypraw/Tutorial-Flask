import connection as dbs

mysqli = dbs.MysqlUserDB(DBrootHost='127.0.0.1', DBrootUser='root',
                         DBrootPass='')
# mysqli.CreateDB(DBrootDatabase='jajal')
mysqli.GrantsAccess(DBrootUser='root', DBrootPass='',
                    DBrootDatabase='flasktutorial')
del mysqli
