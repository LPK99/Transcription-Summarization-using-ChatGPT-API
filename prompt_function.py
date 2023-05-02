import whisper
import openai

#take the prompt and text content as parameter
#call the chatgpt api and return the response
open_ai_api_key = ''

def request_gpt(prompt, text):
    openai.api_key = open_ai_api_key
    content = transcribe(text)
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "system", "content": prompt}, {"role": "user", "content": content}]
    )
    return response["choices"][0]["message"]["content"]

def getAPIkey(apikey):
    global open_ai_api_key
    open_ai_api_key = apikey

#transcribe the file into text
def transcribe(filename):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    return(result["text"])
    

#declare the prompt and call the request_gpt function

def short_summarize(result):
    return request_gpt('You are a college student . Summarize to all inputs in 50 concise words or less', result)

def long_summarize(result):
    prompt = "You are a college student .Summarize to all inputs in a short and concise paragraph"
    return request_gpt(prompt, result)

def bulletpoints_summarize(result):
    prompt = "You are a college student .Summarize to all inputs in a short and concise paragraph"
    return request_gpt(prompt, result)


