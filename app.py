import joblib

def predict_blood(MLD, ND, TD, MFD):
    model = joblib.load('RF_Oversampling_gridsearch83%.pkl')
    prediction = model.predict([[MLD, ND, TD, MFD]])
    # 0 - No

    if prediction == 0:
        return 'No'

    # 1 - Yes
    
    else :
        return 'Yes'



import flask
from flask import render_template, request
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def default():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    #extract the data from post request
    MLD = float(request.form['MLD'])
    ND = float(request.form['ND'])
    TD = float(request.form['TD'])
    MFD = float(request.form['MFD'])
    prediction= predict_blood(MLD, ND, TD, MFD)
    return render_template('predict.html',Made_Donation=prediction)


if __name__ == '__main__':
    app.run()

  