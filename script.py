import requests

# Get the version of the requests library
print(requests.__version__)

# Get the Google homepage
print(requests.get("http://google.com/"))

# Get scripts source code from GitHub
print(requests.get("https://raw.githubusercontent.com/zhininghjl/404_lab_1/master/script.py"
).content)
