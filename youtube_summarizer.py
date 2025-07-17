import os
import subprocess
import gradio as gr
import whisper
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
client = OpenAI()

# Load Whisper model
model = whisper.load_model("base")

def download_audio(url):
    if os.path.exists("input.mp3"):
        os.remove("input.mp3")
    subprocess.run(f'yt-dlp -x --audio-format mp3 -o "input.mp3" "{url}"', shell=True)

def summarize(url):
    try:
        download_audio(url)
        result = model.transcribe("input.mp3")
        transcript = result["text"]

        prompt = f"Summarize the following transcript in English in 5 sentences or less:\n\n{transcript[:3000]}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        summary = response.choices[0].message.content
        os.remove("input.mp3")
        return summary
    except Exception as e:
        return f"⚠️ Error occurred: {e}"

# Load external CSS file
with open("style.css") as f:
    custom_css = f.read()

with gr.Blocks(css=custom_css) as demo:
    # Title and description
    gr.Markdown("# YouTube Video Summarizer")
    gr.Markdown("## This tool extracts audio from a YouTube video, transcribes it, and summarizes the content in English.")

    # 2-column layout: left for input/buttons, right for summary
    with gr.Row():
        with gr.Column(scale=1):  # Left side: URL input + buttons
            url_input = gr.Textbox(
                label="🔗 Enter Youtube Video URL",
                placeholder="https://www.youtube.com/watch?v=...",
                lines=1,
                elem_id="url-input"
            )
            summarize_btn = gr.Button("🚀 Summarize")
            clear_btn = gr.Button("🧹 Clear")

        with gr.Column(scale=2):  # Right side: summary output box
            output_box = gr.TextArea(
                label="📝 Summary",
                lines=20,
                elem_id="summary-box"
            )

    # Connect button functionalities
    summarize_btn.click(fn=summarize, inputs=url_input, outputs=output_box)
    clear_btn.click(fn=lambda: ("", ""), outputs=[url_input, output_box])

demo.launch()
