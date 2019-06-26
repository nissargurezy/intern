import MySQLdb
def connection():
    conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="intern",charset="utf8")
    c=conn.cursor()
    return c,conn
