#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, template, request, static_file, template, get, post
from hashlib import sha256
#Below code is taking from https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py
def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()


My_list = []
Passwords = {}

index = 0
password_index = 0
password_found = False


def Registering(username, pw1):
    global Passwords
    hsh1 = create_hash(pw1)
    if (username not in Passwords):
        Passwords[username] = hsh1
        return True
    else:
        return False


def Comment(username, pw1):
    global Passwords
    global My_list

    hsh2 = create_hash(pw1)

    if (username in Passwords):
        if (Passwords[username] == hsh2):
            return True
        else:
            return False


def htmlify(text):

def static_file_callback(filename):
    return static_file(filename, root=".")


route('/static/<filename>', 'GET', static_file_callback)
def html ():
    page = """
<!DOCTYPE html>
	<html lang="en-US">
		<head>
		  <title> Vanlife </title>
		<meta charset="utf-8"/>
        <link rel= "stylesheet" href= "/static/style.css">
        <link rel="icon" href="/static/vl.ico">
        <style> 
		.box {width:800px;
              margin:auto;
              width:800px;
              background-color: lemonchiffon;
              border: 1px solid darkblue;}
        </style>
		</head>
	    <body>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 <header>
  <img src="/static/vl.png" alt="vanlife designed by Gimp" width="350" height="150">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 </header>

 <div class="menu">
		     <ul>
				  <li><a href="/static/index.html">Mainpage</a></li>
				 <li><a href="/static/whatisvanlife.html">WhatisVanLife</a></li>
				 <li><a href="/static/doityourself.html">Do it Yourself</a></li>
				 <li><a href="/static/types.html">Types </a></li> 
				 <li><a href="/static/comments.html">Comments</a></li>
			 </ul> </div><br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; 
&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; 
&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

  <div class="box">
  <p style= "font-family: Times New Roman, sans-serif ;text-align:justify;text-indent:10px;
   text-align: center;margin:auto ; padding:20px;
  color: darkblue; font-size: 20pt"> Comments </p>
  
			<form class="form_input" action="/yorum" method="POST">
				<br/>
				<textarea type="text" name="comments" style="font-size:20px; color:darkblue; background-color:lemonchiffon;  border:3px solid darkblue; width:200" placeholder=" Please enter your comment"></textarea><br/>
				Enter your passwords:<br/>
				<input type="password" name="password"><br/><br/>
				<button type="submit" name="button" style=">Submit</button>
			</form>
			<h1 style="font-size:24px; color:darkblue;"> Previosly entered comments </h1><br/>
		</div>
		
		<ol>
			
		</ol>
  
  

</div>

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; 
&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; 
&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;




	<div class="footer">
	<footer>
		<p> contact: cetina16@itu.edu.tr</p> <br>
 <p>references:</p>
<a href="https://southernchronicles.icebreaker.com" target="_blank">icebraker.com </a> <br>
<a href="https://www.influx.co.uk/" target="_blank"> influx.co </a> <br>
<a href="https://kombilife.com/" target="_blank"> kombilife.com </a> <br>
<a href="https://pinterest.com" target="_blank"> pinterest.com </a> <br>
<a href="https://www.thevanual.com/" target="_blank"> thevanual.com </a>
</footer></div>
</body>


    """
    return page


route('/', 'GET', html)

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
    run()
