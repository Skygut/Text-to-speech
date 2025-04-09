import torch
from TTS.api import TTS
import gradio as gr

device = "cuda" if torch.cuda.is_available() else "cpu"


# def generate_audio(text="A journey of a thousand miles begins with a single step."):
#     tts = TTS(model_name="tts_models/en/ljspeech/fast_pitch").to(device)
#     tts.tts_to_file(text=text, file_path="outputs/output.wav")
#     return "outputs/output.wav"


# def generate_audio(text="A journey of a thousand miles begins with a single step."):
#     tts = TTS(model_name="tts_models/en/vctk/vits").to(device)
#     tts.tts_to_file(text=text, speaker="p225", file_path="outputs/output.wav")
#     return "outputs/output.wav"


# def generate_audio(text="A journey of a thousand miles begins with a single step."):
#     tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts").to(device)
#     tts.tts_to_file(
#         text=text, speaker="male-en-1", language="en", file_path="outputs/output.wav"
#     )
#     return "outputs/output.wav"


def generate_audio(text="A journey of a thousand miles begins with a single step."):
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts").to("cpu")

    # Beispiel: einen gültigen Speaker ausgeben
    print("Speakers:", tts.speakers)

    tts.tts_to_file(
        text=text,
        speaker="male-pt-3\n",  # Hier durch gültigen Namen ersetzen
        language="en",
        file_path="outputs/output.wav",
    )
    return "outputs/output.wav"


print(generate_audio())

demo = gr.Interface(
    fn=generate_audio,
    inputs=[
        gr.Text(label="Text"),
    ],
    outputs=[gr.Audio(label="Audio")],
)
demo.launch()
