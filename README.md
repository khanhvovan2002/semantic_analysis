# Project README

## Semantic Analysis

This project focuses on two semantic analysis tasks: fake news detection and movie review sentiment classification.

### Fake News Detection

- Developed models for fake news detection using LSTMs and GloVe for text-to-vector conversion.
- Utilized Long Short-Term Memory (LSTM) networks, a type of recurrent neural network (RNN), for capturing sequential information in textual data.
- Employed GloVe (Global Vectors for Word Representation) embeddings to represent words as dense vectors.

### Movie Review Sentiment Classification

- Created a movie review classifier for positive and negative sentiment using the Bayes model and CountVectorizer.
- Leveraged Naive Bayes, a probabilistic classifier, to determine the likelihood of a document belonging to a particular sentiment class.
- Applied the CountVectorizer, a technique for converting text into a numerical representation by counting word occurrences.

## Repository Structure

- `/model/fake-true.ipynb`: Jupyter Notebook for fake news detection using LSTMs and GloVe embeddings.
- `model/positive-negative.ipynb`: Jupyter Notebook for movie review sentiment classification using the Bayes model and CountVectorizer.
- `data/`: Directory containing datasets for training and evaluation.
- `README.md`: Overview of the project.

## Getting Started

1. Clone the repository.
2. Install the required dependencies (specified in the notebooks).
3. Open the Jupyter Notebooks (`fake_news_detection.ipynb` or `movie_sentiment_classification.ipynb`) to explore the code and execute it.
4. Follow the instructions in the notebooks to train the models or use pre-trained models for prediction.

## Dependencies

- Python (version 3.6 or above)
- Jupyter Notebook
- TensorFlow (for LSTM models)
- Scikit-learn (for Bayes model)
- Numpy
- Pandas
- Matplotlib

Note: Additional dependencies may be required based on the specific code implementation and library versions.

## Conclusion

This project demonstrates the application of semantic analysis techniques for fake news detection and movie review sentiment classification. By using LSTMs, GloVe embeddings, the Bayes model, and the CountVectorizer, accurate models have been developed for these tasks.

