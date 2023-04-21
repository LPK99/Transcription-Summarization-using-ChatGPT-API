import whisper
import openai
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
    prompt = "You are a professor .Summarize to all inputs in bullet points"
    return request_gpt(prompt, result)