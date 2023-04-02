import streamlit as st
from PIL import Image
import json
import requests  # pip install requests
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
from pathlib import Path
import streamlit as st
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "style.css"
css_file1 = current_dir / "styles" / "touch.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "download.png"


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Text Summarize", page_icon=":blush:", layout="wide")


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

 
lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_DMgKk1.json")
lottie_experience = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_3jmvq04g.json")
lottie_certificate = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_tbwqrxnz.json")
lottie_skills = load_lottieurl('https://assets9.lottiefiles.com/private_files/lf30_obidsi0t.json')
lottie_social = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_zwn6fmnu.json")
lottie_projects = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_cwA7Cn.json")


with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
## Text Summarisation
#### *Team : Aakash & Anusur* 

''')
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read() 
    

    

image = Image.open(profile_pic)
st.image(image, width=400,clamp=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()




  
st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
Text Summarizer is a powerful tool that helps you quickly and easily summarize long pieces of text into concise 
and informative summaries. Whether you're a student, researcher, or simply someone who needs to read a lot of text on a daily basis, 
Text Summarizer is an indispensable tool that will save you time and energy. With just a few clicks, 
Text Summarizer analyzes your text and provides you with a summary that captures the key ideas and information in a way 
that is easy to read and understand. So why waste time reading through endless pages of text when you can use Text Summarizer
 to get the gist of it in no time? Try it out today and experience the power of text summarization for yourself!
''')

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

st.markdown('''
## Let's get to the point with the power of summarization!
''')
st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    height= 200,
    width=700,
    key=None,
)

# Define the Streamlit web interface

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



#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)



#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################


st.markdown('''
## Social Media
''')
st_lottie(
    lottie_social,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    height= 200,
    width=700,
    key=None,
)

txt2('📱 LinkedIn', 'https://www.linkedin.com/in/akash-kathole-005125202')
txt2('📱 Twitter', 'https://twitter.com/akashkathole74')
txt2('📱 Youtube', 'https://www.youtube.com/channel/UCead4mOe2wXcjdo7_VaM6cg')
txt2('', 'https://www.youtube.com/channel/UCMec-aZFzp9FwDd5M7FKBYg')
txt2('📱 Githhub', 'https://github.com/akashkathole7')
txt2('📱 Stackoverflow', 'https://stackoverflow.com/users/17599238/akash-kathole')
txt2('📱 Medium', 'https://medium.com/@akashkathole74')


#####################
st.markdown('''
## contact
''')
st.header(":mailbox: Get In Touch With Me!")


contact_form = """
<form action="https://formsubmit.co/akashkathole74@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""


st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(css_file1):
    with open(css_file1) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)




    
