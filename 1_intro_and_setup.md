# Python 3
## Install python 3
Python is an interpreted scripting language that offers more complex features than bash.
We can write scripts, or we can use the python repl (command line).
We need python for the python course.
```bash
$ python3 --version
$ pip3 --version
```
If this returns noting good, then install python3.
```bash
$ sudo yum install python3, python3-pip # pip is the python package manager, with it we can get python packages from the internet
```
Try it out:
```python3
$ python3
>>> from datetime import date
>>> print(date.today())
2022-05-05
# (Ctr + D or exit() to quit)
>>> exit()
```
or write it as a script (my_script.py):
```python3
#!/usr/bin/python3

from datetime import date

print(date.today())
```
```bash
$ chmod +x my_script.py
$ python3 my_script.py
```