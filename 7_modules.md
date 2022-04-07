# Modules
We can pack our reusable code into modules. Modules are simple python files with functions and other stuff. <br>
Example: we can write a python file with a function that adds 2 integers and use this function in another python script.
```python
#!/bin/python3

# add.py

def add(a, b):
   return a + b
```

```python
#!/bin/python3

# script.py

from add import add   # best way to import
# from add import *

print (add(1, 2))
```

### Where are my modules at?
Python looks for modules in the current directory or in PYTHONPATH (which you can edit).

## PIP and packages
We can group modules into packages.<br>
PIP is the python package manager. We can get packages from the internet with it.
```commandline
$ pip3 install numpy
```

### Practice
- We can redo some previous exercise, but we use modules for grouping functions.