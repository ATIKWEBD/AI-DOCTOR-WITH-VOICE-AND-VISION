import os
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
import base64

image_path="blist.jpeg"
def sext(image_path):
    image_file=open(image_path,"rb")
    return base64.b64encode(image_file.read()).decode('utf-8')

query="What is this happening to me"
model="meta-llama/llama-4-scout-17b-16e-instruct"
from groq import Groq
def analy(query,model,encoded_image):
  
  client=Groq()
  
  message=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url":f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]

  chat_completion=client.chat.completions.create(
        messages=message,
        model=model
    )

  return chat_completion.choices[0].message.content 


   