import streamlit as st
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# Define a function that generates a summary based on the input text and the number of summary lines
def generate_summary(text, n):
    # Tokenize the text into individual sentences
    sentences = sent_tokenize(text)
    
    # Tokenize each sentence into individual words and remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in word_tokenize(text) if word.lower() not in stop_words and word.isalnum()]
    
    # Compute the frequency of each word
    word_freq = Counter(words)
    
    # Compute the score for each sentence based on the frequency of its words
    sentence_scores = {}

    for sentence in sentences:
        sentence_words = [word.lower() for word in word_tokenize(sentence) if word.lower() not in stop_words and word.isalnum()]
        sentence_score = sum([word_freq[word] for word in sentence_words])
        if len(sentence_words) < 20:
            sentence_scores[sentence] = sentence_score
    
    # Select the top n sentences with the highest scores
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:n]
    summary = ' '.join(summary_sentences)
    
    return summary

# Define the Streamlit web interface
st.set_page_config(page_title="Text Summarizer", page_icon=":memo:", layout="wide")
st.title("Text Summarizer")
st.image("https://images.unsplash.com/photo-1498050108023-c5249f4df085", width=300)
st.write("Are you tired of reading through endless pages of text? Are your eyes starting to glaze over from all the information overload? Then you need the Text Summarizer! With just a few clicks, this magical tool will transform your long and boring text into a concise and snappy summary that will keep you engaged and on the edge of your seat. Say goodbye to brain fog and hello to clarity with the Text Summarizer!")
col1, col2 = st.columns(2)

with col1:
    text = st.text_area("Enter the text you want to summarize:", height=300)

with col2:
    n = st.slider("Number of summary lines", min_value=1, max_value=10, value=5)

if st.button("Generate Summary"):
    summary = generate_summary(text, n)
    summary_sentences = summary.split('. ')
    formatted_summary = '.\n'.join(summary_sentences)
    st.write("Summary:")
    st.write(formatted_summary)
