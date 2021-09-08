import requests

# Get the version of the requests library
print(requests.__version__)

# Get the Google homepage
print(requests.get("http://google.com/"))

# Get scripts source code from GitHub and download
code = requests.get("https://raw.githubusercontent.com/zhininghjl/404_lab_1/master/script.py"
).content
print(code)
open('lab_1_downloaded.py', 'wb').write(code)