# 🚀 DAILY CONTENT EMAIL BOT (with video generation + TTS)

import random
import schedule
import smtplib
import ssl
from datetime import datetime
from email.message import EmailMessage
import time
from gtts import gTTS
import ffmpeg
from moviepy.editor import *  # for combining audio and video
import os

# 📧 Gmail Setup
SENDER_EMAIL = "smit3297@gmail.com"  # <-- Your Gmail
APP_PASSWORD = "ukgi teww otuo pitw"  # <-- Your App Password
RECEIVER_EMAIL = "smitsuthar.techmihirnaik@gmail.com"

# 🎯 Expanded Topics and Music
fact_topics = [
    "Amazing facts about the Universe",
    "Unknown facts about Animals",
    "Mind-blowing facts about the Human Body",
    "Historical facts you won't believe",
    "Bizarre World Records",
    "Secrets of the Ocean",
    "Hidden Facts about the Brain",
    "Shocking Inventions You Didn't Know About",
    "Incredible Space Discoveries",
    "Mysterious Ancient Civilizations",
    "Weird Science Experiments",
    "Amazing Nature Phenomena",
    "Record-Breaking Human Feats",
    "Strangest Laws Around the World",
    "Mind-Bending Optical Illusions",
    "Unknown Facts About Famous People",
    "Bizarre Food from Different Cultures",
    "Craziest Guinness World Records",
    "Things You Didn't Know Your Body Can Do",
    "Unbelievable Coincidences in History",
    "Secrets Behind Famous Landmarks",
    "Little-Known Tech Facts",
    "Freaky Facts about Weather",
    "Rare Animals You've Never Heard Of",
    "Wonders of the Micro World",
    "Quantum Physics Made Simple",
    "Mysteries of Black Holes",
    "Fun Facts About Languages",
    "Incredible Survival Stories",
    "Amazing Facts About Time and Space"
]

music_links = [
    "https://pixabay.com/music/search/relaxing/",
    "https://pixabay.com/music/search/inspiring/",
    "https://pixabay.com/music/search/upbeat/"
]

def create_content():
    topic = random.choice(fact_topics)
    music = random.choice(music_links)
    english_script = f"Did you know? {topic} can surprise you! Stay tuned to learn something amazing in just 60 seconds!"
    hindi_script = f"क्या आप जानते हैं? {topic} आपको चौंका सकता है! केवल ६० सेकंड में कुछ अद्भुत जानें!"
    
    # Randomly choose between English and Hindi
    language_choice = random.choice(['en', 'hi'])
    if language_choice == 'en':
        script = english_script
        language = 'en'
    else:
        script = hindi_script
        language = 'hi'

    title = f"{topic} | Amazing Facts in 60 Seconds! #Shorts"
    description = f"Discover fascinating facts about {topic} in this short video! Don't forget to like, share, and subscribe for more daily facts. #facts #shorts #amazingfacts"
    tags = "#facts #amazingfacts #shorts #trivia #dailyfacts"
    
    content = f"""
🎬 Topic: {topic}

📝 Script: {script}

🎯 Title: {title}
🧩 Description: {description}
🏷 Tags: {tags}

🎵 Suggested Free Music: {music}

✅ What You Need To Do:
1. Create a 60-sec video using this topic.
2. Add AI voice (English or Hindi).
3. Add background music.
4. Post as YouTube Short with the Title + Tags!

🚀 Let's grow your channel daily!  
"""
    return content, script, language

def generate_audio(script, language):
    tts = gTTS(text=script, lang=language)
    audio_filename = "daily_audio.mp3"
    tts.save(audio_filename)
    return audio_filename

def create_video(audio_filename):
    # Load a simple background image (can replace with custom images)
    video_clip = ImageClip("background_image.jpg", duration=60)
    audio_clip = AudioFileClip(audio_filename)

    video_clip = video_clip.set_audio(audio_clip)
    video_clip = video_clip.set_fps(24)

    # Save video
    video_filename = "daily_video.mp4"
    video_clip.write_videofile(video_filename, codec="libx264", audio_codec="aac")
    return video_filename

def send_email(video_filename):
    content, script, language = create_content()
    message = EmailMessage()
    message['Subject'] = f"Your Daily YouTube Content - {datetime.now().strftime('%Y-%m-%d')}"
    message['From'] = SENDER_EMAIL
    message['To'] = RECEIVER_EMAIL
    message.set_content(content)

    with open(video_filename, "rb") as video_file:
        video_data = video_file.read()
        message.add_attachment(video_data, maintype='video', subtype='mp4', filename=video_filename)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(message)
    
    print(f"✅ Email sent successfully! ({datetime.now().strftime('%Y-%m-%d %H:%M')})")

# Schedule it at 7 PM everyday
schedule.every().day.at("19:00").do(lambda: send_email(create_video(generate_audio(*create_content())[0])))

if __name__ == "__main__":
    print("⏳ Bot started... Waiting for 7 PM everyday...")
    while True:
        schedule.run_pending()
        time.sleep(60)
