import whisper
import openai
import gradio 

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


