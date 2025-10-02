import streamlit as st
import pickle
import nltk 
import string
from nltk.corpus import stopwords

# Download necessary resources
nltk.download("punkt")
nltk.download("stopwords")

# Load model + vectorizer
knn = pickle.load(open("knn.pkl", "rb"))
tf = pickle.load(open("tfidf.pkl", "rb"))

def clean_resume(resume_text):
    # Lowercase
    text = resume_text.lower()
    # Tokenize
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():  # keep only words/numbers
            y.append(i)

    # Remove stopwords + punctuation
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words("english") and i not in string.punctuation:
            y.append(i)

    return " ".join(y)  # join cleaned tokens back to string

def main():
    st.title("📄 Resume Screening App")

    uploaded_file = st.file_uploader("Upload Resume", type=["txt", "pdf"])
    
    if uploaded_file is not None:
        try:
            resume_bytes = uploaded_file.read()
            resume_text = resume_bytes.decode("utf-8")
        except UnicodeDecodeError:
            resume_text = resume_bytes.decode("latin-1")

        # Clean the text
        cleaned_text = clean_resume(resume_text)

        # Transform text using TF-IDF
        vector_input = tf.transform([cleaned_text])

        # Predict with KNN
        prediction = knn.predict(vector_input)[0]

        st.subheader("✅ Prediction")
        st.write(f"Category: **{prediction}**")

if __name__ == "__main__":
    main()
