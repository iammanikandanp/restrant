#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi,cgitb
cgitb.enable()
con = pymysql.connect(host="localhost",user="root",password="",database="mani")
cur=con.cursor()
form= cgi.FieldStorage()
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
        <div><a href="login.py"><i class="glyphicon glyphicon-user " style="padding-top: 7px;"></i> Login</a></div>
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
     <div class="container divs">

        <div>
            <a href="">
                <img src="./image/rasakula.jpg" alt="illai"  class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/lolipop donut.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/walfuls.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/gift.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/sweet murukku.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/cupcake.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/cakes.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/col donus.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/badham mlik.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/brownies.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/seeda.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/miture2.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>

       </div>
         <div class="container ">
            
""")

q1="""select * from sweets """
cur.execute(q1)
red=cur.fetchall()
for i in red:
        print(""" 
         <div class="cartd col-md-2 col-sm-2 ">
        <header>
            <img src="media/%s" alt="ll" id="cart-img" style="padding-top: 5px;">
        </header>
        <hr>
        <h4>%s</h4>
        <h6>%s</h6>
        <h5><span class="disabled" style="text-decoration: line-through;">Rs.%s</span> &nbsp;<b>Rs.%s <b></h5>
        <footer>
            <a href="login.py">
            <button class="btn btn-danger cart-btn btn-lg"> ADD CART</button></a>
        </footer>

    </div>
        """ %(i[1],i[2],i[3],i[4],i[5]))
print("""</div>""")
