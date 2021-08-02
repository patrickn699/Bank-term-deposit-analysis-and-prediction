from flask import Flask,render_template,url_for,request
import numpy as np
import pickle
import  os

static = os.path.join('web_apps', 'static')
template = os.path.join('web_apps', 'templates')


app = Flask(__name__,static_folder=static, template_folder=template)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    output = [x for x in request.form.values()]
    return render_template('index.html', prediction_text='The person may{}'.format(output))
   


if __name__ =='__main__':
    app.run(host ='0.0.0.0', port = 5001, debug = True) 