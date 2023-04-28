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
st.set_page_config(page_title="Luminious", page_icon=":blush:", layout="wide")


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
## Luminous techathon
#### *creation : Aakash * 

''')
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read() 
    

    

image = Image.open(profile_pic)
st.image(image, width=400,clamp=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()




  
st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
Harnessing the power of the sun, solar energy generation has emerged as a pivotal solution in our pursuit of sustainable and renewable energy sources.
 The importance of solar power generation cannot be overstated, as it brings with it a multitude of benefits for individuals, communities, and 
 the planet as a whole.
''')

# Define a function that generates a summary based on the input text and the number of summary lines
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
#from tensorflow.keras.models import load_model
# Load the saved model

# loaded_model = load_model("/home/akash/Documents/programming/luminous hackathon ppt/pretrained_model_load/solar_energy_model.h5")

def app():
    # Set Streamlit app title
    st.title("Solar Energy Output Prediction")

    # Create input fields
    date_hour = st.text_input("Date-Hour(NMT)")
    wind_speed = st.number_input("Wind Speed")
    sunshine = st.number_input("Sunshine")
    air_pressure = st.number_input("Air Pressure")
    radiation = st.number_input("Radiation")
    air_temperature = st.number_input("Air Temperature")
    relative_air_humidity = st.number_input("Relative Air Humidity")

    # Create submit button
    submit_button = st.button("Predict")

    # Perform prediction when the submit button is clicked
    if submit_button:
        # Preprocess the input data
        input_data = pd.DataFrame({
            "Date-Hour(NMT)": [date_hour],
            "WindSpeed": [wind_speed],
            "Sunshine": [sunshine],
            "AirPressure": [air_pressure],
            "Radiation": [radiation],
            "AirTemperature": [air_temperature],
            "RelativeAirHumidity": [relative_air_humidity]
        })

        # Convert "Date-Hour (NMT)" column to datetime
        input_data["Date-Hour (NMT)"] = pd.to_datetime(input_data["Date-Hour (NMT)"], format="%d.%m.%Y-%H:%M")

        # Extract the features from the input data
        input_features = input_data[["WindSpeed", "Sunshine", "AirPressure", "Radiation", "AirTemperature", "RelativeAirHumidity"]]

        # Normalize the input features using the scaler used during training
        scaler = MinMaxScaler()
        input_features_scaled = scaler.fit_transform(input_features)

        # Make predictions using the loaded model
        predictions = loaded_model.predict(input_features_scaled)

        # Display the predictions
        st.subheader("Prediction Result")
        st.write("Predicted System Production:", predictions)

if __name__ == "__main__":
    app()




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




    
