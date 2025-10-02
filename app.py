import streamlit as st
import pickle
import re
import nltk 
nltk.download("punkt")
nltk.download("stopwords")
knn=pickle.load(open("knn.pkl","rb"))
tf=pickle.load(open("tfidf.pkl","rb"))
def main():
  st.title("Resume Screning App")
  uploaded_file=st.file_uploader("Upload_Resume",type=["txt","pdf"])
  if uploaded_file is not None:
    try:
      resume_bytes=uploaded_file.read()
      resume_text=resume_bytes.decode("utf-8")
    except UnicodeDecodeError:
      resume_text=resume_bytes.decode("latin-1")






if __name__ == "__main__":
    main()

