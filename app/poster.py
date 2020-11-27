import requests

r = requests.post("https://httprecorder.herokuapp.com/", data={'number': 12524, 'type': 'issue', 'action': 'show'})
print(r.status_code, r.reason)
print(r.text)
