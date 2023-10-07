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
    processed_review = preprocess_review(user_review)

    prediction = log_reg_model.predict(processed_review)
    
    label_map = {1: 'Negative', 0: 'Neutral', 2: 'Positive'}
    predicted_label = label_map[prediction[0]]

    return render_template("result.html", prediction=predicted_label)



# Load the TF-IDF vectorizer and the trained logistic regression model
vectorizer = joblib.load('tfidf_vectorizer.pkl')
log_reg_model = joblib.load('log_reg_model.pkl')

# Function to map POS tag to first character used by WordNetLemmatizer
def get_wordnet_pos(tag):
    tag = tag[0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

# Your preprocessing function
def preprocess_review(review):
    # Text Cleaning
    review = re.sub('[^\w\s]', '', review)
    
    # Tokenization
    tokenized_review = word_tokenize(review)
    
    # Lemmatization
    lemmatizer = nltk.WordNetLemmatizer()
    lemmatized_review = [lemmatizer.lemmatize(w, get_wordnet_pos(p)) for w, p in pos_tag(tokenized_review)]
    
    # Remove Stopwords
    stop_words = set(stopwords.words('english'))
    filtered_review = [word for word in lemmatized_review if word.lower() not in stop_words]
    
    # TF-IDF Transformation
    tfidf_review = vectorizer.transform([" ".join(filtered_review)])
    
    return tfidf_review


# run flask server on localhost:8000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)