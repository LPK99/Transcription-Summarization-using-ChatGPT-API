import whisper
import openai
import gradio as gr
import api_key



def request_gpt(prompt, text):
    openai.api_key = api_key.OPEN_AI_API_KEY
    content = transcribe(text)
    print(content)
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "system", "content": prompt}, {"role": "user", "content": content}]
    )
    print(response["choices"][0]["message"]["content"])
    return response["choices"][0]["message"]["content"]

def transcribe(filename):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    return(result["text"])

def short_summarize(result):
    return request_gpt('You are a professor . Summarize to all inputs in 50 concise words or less', result)

def long_summarize(result):
    prompt = "You are a professor .Summarize to all inputs in a short and concise paragraph"
    return request_gpt(prompt, result)

def bulletpoints_summarize(result):
    prompt = "You are a professor .Summarize to all inputs in a short and concise paragraph"
    return request_gpt(prompt, result)


with gr.Blocks() as demo:
    with gr.Tab("Batch"):
        with gr.Column(scale=1):
            with gr.Row():
                audio_input = gr.Audio(type="filepath")
                with gr.Column(scale=1, min_width=500):
                    transcribe_button = gr.Button("Transcribe")
                    short_summarize_button = gr.Button("Short Audio Summary")
                    long_summarize_button = gr.Button("Long Audio Summary")
                    bulletpoints_summarize_button = gr.Button("Bullet Points Summaryyyy")
        with gr.Column(scale=1):
            text_output = gr.Textbox("Summary")
            #exit_button = gr.Button("EXIT UI")
            transcription_output = gr.Textbox("Transcript")    
    with gr.Tab("Real-time"):
        with gr.Column(scale=1):
            with gr.Row():
                audio_realtime_input = gr.Audio(source="microphone" ,type="filepath")
                with gr.Column(scale=1, min_width=500):
                    transcribe_button_rt = gr.Button("Transcribe")
                    short_summarize_button_rt = gr.Button("Short Audio Summary")
                    long_summarize_button_rt = gr.Button("Long Audio Summary")
                    bulletpoints_summarize_button_rt = gr.Button("Bullet Points Summaryyyy")
        with gr.Column(scale=1):
            text_output_rt = gr.Textbox("Summary")
            transcription_output_rt = gr.Textbox("Transcript")
            #exit_button = gr.Button("EXIT UI")    

    transcribe_button.click(transcribe, inputs=audio_input, outputs=transcription_output)
    short_summarize_button.click(short_summarize, inputs=audio_input, outputs=text_output)
    long_summarize_button.click(long_summarize, inputs=audio_input, outputs=text_output)
    bulletpoints_summarize_button.click(bulletpoints_summarize, inputs=audio_input, outputs=text_output)

    transcribe_button_rt.click(transcribe, inputs=audio_realtime_input, outputs=transcription_output_rt)
    short_summarize_button_rt.click(short_summarize, inputs=audio_realtime_input, outputs=text_output_rt)
    long_summarize_button_rt.click(long_summarize, inputs=audio_realtime_input, outputs=text_output_rt)
    bulletpoints_summarize_button_rt.click(bulletpoints_summarize, inputs=audio_realtime_input, outputs=text_output_rt)

demo.launch()

