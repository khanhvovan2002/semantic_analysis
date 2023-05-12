from flask import Flask, request, jsonify, render_template
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.pipeline import Pipeline
import pickle
import re
import nltk
from textblob import Word
app = Flask(__name__)
import platform
print(platform.uname())
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']
    text = text.lower()
    text = " ".join(re.sub(r'[^a-zA-z0-9\s]', '', word) for word in text.split()) 
    text = re.sub(r'\d+', '', text)
    stop_words = set(stopwords.words("english"))
    text = " ".join(re.sub(r'http\S+', '', word) for word in text.split()) 
    text = " ".join(word for word in text.split() if text not in stop_words)
    text = " ".join([Word(word).lemmatize() for word in text.split()])
    if(model_1.predict([text])):
      prediction_1 = 'positive'
    else:
      prediction_1 = 'negative'
    if(model_2.predict([text])):
        prediction_2 = 'True news'
    else:
        prediction_2 = 'Fake news'
    prediction = prediction_2 + 'with' + prediction_1 + 'content!'
    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    with open('model/bayens.pkl', 'rb') as file:
        model_1 = pickle.load(file)
    with open('model/lstm.pkl', 'rb') as file:
        model_2 = pickle.load(file)
    app.run(host='0.0.0.0', port=5005)