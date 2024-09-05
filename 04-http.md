# Working with HTTP requests

We'll be using the `requests` module to send http calls to various APIs.  
Make sure you have it installed by going to the repl and importing `requests`

```bash
$ python3
>>> import requests
```

## Getting the weather

wttr.in is a free and unauthenticated https API we'll be using to get the weather.

Let's start by sending them a simple GET request:

```python
import requests

resp = requests.get('https://wttr.in')
if resp.status_code == 200: # You should make it a habit to check the status code of a request instead of going straight for the body.
    print(resp.text)
else:
    print(f'Unexpected status code {resp.status_code}!')
```

Let's use the [github docs](https://github.com/chubin/wttr.in) to figure out how to make the output smaller.  
We can see that by adding `?format=3`, the weather app will return a one liner.

You could do it like this:
```python
import requests

resp = requests.get('https://wttr.in/?format=3')
if resp.status_code == 200: 
    print(resp.text)
else:
    print(f'Unexpected status code {resp.status_code}!')
```

But the following is more configurable, since you can pass in a dict:
```python
import requests

resp = requests.get('https://wttr.in', params={'format': 3})
if resp.status_code == 200: 
    print(resp.text)
else:
    print(f'Unexpected status code {resp.status_code}!')
```
[Here](https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request) you can find more info on your options when sending requests and reading responses.

Notably, to send a json body:
```python
import requests

body = {"field1" : value1, "field2": value2}
resp = requests.post('https://sample_post_api.com/add-data', data=body)
if resp.status_code == 200: 
    print(resp.text)
else:
    print(f'Unexpected status code {resp.status_code}!')

```
## Practice:
1. Send a request to wttr.in for a city of your choice. (check out the [github docs](https://github.com/chubin/wttr.in) for how to specify a city).  
Ask wttr.in to give you back the weather in your native language.   
Get the city from the command line.  
2. http.cat is a web app that can give you back an image of a cat for each HTTP status code. [Http cats](https://http.cat/).  
Take the status code of the response from wttr.in and send it to http.cat. Check out the website for where to put the status code.  
Write the response of the request to http.cat to a jpeg file, and check out the image! (Access the raw response bytes using `resp.content`. The response body will be binary, not text! have a look at [the docs](https://docs.python.org/3/library/functions.html#open) to figure out how to write a binary file)

3. Pretend you don't know all images on http.cat are of type jpeg.  
Look at the response headers (`resp.headers` is a dict) for the `"Content-type"` header to determine the extension of the image.