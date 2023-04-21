import whisper
import openai
import gradio as gr
import numpy as np



def transcribe(filename):
    model = whisper.load_model("base")
    #print(filename)
    #audio = whisper.load_audio(filename)
    #convert_to_array = np.array(filename, dtype=np.int16)
    #print(convert_to_array)
    result = model.transcribe(filename[1])
    return(result["text"])

def short_summarize(result):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a professor . Summarize to all inputs in 50 concise words or less"},
            {"role": "user", "content": result["text"]},
        ]
    )
    return response["choices"][0]["message"]["content"]

def long_summarize(result):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a professor . Summarize to all inputs in a short and concise paragraph"},
            {"role": "user", "content": result["text"]},
        ]
    )
    return response["choices"][0]["message"]["content"]

def bulletpoints_summarize(result):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a professor . Summarize to all inputs in bullet points"},
            {"role": "user", "content": result["text"]},
        ]
    )
    return response["choices"][0]["message"]["content"]

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=1, min_width=600):
            audio_input = gr.Audio()
            transcribe_button = gr.Button("Submit")
            text_output = gr.Textbox()

    transcribe_button.click(transcribe, inputs=audio_input, outputs=text_output)

demo.launch()

