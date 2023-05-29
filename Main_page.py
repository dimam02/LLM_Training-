import streamlit as st
from pytube import YouTube
from moviepy.editor import VideoFileClip
from transformers import pipeline
import os
import tempfile
from tempfile import NamedTemporaryFile

def save_audio(file):
    temp_file = NamedTemporaryFile(suffix=".mp4", delete=False)
    temp_filename = temp_file.name

    file_contents = file.read()
    temp_file.write(file_contents)
    temp_file.close()

    video = VideoFileClip(temp_filename)
    video_title = video.reader.filename

    audio_file = temp_filename.replace(".mp4", ".mp3")
    video.audio.write_audiofile(audio_file)

    return video_title, audio_file

def summarize_video(file):
    video_title, audio_file = save_audio(file)
    # Perform audio analysis or transcription analysis
    # ...
    # Use a summarization model to generate a summary
    summarizer = pipeline("summarization")
    summary = summarizer(transcription_text, max_length=150, min_length=30, do_sample=False)
    return video_title, summary[0]['summary_text']

st.title("Video Summary Tool")
st.markdown("Upload a video file to generate a summary.")

uploaded_file = st.file_uploader("Upload Video", type=["mp4"])

if st.button("Generate Summary"):
    if uploaded_file is not None:
        video_title, video_summary = summarize_video(uploaded_file)
        st.header(video_title)
        st.subheader("Summary:")
        st.write(video_summary)
    else:
        st.warning("Please upload a video file.")