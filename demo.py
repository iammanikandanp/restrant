#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="mani")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")
fid = form.getvalue("cid")
padam=form.getvalue("img")
pcts=form.getvalue("pct")
shortnote=form.getvalue("sd")
actamt=form.getvalue("act")
discount=form.getvalue("dis")
v1= """select fid from useraddcart where cid='%s' and fid='%s' """%(uid,fid)
cur.execute(v1)
rec=cur.fetchone()
if rec==None:
    j = """insert into useraddcart (cid,fid ,img,pctname,shortnote,actualamt,disamt,qty) values ('%s','%s','%s','%s','%s','%s','%s','1')""" % (uid,fid,padam,pcts,shortnote,actamt,discount)
    cur.execute(j)
    con.commit()
    print(""" <script> 
    location.href="dashfood.py?id=%s&fid=%s"
    </script>
    """%(uid,fid))
if rec!=None:
    u="""select qty from useraddcart where cid='%s' and fid='%s' """%(uid,fid)
    cur.execute(u)
    res=cur.fetchone()
    count=res[0]+1
    o="""update useraddcart set qty='%s' where cid='%s' and fid='%s' """%(count,uid,fid)
    cur.execute(o)
    con.commit()
    print(""" <script> 
        location.href="dashfood.py?id=%s&fid=%s"
        </script>
        """ % (uid, fid))