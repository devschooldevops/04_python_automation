# PIP and packages
We can group modules into packages.<br>
PIP is the python package manager. We can get packages from the internet with it.
```commandline
$ pip3 install <package_name>
```

# REST APIs
## GET example
```python3
#!/usr/bin/python3
import requests, json

# check this: https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/

url = "https://api.coinbase.com/v2/currencies"
response = requests.request("GET", url)
json_response = json.loads(response.text)          # this is traversable now
print( json_response)
```
## POST example

```
#!/usr/bin/python3
import requests, json

url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(url, json=todo)
json_response = response.json()         # this is traversable now
print( json_response)
```
## DELETE example

```
#!/usr/bin/python3
import requests, json

url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(url)
json_response = response.json()
status_code = response.status_code
print( json_response)
print( status_code) 
```

## PUT example
```
#!/usr/bin/python3
import requests, json

url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(url, json=todo)
json_response = response.json()         # this is traversable now
print( json_response)
```
## PATCH example 
```
#!/usr/bin/python3
import requests, json

url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Wash car"}
response = requests.patch(url, json=todo)
json_response = response.json()         # this is traversable now
print( json_response)
```