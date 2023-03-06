import openai
import os
API_KEY="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"
os.environ['OPENAI_Key']=API_KEY
openai.api_key=API_KEY


def getans(query):
    # print(query)
    response = ""
    response = openai.Completion.create(engine='text-davinci-003',prompt=query,max_tokens=200)
    # print(response)
    return response['choices'][0]['text']