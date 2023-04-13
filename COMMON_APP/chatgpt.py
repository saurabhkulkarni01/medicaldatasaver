import openai
import os
API_KEY="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"
os.environ['OPENAI_Key']=API_KEY
openai.api_key=API_KEY


def getans(query):
    response = openai.Completion.create(engine='text-davinci-003',prompt=query,max_tokens=200) 
    return response['choices'][0]['text']
