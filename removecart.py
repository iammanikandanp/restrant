#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="mani")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")
fid = form.getvalue("fid")
u = """select qty from useraddcart where cid='%s' and fid='%s' """ % (uid, fid)
cur.execute(u)
res = cur.fetchone()

if res!=None:
    if res[0]==1:
        x="""delete from useraddcart where cid='%s' and fid='%s' """ % (uid, fid)
        cur.execute(x)
        con.commit()
        con.close()
    if res[0] > 1:
        count=res[0]-1
        o="""update useraddcart set qty='%s' where cid='%s' and fid='%s' """%(count,uid,fid)
        cur.execute(o)
        con.commit()
        con.close()
print(""" <script> 
        location.href="dashfood.py?id=%s&fid=%s"
        </script>
        """ % (uid, fid))