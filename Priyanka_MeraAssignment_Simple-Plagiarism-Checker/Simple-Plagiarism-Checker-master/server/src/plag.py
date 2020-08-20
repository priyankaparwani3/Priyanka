from flask import Flask, session,request,redirect,url_for, render_template
import re
import math

from flask_cors import CORS, cross_origin

# importing required modules 
import PyPDF2 
import pyrebase
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask("__name__")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app, support_credentials=True)
app.secret_key = os.urandom(24)
q = ""


config = {
  "apiKey": "AIzaSyBA7kDQiO25NCON5oPh2h0Bzc1I7eeMTng",
  "authDomain": "plagarism-check.firebaseapp.com",
  "databaseURL": "https://plagarism-check.firebaseio.com",
  "storageBucket": "plagarism-check.appspot.com",
  "messagingSenderId": "621931215883",
  "serviceAccount": "../../service.json",
  "appId": "1:621931215883:web:b460a52432ea8554f7db0e",
  "measurementId": "G-0F3SN0QCS7"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

@app.route('/index')
def index():
        return render_template("index.html")

@app.route('/')
@cross_origin(supports_credentials=True)
def admin():
        try:
                print(session['usr'])
                if session['teacher'] == 'yes':
                        print("teacher = yes")
                        return redirect(url_for('filesview'))
                else:
                        return redirect(url_for('fileupload'))
        except Exception as e:
                print(e)
                return redirect(url_for('index'))

@app.route('/filesview',methods=['POST','GET'])
def filesview():
        filesOutput=""
        files = ""
        urls = db.child("files").get()
        for url in urls.each():
                print(db.child("files/"+url.key()+"/downloadToken").get().val())
                print(storage.child("images/"+session['email']+"/"+url.key()).get_url(db.child("files/"+url.key()+"/downloadToken").get().val()))
                files = files+"""
                  <div style="margin:20px;padding:20px;overflow:hidden;white-space: nowrap;width:100px;height:150px;border: 0.5px solid black;border-radius: 7px 25px 15px;box-shadow: 2px 2px;>
                        <div>
                                <center><img src="fileIcon.png" width="50px" height="50px"/><br/><span>
                                <b>"""+url.key()+"""</b></span><br/><br/><br/>
                                <a style="text-decoration:none;background-color:blue;padding:8px;border-radius:5px 5px 5px 5px;color:white;" href="""+storage.child("images/"+db.child("files/"+url.key()+"/uploader").get().val()+"/"+url.key()+".pdf").get_url(db.child("files/"+url.key()+"/downloadToken").get().val())+""">Download</a></center>
                        </div>
                </div>
                """

        filesOutput = """
                                <!DOCTYPE>
<html>
<title>Student</title>
<head>
<style>

.login-page {
  width: 80%;
  padding: 8% 0 0;
  margin: auto;
}
.form {
  position: relative;
  z-index: 1;
  background: #FFFFFF;
  max-width: 360px;
  margin: 0 auto 100px;
  padding: 45px;
  text-align: center;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
}
.form input {
  font-family: "Roboto", sans-serif;
  outline: 0;
  background: #f2f2f2;
  width: 100%;
  border: 0;
  margin: 0 0 15px;
  padding: 15px;
  box-sizing: border-box;
  font-size: 14px;
}
.form button {
  font-family: "Roboto", sans-serif;
  text-transform: uppercase;
  outline: 0;
  background: #4CAF50;
  width: 100%;
  border: 0;
  padding: 15px;
  color: #FFFFFF;
  font-size: 14px;
  -webkit-transition: all 0.3 ease;
  transition: all 0.3 ease;
  cursor: pointer;
}
.form button:hover,.form button:active,.form button:focus {
  background: #43A047;
}
.form .message {
  margin: 15px 0 0;
  color: #b3b3b3;
  font-size: 12px;
}
.form .message a {
  color: #4CAF50;
  text-decoration: none;
}
.form .register-form {
  display: none;
}
body {
  background: #76b852; /* fallback for old browsers */
  background: -webkit-linear-gradient(right, #76b852, #8DC26F);
  background: -moz-linear-gradient(right, #76b852, #8DC26F);
  background: -o-linear-gradient(right, #76b852, #8DC26F);
  background: linear-gradient(to left, #76b852, #8DC26F);
  font-family: "Roboto", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;      
}
</style>

<html>
<head>
  <meta charset=utf-8 />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Files</title>

  <!-- Material Design Theming -->
  <link rel="stylesheet" href="https://code.getmdl.io/1.1.3/material.orange-indigo.min.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
  <script defer src="https://code.getmdl.io/1.1.3/material.min.js"></script>

  <link rel="stylesheet" href="main.css">
</head>
<body>
  <div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-header">

    <main class="mdl-layout__content mdl-color--grey-100">
      <div class="mdl-cell mdl-cell--12-col mdl-cell--12-col-tablet mdl-grid">
	  
		<!-- Container for the demo -->
        <div class="mdl-card mdl-shadow--2dp mdl-cell mdl-cell--12-col mdl-cell--12-col-tablet mdl-cell--12-col-desktop">
          <div class="mdl-card__title mdl-color--light-blue-600 mdl-color-text--white">
            <h2 class="mdl-card__title-text">Files Uploaded</h2>
          </div>
          <div class="mdl-card__supporting-text mdl-color-text--grey-600" style=" display:flex;" id="filesDiv">
          """+files+"""
          </div>
        </div>
      </div>
    </main>
	
  </div>
</body>
</html>
                """
        return filesOutput

@app.route('/login',methods= ['POST','GET'] )
def login():
        message = ""
        try:
                print(session['usr'])
                return redirect(url_for('admin'))
        except KeyError:
                if request.method == 'POST':
                        email = request.form['email']
                        password = request.form['password']
                        usertype = request.form['user']
                        print(email)
                        print(password)
                        try:
                                user = auth.sign_in_with_email_and_password(email,password)
                                user = auth.refresh(user['refreshToken'])
                                user_id = user['idToken']
                                session['usr'] = user_id
                                session['email'] = email
                                if usertype == 'teacher':
                                        session['teacher'] = "yes"

                                else:
                                        session['teacher'] = "no"
                                return redirect(url_for('admin'))
                        except:
                                message = "Incorrect password"
                                print(message)

                return render_template("login.html",message=message)

        return render_template('fileupload.html', query="")


@app.route('/signupt',methods=['POST','GET'])
def signupt():
        message = ""
        try:
                print(session['usr'])
                return redirect(url_for('admin'))
        except KeyError:
                if request.method == 'POST':
                        email = request.form['email']
                        password = request.form['password']
                        try:
                                user = auth.create_user_with_email_and_password(email, password)
                                user_id = user['idToken']
                                session['usr'] = user_id
                                session['email'] = email
                                session['teacher'] = "yes"
                                return redirect(url_for('admin'))
                        except Exception as e:
                                message = "Account Creation Failed"
                                print(str(e))
                                print(message)
                return render_template('signupt.html',message=message)

        return render_template('fileupload.html',query="")




@app.route('/signup',methods=['POST','GET'])
def signup():
        message = ""
        try:
                print(session['usr'])
                return redirect(url_for('admin'))
        except KeyError:
                if request.method == 'POST':
                        email = request.form['email']
                        password = request.form['password']
                        try:
                                user = auth.create_user_with_email_and_password(email, password)
                                user_id = user['idToken']
                                session['usr'] = user_id
                                session['email'] = email
                                return redirect(url_for('admin'))
                        except Exception as e:
                                message = "Account Creation Failed"
                                print(str(e))
                                print(message)
                return render_template('signup.html',message=message)

        return render_template('fileupload.html',query="")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/fileupload',methods=['POST','GET'])
def fileupload():
        message=""
        filesOutput=""
        if request.method == 'POST':
                file = request.files['file']
                if file and allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                        inputQuery = " "
                        universalSetOfUniqueWords = []
                        matchPercentage = 0

                        
                        # creating a pdf file object 
                        pdfFileObj = open('uploads/'+filename, 'rb') ;
                          
                        # creating a pdf reader object 
                        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
                          
                        # printing number of pages in pdf file
                        x = pdfReader.numPages
                        print(x) 
                          
                        # creating a page object
                        for i in range(x):
                                pageObj = pdfReader.getPage(i)
                                # extracting text from page
                                print(pageObj.extractText())
                                inputQuery = inputQuery+pageObj.extractText()
                        # closing the pdf file object 
                        pdfFileObj.close() 
                        lowercaseQuery = inputQuery.lower()
                        print(inputQuery)
                        queryWordList = re.sub("[^\w]", " ",lowercaseQuery).split()			#Replace punctuation by space and split
                        # queryWordList = map(str, queryWordList)					#This was causing divide by zero error

                        for word in queryWordList:
                                if word not in universalSetOfUniqueWords:
                                        universalSetOfUniqueWords.append(word)

                        ####################################################################################################

                        fd = open("database1.txt", "r")
                        database1 = fd.read().lower()

                        databaseWordList = re.sub("[^\w]", " ",database1).split()	#Replace punctuation by space and split
                        # databaseWordList = map(str, databaseWordList)			#And this also leads to divide by zero error

                        for word in databaseWordList:
                                if word not in universalSetOfUniqueWords:
                                        universalSetOfUniqueWords.append(word)

                        ####################################################################################################

                        queryTF = []
                        databaseTF = []

                        for word in universalSetOfUniqueWords:
                                queryTfCounter = 0
                                databaseTfCounter = 0

                                for word2 in queryWordList:
                                        if word == word2:
                                                queryTfCounter += 1
                                queryTF.append(queryTfCounter)

                                for word2 in databaseWordList:
                                        if word == word2:
                                                databaseTfCounter += 1
                                databaseTF.append(databaseTfCounter)

                        dotProduct = 0
                        for i in range (len(queryTF)):
                                dotProduct += queryTF[i]*databaseTF[i]

                        queryVectorMagnitude = 0
                        for i in range (len(queryTF)):
                                queryVectorMagnitude += queryTF[i]**2
                        queryVectorMagnitude = math.sqrt(queryVectorMagnitude)

                        databaseVectorMagnitude = 0
                        for i in range (len(databaseTF)):
                                databaseVectorMagnitude += databaseTF[i]**2
                        databaseVectorMagnitude = math.sqrt(databaseVectorMagnitude)

                        matchPercentage = (float)(dotProduct / (queryVectorMagnitude * databaseVectorMagnitude))*100

                        '''
                        print queryWordList
                        print
                        print databaseWordList


                        print queryTF
                        print
                        print databaseTF
                        '''

                        message = "Input query text matches %0.02f%% with database."%matchPercentage

                        filepath = "uploads/"+filename
                        print(filepath)
                        imgurl = storage.child("images/"+session['email']+"/"+filename).put(filepath, session['usr'])
                        data = {"uploader":session['email'],"name":filename,"size":imgurl['size'],"downloadToken": imgurl['downloadTokens']}
                        db.child("files/"+filename.replace(".pdf","")).set(data)
                        
        return render_template('fileupload.html',message=message)
                
app.run(threaded=True)
