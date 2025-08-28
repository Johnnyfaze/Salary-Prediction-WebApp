# create a flask app for salary prediction
# import the libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

# create the flask app
app = Flask(__name__)

# load the model
pipeline = pickle.load(open('salary.pkl', 'rb'))

# create the home page
@app.route('/')
def home():
    return render_template('index.html')

# create a predict route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # create df with correct column names
    df = pd.DataFrame([{'Age': data.get('age'), 
                        'Education Level': data.get('education_level'), 
                        'Years of Experience': data.get('Years of Experience')}])

    # Prepare the input for the model
    prediction = pipeline.predict(df)

    return jsonify({'Salary': round(prediction[0], 2)})
# run the app
if __name__ == "__main__":
    app.run(debug=False)