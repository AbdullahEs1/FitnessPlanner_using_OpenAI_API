from openai import OpenAI

api_key = "" # paste your key here

client = OpenAI(api_key=api_key)

def processInput(prompt):
    try:
        response = client.responses.create(
            model="gpt-4o",
            input=prompt
        )
        return response.output_text
    except Exception:
        text = "THIS IS A RESPONSE FOR DEBUGGING, NOT REAL RESPONSE FROM OPENAI API. Check if your key is working."
        return text




