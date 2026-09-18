import requests
import json

url="http://localhost:11434/api/generate"

data ={
    "model":"llama3.2",
    "prompt":"Tell me a Short Story and Make It Funny."
}

response=requests.post(url,json=data,stream=True)

# Check The Response Status

if response.status_code==200:
    print("Generated Text:",end="",flush=True)
    # Iterate Over the Streaming flow
    
    for lines in response.iter_lines():
        if lines:
            # decode the line and parse the json
            decode_line=lines.decode("utf-8")
            result=json.loads(decode_line)
            # get the text from the response
            generate_text=result.get("response","")
            print(generate_text,end="",flush=True)
            
else:
    print("Error",response.status_code,response.text)