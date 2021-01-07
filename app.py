from flask import Flask, redirect, render_template, request, url_for
import os
import requests
import json
import sys

app = Flask(__name__)

app.config["DEBUG"] = True


Info = []
@app.route('/a')
def hello_world():
    return 'Hello from Flask! kjhjj bjhkh'

@app.route('/b')
def hello_world1():
    return render_template("html.html")

@app.route('/wibble')
def wibble():
    return 'This is my pointless new page'


@app.route("/")
def index():
    return render_template("html.html")

@app.route("/test", methods=["GET", "POST"])
def form():
    return render_template('form.html')

@app.route('/form', methods=['GET', 'POST'])
def hello():
    to=request.form['to']
    say=request.form['say']
    if to != "":
        return render_template('greet.html', say=os.getcwd(), to=request.form['to'])



@app.route('/test1', methods=['GET', 'POST'])
def hellodc():

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload File To sourush</h1>
    <form action="http://frjhgu.pythonanywhere.com/upload" method=post enctype=multipart/form-data>
      <p><input name="link" id="link" value="link"><input name="name" id="name" value="name">
         <input type=submit value=Upload>
    </form>
    '''

#@app.route('/upload',methods = ['GET','POST'])
#def upload_file():
#    if request.method =='POST':
#        file = request.files['file']
#        file.save(file.filename)
#    return 'okkkkkkkk'


@app.route('/upload',methods = ['GET','POST'])
def upload_file():
    if request.method =='POST':
        namev =request.form['name']
        url=request.form['link']

        
        r = requests.get(url)
        if namev:
            #f = open(ppath, 'wb')
            #f.write(r.content)
            sample_file = r.content
            upload_file = {"file": sample_file}
            urll= 'https://bot.sapp.ir/wUhqub6FyG0ZiPVLkYX33GCI2zz292xb6tyu7-zxB9th8Lw3wCzLyNA9fO0NFvxNtfoYZXGMlU0879Vus1tgMXd0oLomLa3MUdosd3V-ouRv5AwVuXkJ7GrJPumxq5S_u5VeUzlVic5eDrJ0/uploadFile'
            r1 = requests.post(urll, files = upload_file)
            x =  r1.text
            y = json.loads(x)
            furl=y["fileUrl"]
            urlsu = "https://bot.sapp.ir/JzdoVqPnRb7rn032wT29fZvNOZUCXX3pR4xp9HFWh0bkQ_8Qtw8j_L9zKZtxEBB3-HiJJjD6W423CyzbhvfHYtLdUpBgN0AXjdlACFTVhmkGNx2aj3VR7-3NghnkQLV3jzolToUeLWalQSLv/sendMessage"
            data = {
                "to": "Ke39LIXbMYNlfSwyBk6vK6Rd8kljthh9ef34khcZiYmbWxX3vrbyDWw95xY",
                "type": "FILE",
                "body": "tis is file",
                "time": "1538399819589",
                "fileName": namev,
                "fileType": "FILE_TYPE_OTHER",
                "fileSize": sys.getsizeof(sample_file),
                "fileUrl": furl
                }
            headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
            r3 = requests.post(urlsu, data=json.dumps(data), headers=headers)
            #filename = 'yuyu'
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return render_template('greet.html', say=r3.text, to=sys.getsizeof(sample_file))
    return 'okkkkkkkk'

