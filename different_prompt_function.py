import whisper
import openai
import gradio as gr
import api_key

openai.api_key = api_key.OPEN_AI_API_KEY

def transcribe(filename):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    return(result["text"])

def short_summarize(result):
    content = transcribe(result)
    print
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a professor . Summarize to all inputs in 50 concise words or less"},
            {"role": "user", "content": content},
        ]
    )
    return response["choices"][0]["message"]["content"]

def long_summarize(result):
    content = transcribe(result)
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a professor . Summarize to all inputs in a short and concise paragraph"},
            {"role": "user", "content": content},
        ]
    )
    return response["choices"][0]["message"]["content"]

def bulletpoints_summarize(result):
    content = transcribe(result)
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a professor . Summarize to all inputs in bullet points"},
            {"role": "user", "content": content},
        ]
    )
    return response["choices"][0]["message"]["content"]

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=1, min_width=600):
            audio_input = gr.Audio(type="filepath")
            transcribe_button = gr.Button("Transcribe")
            short_summarize_button = gr.Button("Short Audio Summary")
            long_summarize_button = gr.Button("Long Audio Summary")
            bulletpoints_summarize_button = gr.Button("Bullet Points Summary")
            text_output = gr.Textbox()

    transcribe_button.click(transcribe, inputs=audio_input, outputs=text_output)
    short_summarize_button.click(short_summarize, inputs=audio_input, outputs=text_output)
    long_summarize_button.click(long_summarize, inputs=audio_input, outputs=text_output)
    bulletpoints_summarize_button.click(bulletpoints_summarize, inputs=audio_input, outputs=text_output)

demo.launch()

