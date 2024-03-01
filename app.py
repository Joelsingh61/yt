

User
load_dotenv() ##load all the nevironment variables
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt="""You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """


## getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e
    
## getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text,prompt):

    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text

st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes"):
    transcript_text=extract_transcript_details(youtube_link)

    if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)





ChatGPT
It seems like you're developing a script that takes a YouTube video URL as input, extracts its transcript, and then generates detailed notes using Google's Gemini Pro. However, it appears you're using Streamlit for the user interface. Streamlit is a Python library used for creating web applications with simple Python scripts.

Your code structure looks mostly fine, but there are a few points to address:

Environment Variables: Ensure that you have set up your environment variables correctly, especially the GOOGLE_API_KEY.

Error Handling: You're catching exceptions but only re-raising them without any additional handling. You might want to handle specific exceptions or at least log the errors for debugging purposes.

User Interface: It seems like you're using Streamlit for the UI. Make sure you have installed Streamlit (pip install streamlit) and imported it (import streamlit as st) at the beginning of your script.

Image Display: You're using st.image to display an image of the YouTube video, which is good for enhancing the user experience.

Button Action: You're using a button (st.button) to trigger the processing of the YouTube video. Ensure that the button is functioning as expected.

Summary Display: After processing the video transcript, you're displaying the detailed notes using st.markdown and st.write, which should work fine.

Error Handling: Consider adding error handling in your Streamlit app to provide feedback to users if something goes wrong during processing.

Testing: Make sure to thoroughly test your application with various YouTube video links to ensure it works correctly in different scenarios.

Here's a streamlined version of your code with Streamlit integration and minor improvements:

python
Copy code
import os
from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
import google.generativeai as genai

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configure Google API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to extract transcript details from YouTube video
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([i["text"] for i in transcript_text])
        return transcript
    except Exception as e:
        st.error("Error extracting transcript details. Please check the YouTube video URL.")
        st.stop()

# Function to generate summary using Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Streamlit UI
st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if st.button("Get Detailed Notes"):
    if youtube_link:
        video_id = youtube_link.split("=")[1]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
        
        transcript_text = extract_transcript_details(youtube_link)

        if transcript_text:
            summary = generate_gemini_content(transcript_text, prompt)
            st.markdown("## Detailed Notes:")
            st.write(summary)
    else:
        st.warning("Please enter a YouTube video link.")
Make sure to run this script with Streamlit (streamlit run your_script.py) and ensure all dependencies are installed (pip install -r requirements.txt). Also, don't forget to replace your_script.py with the name of your Python script file.

User
fix transcript error import streamlit as st
from dotenv import load_dotenv

import os
from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
import google.generativeai as genai

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configure Google API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to extract transcript details from YouTube video
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([i["text"] for i in transcript_text])
        return transcript
    except Exception as e:
        st.error("Error extracting transcript details. Please check the YouTube video URL.")
        st.stop()

# Function to generate summary using Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Streamlit UI
st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if st.button("Get Detailed Notes"):
    if youtube_link:
        video_id = youtube_link.split("=")[1]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
        
        transcript_text = extract_transcript_details(youtube_link)

        if transcript_text:
            summary = generate_gemini_content(transcript_text, prompt)
            st.markdown("## Detailed Notes:")
            st.write(summary)
    else:
        st.warning("Please enter a YouTube video link.")
ChatGPT
It looks like you have duplicated the import statements for Streamlit and dotenv. Let's remove the duplicate imports and ensure that the code runs smoothly. Here's the corrected version:

python
Copy code
import os
import streamlit as st
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to extract transcript details from YouTube video
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([i["text"] for i in transcript_text])
        return transcript
    except Exception as e:
        st.error("Error extracting transcript details. Please check the YouTube video URL.")
        st.stop()

# Function to generate summary using Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Streamlit UI
st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if st.button("Get Detailed Notes"):
    if youtube_link:
        video_id = youtube_link.split("=")[1]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
        
        transcript_text = extract_transcript_details(youtube_link)

        if transcript_text:
            summary = generate_gemini_content(transcript_text, prompt)
            st.markdown("## Detailed Notes:")
            st.write(summary)
    else:
        st.warning("Please enter a YouTube video link.")
