# IO
## STDIN, STDOUT, STDERR
```python3
#!/usr/bin/python3
import sys

# x is a string
x = input("write a value: ")            # read from standard input
print (x)                               # (default) print to stdout
print ("fatal error", file=sys.stderr)  # print to stderr
```

## Command line arguments

```python3
#!/usr/bin/python3
import sys

# cmd line args are strings
print (len(sys.argv) - 1)               # print number arguments excluding script name
print (sys.argv[1:])                    # print arguments, also excluding script name
```

## Files
```python3
#!/usr/bin/python3

# basic open file syntax: file name and access mode
my_file = open("in.txt", "r")  # open file
print (my_file.read())              # read entire file
my_file.close()                     # release file
```
### Access modes

| Access mode | Description (b stands for binary files)                                                                                                  | 
|-------------|------------------------------------------------------------------------------------------------------------------------------------------|
| r, rb       | Read-only [binary]                                                                                                                       |
| r+, rb+     | Read and write [binary]                                                                                                                  |
| w, wb       | Write only [binary]; Creates file if it does not exist; Overwrites file if it exists                                                     |
| w+, wb+     | Write and read [binary]; Creates file if it does not exist; Overwrites file if it exists                                                 |
| a, ab       | Append [binary]; Appends to existing file; Creates new file if it does not exist                                                         |
| a+, ab+     | Append and read [binary]; Appends to existing file; Creates new file if it does not exist; The new file is opened in write and read mode |
More examples:
```python3
#!/usr/bin/python3
import sys

# Open a file
my_file = open("out.txt", "w")
my_file.write("abcd")

# Close my_file
my_file.close()

# $ cat out.txt
```

```python3
#!/usr/bin/python3

# Create in.txt file
# add to it: abcdefghijklmnopqrstuvwxyz
my_file = open("in.txt", "r+")
my_str = my_file.read(4)
print ("First 4 letters : ", my_str)  # abcd

# Print current position
position = my_file.tell()
print ("Current file position : ", position) # 4

# Do a seek close to the end
# first arg is offset, second is 0 (start), 1 (current), 2 (end)
position = my_file.seek(23, 0)               
my_str = my_file.read(3)
print ("Last 3 letters : ", my_str)          # xyz

my_file.close()
```

```python3
#!/usr/bin/python3

# Same in.txt file
my_file = open("in.txt", "a")
my_file.write("0123456789")
my_file.close()

my_file = open("in.txt", "r")
print("Alphabet + numbers: ", my_file.read())
my_file.close()
```

## REST APIs
```python3
#!/usr/bin/python3
import requests, json

# check this: https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/

url = "https://api.coinbase.com/v2/currencies"
response = requests.request("GET", url)
json_response = json.loads(response.text)          # this is traversable now
print( json_response)
```