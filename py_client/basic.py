import requests
endpoint = "http://httpbin.org/"
get_response = requests.get(endpoint)
print(get_response.text)