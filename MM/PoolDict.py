import pymysql as mysql
def ConnectionPolling():
    dbe = mysql.connect(host="localhost", port=3306,user="root", password="1234", db="mm")
    cmd = dbe.cursor(mysql.cursors.DictCursor)
    return (dbe, cmd)
