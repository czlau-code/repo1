import requests

# requests.adapters.DEFAULT_RETRIES=5
url = "http://localhost:8000/tclapi/hello2"
myobj = {"name": "Yoda"}
x = requests.post(url, json=myobj)
print(x.text)
