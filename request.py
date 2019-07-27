import requests

# URL
url = 'http://localhost:5050/api'

# Change the value of experience that you want to test
# r = requests.post(url,json={'exp':3.8,})
r = requests.post(url,json={'population':35000,})
print(r.json())
