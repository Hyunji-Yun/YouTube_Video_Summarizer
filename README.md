# YouTube Video Summarizer

A simple tool that extracts audio from a YouTube video, transcribes the content using OpenAI's Whisper, and summarizes it into concise English text using GPT-3.5. Built with Gradio for a clean and interactive UI.

---

## Features

- Paste any YouTube video URL  
- Extracts and transcribes audio with Whisper  
- Summarizes the transcript using GPT-3.5  
- Clean and responsive Gradio interface  
- One-click reset  

---

## Installation

### 1. Set up a virtual environment (optional)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your OpenAI API key

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your-api-key-here
```

### 4. Run the app

```bash
python3 youtube_summarizer.py
```

Replace `youtube_summarizer.py` with your actual Python file name if different.

---

## How It Works

1. User inputs a YouTube video URL  
2. Audio is downloaded and converted to MP3 using yt-dlp  
3. Whisper transcribes the audio into text  
4. GPT-3.5 summarizes the transcription  
5. The summary is displayed through a Gradio UI  

---

## Notes

- Longer videos may take time to process.  
- Ensure your use complies with YouTube’s Terms of Service and OpenAI’s usage policies.  
- Audio is temporarily saved as `input.mp3` and deleted after processing.  

---

## Requirements

- Python 3.8+  
- yt-dlp  
- openai  
- whisper  
- gradio  
- python-dotenv  
