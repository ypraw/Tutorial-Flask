import database as dbs

mysqli = dbs.MysqlUserDB(DBrootHost='127.0.0.1', DBrootUser='root',
                         DBrootPass='', DBrootDatabase='flasktutorial')
mysqli.GrantsAccess(DBrootUser='root', DBrootPass='',
                    DBrootDatabase='flasktutorial')
del mysqli
