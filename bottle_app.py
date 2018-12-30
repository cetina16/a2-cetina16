#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import *
from hashlib import sha256
from bottle import  *
from hashlib import sha256

my_list = list()


password= "c2e2de13717990810a222f960c2b73f7d981a7a230a8c5b05ea622ddcc6e1710"
def create_hash(password): 
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

@route('/static/<filepath>')
def server_static(filepath):
    return static_file(filepath, root='./')

#all pages
@route("/doityourself.html")
def doityourself():
    return template("doityourself.html")

@route("/types.html")
def types():
    return template("types.html")

@route("/whatisvanlife.html")
def whatisvanlife():
    return template("whatisvanlife.html")

@route('/x')
def commentop():
    return template('comment.html', my_list= my_list)


@post('/x')   #post method
def comment_adding():
    psw=request.forms.get('password')
    comment= request.forms.get('comment')
    if create_hash(psw) == password:
        my_list.append(comment)
        return template('comment.html', my_list=my_list)
    else:
        return template('comment.html', my_list=my_list)


@route('/')
@route("/index.html")
def index():
    return template("index.html")
 


   

    




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
