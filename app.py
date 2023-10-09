import re
import joblib
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet, stopwords
from nltk import pos_tag
from flask import Flask, render_template, request

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('stopwords')


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    user_review = request.form['review']
    

    return render_template("result.html", prediction=user_review)






# preprocess the inputted review to feed into the model
def preprocess_review(review):
    pass


# run flask server on localhost:8000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)