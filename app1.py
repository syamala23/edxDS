from flask import Flask, request, render_template,redirect,url_for
import numpy as np
import joblib 
import pickle
app = Flask(__name__)
model1 =pickle.load(open('myplacementnow.pkl',"rb")) 
ct=joblib.load("myplacementnow.pkl") 

@app.route('/')
def hel():
    return render_template("current.html")
@app.route('/job')
def jobs():
     return render_template("joblist.html")

@app.route('/login')
def log():
    return render_template("login.html")

@app.route('/resume')
def resume():
    return render_template("resum.html")

@app.route('/interview')
def interview():
    return render_template("interview.html")
@app.route('/career')
def career():
  return render_template("careers.html")

@app.route('/sec')
def hello():
    return render_template("index.html") 

@app.route('/guest', methods=['GET','POST'])
def Guest():
    if request.method == 'POST':
        age = request.form['age']
        gender = request.form['gender']
        stream = request.form['stream']
        internship = request.form['internship']
        cgpa = request.form['cgpa']
        backlogs = request.form['backlogs']
        internship=request.form['internship']
    return render_template("index2.html")

     

@app.route('/y_predict',methods=["POST"])
def y_predict():
    x_test=[yo for yo in request.form.values()]
    
    predict_output=model1.predict([x_test])
    if predict_output==0:
        return render_template("unsel.html")
    else: 
       return render_template("sel.html")
if __name__=="__main__":

 app.run(debug=True,port=8000)

