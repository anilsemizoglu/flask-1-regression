# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template, flash
import pickle
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

# Load the model
# model = pickle.load(open('model.pkl','rb'))
def predictor(population):
    slope, intercept = pickle.load(open('models/ex1_restaurant_model.pkl','rb'))
    prediction = population * slope + intercept
    return prediction * 10000

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # Make prediction using model loaded from disk as per the data.
    # prediction = model.predict([[np.array(data['exp'])]])
    prediction = slope * (data['population']/10000) + intercept
    # Take the first value of prediction
    output = prediction # prediction[0]

    return jsonify(output)

@app.route('/')
def my_form():
    return render_template('hello.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()

    output = predictor(int(processed_text)/10000)
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5050, debug=True)
