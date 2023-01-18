import streamlit as st
import joblib
from transformers import pipeline
from IPython.display import YouTubeVideo
from youtube_transcript_api import YouTubeTranscriptApi

st.title("YouTube Video Summarization")

youtube_video=st.text_input("Enter a video url")

video_id = youtube_video.split("=")[1]

st.write(video_id)  
st.video(youtube_video)

YouTubeTranscriptApi.get_transcript(video_id)
transcript = YouTubeTranscriptApi.get_transcript(video_id)
result = " "
for i in transcript:
    result += " " + i["text"]
t=len(result)
st.write(t)

pipe_lr=joblib.load(open("summarizeryt.pkl","rb"))

def summarizer_transformers(from_url):
    results = pipe_lr(from_url)
    num_iters = int(len(result)/1000)
    summarized_text = []
    for i in range(0, num_iters + 1):
        start = 0
        start = i * 1000
        end = (i + 1) * 1000
        out = pipe_lr(result[start:end])
        out = out[0]
        out = out["summary_text"]
        summarized_text.append(out)
    return summarized_text


result1=summarizer_transformers(youtube_video)
st.write(result1)