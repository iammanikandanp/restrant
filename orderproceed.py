#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb, smtplib

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="mani")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")
p="""select fid,img,pctname,qty,disamt from useraddcart where cid='%s' """% (uid)
cur.execute(p)
rec=cur.fetchall()
q="""select name,phnnum,address,email from register where  id='%s' """% (uid)
cur.execute(q)
res=cur.fetchone()
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./css/bootstrap.css">
    <link rel="stylesheet" href="style/style.css">

</head>

<body>
<div class="navbars">
        <div class="logo">
            <div class="menu"><a href="#"><i class="glyphicon glyphicon-menu-hamburger" data-toggle="collapse"
                        data-target="#menus"></i></a>
                <a href="">
                    <img src="./image/bb logo.png" alt="illai" class="img-circle" width="40px" height="40px">
                    <span><b>Big Bite Dude</b></span>

                </a>
            </div>
        </div>
        <div class="searchbar"><a href=""><input type="search" placeholder="Search..." class="inputs">
                <button class="btn btn-danger btns"><i class="glyphicon glyphicon-search"></i></button>
        </div>
        <div><a href="dashboard.py"><i class="glyphicon glyphicon-home" style="padding-top: 7px;"></i> Home</a></div>     
        <div><a href="login.py"><i class="glyphicon glyphicon-user" style="padding-top: 7px;" ></i>Login</a></div>
        <div><a href=""><i class="glyphicon glyphicon-shopping-cart" style="padding-top: 7px;"></i></a></div>
    </div>

    <!-- navbar small screen -->
    <div class="navbars-min">
        <div class="logo-min">
            <div class="menu-min"><a href="#"><i class="glyphicon glyphicon-menu-hamburger" data-toggle="collapse"
                        data-target="#menus"></i></a>
                <a href="">
                    <img src="./image/bb logo.png" alt="illai" class="img-circle " width="40px" height="40px">
                    <span class="min-name"><b>BB Dude</b></span>
                </a>
            </div>
        </div>
        <div>
            <i class="glyphicon glyphicon-search " data-toggle="collapse" data-target="#searchbarmin"  style="margin-top: 7px;"></i>
        </div>
         <div>
            <a href="dashboard.py"><i class="glyphicon glyphicon-home" style="padding-top: 7px;"></i></a>&nbsp;&nbsp;       
             <a href="login.py"><i class="glyphicon glyphicon-user login-min" style="padding-top: 7px;"></i></a> &nbsp;&nbsp;
            <a href=""><i class="glyphicon glyphicon-shopping-cart" style="padding-top: 7px;"></i></a>
        </div>
    </div>
    <div id="searchbarmin" class="collapse">
        <div><a href=""><input type="search" placeholder="Search...">
                <button class="btn btn-danger">
                    <i class="glyphicon glyphicon-search"></i>
                </button>
            </a>
        </div>
    </div>
    <div id="menus" class="collapse col-md-4 col-sm-6 col-xs-6">
        <ul>
            <li><a href="">Sweets</a></li>
            <li><a href="">Mixture</a></li>
            <li><a href="">Chocolates</a></li>
            <li><a href="">Setting</a></li>
            <li><a href="">Blogs</a></li>
            <li><a href="">About us</a></li>
            <li><a href="">Contact us</a></li>   
        </ul>
    </div>
    <h1>ORDER DETAILS</h1>""")
for i in rec:
    print(""" <div class="container col-md-6 col-sm-12">
            
                <img src="media/%s" alt="ll" class="col-md-3" width="150px" height="150px" style="padding-top: 10px;">
           
            <hr>
            <h4>%s</h4>
            
            <p style="padding-top: 10px;" class="qty"> Quntity : %s</p>
            <h5 style="padding-top: 10px;"><b class="discount">Rs.%s <b></h5>
            
           </div>"""% (i[1],i[2],i[3],i[4]))

f="""select qty * disamt as total from useraddcart where cid='%s' """%(uid)
cur.execute(f)
you=cur.fetchone()

print(""" <div class="container" style="margin-top: 50px;">
        <div class="row">
            <div class="col-xs-12 cart">
                <form enctype="multipart/form-data" method="post">
                    <h2> DELIVARY DETAILS</h2>
                    <hr>
                    <div class="a-cart">
                        <label for="p-disam">Username</label><br>
                        <input type="text" name="uname" value="%s" required>
                    </div>
                    <div class="a-cart">
                        <label for="p-disam">Address</label><br>
                        <input type="text" name="address" value="%s" required>
                    </div>
                   
                    <div class="a-cart">
                        <label for="p-disamt">Phone Number</label><br>
                        <input type="number" name="pnum" value="%s" required>
                    </div>
                    <div class="radio">
                        <label><input type="radio" name="optradio" value="Cash on Delivary" checked>Cash on Delivary</label>
                    </div>
                    <div class="radio">
                        <label><input type="radio" name="optradio" value="Credit Card">Credit Card</label>
                    </div>
                    <div class="radio">
                        <label><input type="radio" name="optradio" value="Debit card">Debit card</label>
                    </div>
                    <a href="">
                        <button type="submit" name="udp" class="btn btn-success btn-lg">Order</button>
                    </a>
                    <a href="">
                        <button type="submit" name="cancel" class="btn btn-danger btn-lg">CANCEL</button>
                    </a>
                </form>
            </div>
        </div>

    </div>
    <script src="./js/jquery.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
</body>

</html>
""" %(res[0],res[2],res[1]))


uname=form.getvalue("uname")
address=form.getvalue("address")
phnum=form.getvalue("pnum")
payment=form.getvalue("optradio")
submit=form.getvalue("udp")
for i in rec:
    if submit !=None:
        g="""insert into orderlist (cid,fid,pname,qty,perprice,uname,address,phnum,payment) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(uid,i[0],i[2],i[3],i[4],uname,address,phnum,payment)
        cur.execute(g)
        con.commit()
        fromadd = "mk7094846331@gmail.com"
        password = "qyfs bnzl fmdn zmje"
        toadd = res[3]
        subject = "welcome to BB Dude"
        body = "{} Your order is confirmed..".format(uname)
        msg = """subject: {} \n\n{}""".format(subject, body)
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(fromadd, password)
        server.sendmail(fromadd, toadd, msg)
        server.quit()
        print(""" <script>
                          alert("email succesfully");
                          </script>""")
con.close()