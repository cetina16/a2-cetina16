#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, template, request, static_file, template, get, post


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
  color: darkblue; font-size: 20pt">
Hello everyone!Every human being needs to relax 
and feel free. Some people stay at home for relaxing.
Get rid of stress and tiredness is easy for them.Actually, I was one of them since 
watching videos about Vanlife.<strong>If you want to find out whether it is suitable for you,read an informative
article about</strong> <a href="https://tinyurl.com/yc4r4x66"> <abbr title= "Is van life for you?"><i>vanlife</i></abbr></a>
<br> There are many options. You can buy a old transporter and convert 
  it to a dream van or you can directly buy an amazing expensive van.
 It depends on your choises and financial conditions.<br> Live simply, live happier!</div>

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; 
&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; 
&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;


<img src="/static/van2ink.png" alt="vanimage" width="800" height="500"  >
&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

<img src="/static/vanedited.png" alt="vanimage2" width="800" height="500"  >
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
</html>


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
