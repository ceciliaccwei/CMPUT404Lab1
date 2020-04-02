import requests
print(requests.__version__)
response = requests.get('http://google.com/')
print(response.status_code)
response = requests.get('https://raw.githubusercontent.com/ceciliaccwei/CMPUT404Lab1/master/script.py')
print(response.content )
