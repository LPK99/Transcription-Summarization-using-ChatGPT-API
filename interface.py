from prompt_function import transcribe, short_summarize, long_summarize, bulletpoints_summarize
import gradio as gr

#The user interface of the gradio web app
with gr.Blocks() as ui:
    with gr.Tab("Batch"):
        with gr.Column(scale=1):
            with gr.Row():
                audio_input = gr.Audio(type="filepath")
                with gr.Column(scale=1, min_width=500):
                    transcribe_button = gr.Button("Transcribe")
                    short_summarize_button = gr.Button("Short Audio Summary")
                    long_summarize_button = gr.Button("Long Audio Summary")
                    bulletpoints_summarize_button = gr.Button("Bullet Points Summary")
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
                    bulletpoints_summarize_button_rt = gr.Button("Bullet Points Summary")
        with gr.Column(scale=1):
            text_output_rt = gr.Textbox("Summary")
            transcription_output_rt = gr.Textbox("Transcript")
            #exit_button = gr.Button("EXIT UI")
    with gr.Tab("Text"):
        with gr.Column(scale=1):
            with gr.Row():
                text_input = gr.Textbox()
                with gr.Column(scale=1, min_width=500):
                    short_summarize_button_text = gr.Button("Short Audio Summary")
                    long_summarize_button_text = gr.Button("Long Audio Summary")
                    bulletpoints_summarize_button_text = gr.Button("Bullet Points Summary")
        with gr.Column(scale=1):
            text_output_textbox = gr.Text("Summary")
        

    transcribe_button.click(transcribe, inputs=audio_input, outputs=transcription_output)
    short_summarize_button.click(short_summarize, inputs=audio_input, outputs=text_output)
    long_summarize_button.click(long_summarize, inputs=audio_input, outputs=text_output)
    bulletpoints_summarize_button.click(bulletpoints_summarize, inputs=audio_input, outputs=text_output)

    transcribe_button_rt.click(transcribe, inputs=audio_realtime_input, outputs=transcription_output_rt)
    short_summarize_button_rt.click(short_summarize, inputs=audio_realtime_input, outputs=text_output_rt)
    long_summarize_button_rt.click(long_summarize, inputs=audio_realtime_input, outputs=text_output_rt)
    bulletpoints_summarize_button_rt.click(bulletpoints_summarize, inputs=audio_realtime_input, outputs=text_output_rt)

    short_summarize_button_text.click(short_summarize, inputs=text_input, outputs=text_output_textbox)
    long_summarize_button_text.click(long_summarize, inputs=text_input, outputs=text_output_textbox)
    bulletpoints_summarize_button_text.click(bulletpoints_summarize, inputs=text_input, outputs=text_output_textbox)

ui.launch()