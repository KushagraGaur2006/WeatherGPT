from groq import Groq
import os 
from dotenv import load_dotenv
load_dotenv()
def main():
    SYSTEM_PROMPT="You are WeatherGPT and you have access to Weather Data as context and you are only allowed to answer weather queries and any greetings and for any other questions you have to say no specially against questions involving code and maths"
    history=[{"role":"system","content":SYSTEM_PROMPT}]
    client=Groq(api_key=os.getenv("GROQ_API_KEY"))
    while True:
        a=str(input("Enter User Query"))
        history.append({"role":"user","content":a})
        stream=client.chat.completions.create(messages=history,stream=True,model="openai/gpt-oss-20b")
        for chunk in stream:
            print(chunk.choices[0].delta.content or "")

main()
