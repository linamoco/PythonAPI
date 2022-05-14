import requests
import time
import json
url = "https://playground.learnqa.ru/ajax/api/longtime_job"
response = requests.get(url)
print(response.text)
token = json.loads(response.text)["token"]
seconds = json.loads(response.text)["seconds"]

response_before_token = requests.get(url, params={"token":token})
print(response_before_token.text)
time.sleep(float(seconds))

response_after_token = requests.get(url, params={"token":token})
print(response_after_token.text)
