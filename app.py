import streamlit as st
import pickle
import numpy as np


# Streamlit app
st.title("Naive Bayes Text Classifier")
st.write("Enter text to classify it using the Naive Bayes model.")

# User input
user_input = st.text_area("Input Text", "")
# Load the model and vectorizer
with open('naive_bayes_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('count_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

if st.button("Predict"):
    if user_input:
        # Transform the user input using the vectorizer
        input_vector = vectorizer.transform([user_input])

        # Get prediction from the model
        prediction = model.predict(input_vector)

        # Display the result
        if prediction[0] == 'positive':
            st.success(f"Predicted Class: {prediction[0]}")
        elif prediction[0] == 'negative':
            st.error(f"Predicted Class: {prediction[0]}")
        else:
            st.warning(f"Predicted Class: {prediction[0]}")
    else:
        st.warning("Please enter some text for classification.")
