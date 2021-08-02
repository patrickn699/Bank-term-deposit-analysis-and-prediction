from flask import Flask,render_template,url_for,request
import numpy as np
import pickle
import  os
from sklearn.preprocessing import StandardScaler

static = os.path.join('web_apps', 'static')
template = os.path.join('web_apps', 'templates')


model =  pickle.load(open('saved_rf.pkl', 'rb'))


app = Flask(__name__,static_folder=static, template_folder=template)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    #output = [x for x in request.form.values()]
    age = request.form.get('age')
    duration = request.form.get('duration')
    month = request.form.get('month')
    date = request.form.get('date')
    balance = request.form.get('balance')
    pout = request.form.get('poutcome')
    job = request.form.get('job_type')
    camp = request.form.get('campaign')
    contact = request.form.get('contact')
    house = request.form.get('housing')

    jb = {'blue-collar': 1, 'entrepreneur': 2, 'housemaid': 3, 'services': 4, 'technician': 5, 'self-employed': 6, 'admin': 7, 'unknown': 8, 'management': 9, 'unemployed': 10, 'retired': 11, 'student': 12}
    mnth = {'may': 1, 'jan': 2, 'jul': 3, 'nov': 4, 'jun': 5, 'aug': 6, 'feb': 7, 'apr': 8, 'oct': 9, 'sep': 10, 'mar': 11, 'dec': 12}
    pou = {'unknown': 1, 'failure': 2, 'other': 3, 'success': 4}
    con = {'unknown': 1, 'telephone': 2, 'cellular': 3}
    hl = {'yes':1,'no':0}

    job = jb.get(job)
    month = mnth.get(month)
    pout = pou.get(pout)
    contact = con.get(contact)
    house = hl.get(house)
    

    
    sc = StandardScaler()
    balance = sc.fit_transform([[balance]])
    balance = balance[0][0]
    print(balance)
    inn = np.array([[duration,month,date,age,balance,pout,job,camp,contact,house]])
    print(inn)
    op = model.predict(inn)
    op = op[0]

    if op == 1:
        op1 = 'deposit'
    else:
        op1 = 'not deposit'

    return render_template('index.html', prediction_text='The person may: {}'.format(op1))
   


if __name__ =='__main__':
    app.run(debug = True)