import requests

ur_uhq_prompt = "how many thousands of black people are there in the world"

res = requests.post("http://localhost:5000/api/gemini", json={"prompt": ur_uhq_prompt})
print(res.json()["deepthoughts"])
