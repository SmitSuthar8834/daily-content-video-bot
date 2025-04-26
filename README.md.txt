# Daily Content Video Bot

## Description
This bot automates the process of generating YouTube Shorts content and sends it to your email daily at 7 PM. It generates the script, creates the audio, combines it into a video, and sends the video to your inbox.

## Requirements
- Python 3.x
- Libraries:
  - `gTTS` (Google Text-to-Speech)
  - `schedule`
  - `moviepy` (for video creation)
  - `smtplib` (to send email)
- FFmpeg installed on your machine for video processing.

## Setup Instructions

1. Clone this repo to your local machine.
2. Install the required Python libraries:
   ```bash
   pip install gtts schedule moviepy
