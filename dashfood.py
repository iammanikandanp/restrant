#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb, os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="mani")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")
fid= form.getvalue("fid")
print("""<!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>BB Dude</title>
            <link rel="stylesheet" href="./css/bootstrap.css">
            <link rel="stylesheet" href="style/style.css">

        </head>

        <body>
            <!-- navbar -->
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
                <div><a href="#"><i class="glyphicon glyphicon-home" style="padding-top: 7px;"></i> Home</a></div>
                <div><a href="login.py"><i class="glyphicon glyphicon-user " style="padding-top: 7px;"></i> Logout</a></div>
                <div><a href=""><i class="glyphicon glyphicon-shopping-cart" style="padding-top: 7px;"></i></a></div>
            </div>

            <!-- navbar small screen -->
            <div class="navbars-min">
                <div class="logo-min">
                    <div class="menu-min"><a href="#"><i class="glyphicon glyphicon-menu-hamburger" data-toggle="collapse"
                                data-target="#menus"></i></a>
                        <a href="">
                            <img src="./image/bb logo.png" alt="illai" class="img-circle" width="40px" height="40px">
                            <span class="min-name"><b>BB Dude</b></span>
                        </a>
                    </div>
                </div>
                <div>
                    <i class="glyphicon glyphicon-search " data-toggle="collapse" data-target="#searchbarmin" style="padding-top: 7px;"></i>
                </div>
                <div>
                    <a href="#"><i class="glyphicon glyphicon-home" style="padding-top: 7px;"></i></a>&nbsp;&nbsp;       
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
            <div id="menus" class="collapse col-md-4 col-sm-6 col-xs-10">
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

            <div class="internet">
                <p class="ps" id="online"><i class="glyphicon glyphicon-ok"></i> You are Online</p>
                <p class="ps" id="offline"><i class="glyphicon glyphicon-ban-circle"></i> No Internet</p>
            </div>





            <script>
                let online = document.getElementById("online");
                let offline = document.getElementById("offline");
                window.addEventListener("online", function () {
                    online.style.display = "block";
                    setTimeout(()=>{
                        online.style.display = "none";
                    },3000);
                });
                window.addEventListener("offline", function () {
                    offline.style.display = "block";
                    setTimeout(()=>{
                        offline.style.display = "none";
                    },3000);
                });
            </script>

            <script src="./js/jquery.min.js"></script>
            <script src="./js/bootstrap.min.js"></script>
        """)
v1 = """select count(cid) from useraddcart where cid= '%s' """ % (uid)
cur.execute(v1)
hot = cur.fetchone()
print(""" <div class="container col-md-12" style="margin:10px","padding:5px">
<a href="orderproceed.py?id=%s">
 <button class="btn btn-warning btn-lg"> Proceed (%s)</button>
 </a>
  </div>""" % (uid,hot[0]))



q1 = """select * from useraddcart where cid='%s' """ % (uid)
cur.execute(q1)
red = cur.fetchall()
for i in red:
    print(""" 
             <div class="container col-md-12 col-sm-12">
            
                <img src="media/%s" alt="ll" class="col-md-3" width="250px" height="250px" style="padding-top: 10px;">
           
            <hr>
            <h4>%s</h4>
            <h6>%s</h6>
            <h5 style="padding-top: 10px;"><span class="disabled" style="text-decoration: line-through;" id="actual">Rs.%s</span> &nbsp;<b id="discount">Rs.%s <b></h5>
            <p style="padding-top: 10px;" id="qty"> Quntity : %s</p>
            <a href="removecart.py?id=%s&fid=%s">
           <button class= "btn btn-info btn-lg" style="margin-top: 15px;"> Remove</button></a>
           </div>


            """ % ( i[3], i[4], i[5], i[6],i[7],i[8],uid,fid))

print("""</div>""")



