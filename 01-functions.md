# Functions

Functions are a way to reuse code.
You can pass data to a function. These are called parameters or arguments.
The function can return data.

```python
def my_function(a, b, c):
    return a + (b * c)

print(my_function(1,2,3))
```

## What can be passed in?
Anything:
```python
my_func(1, 3, "a", [1,2,3], {'a': 3}, ('op', 'noop')) #etc
```

In a script, functions have access to variables defined outside:
```python
a = 2
def my_function2(b):
    return a * b

print(my_function2(10))
```
You should handle these situations with care, since they can be hard to debug.

### Functions can return multiple results:
```python
def divide(a, b):
    quotient = a // b
    modulus - a % b
    return (quotient, modulus)

print(divide(5, 2))
```

Python functions can have default values for arguments (as seen previously with `range`, `print` etc):
```python
def exponentiate(base, exponent = 2):
    return base ** exponent

print(exponentiate(10))
print(exponentiate(10, 3))
```

When calling a function, you can use **keyword** arguments to give the arguments in any order you like:
```python
def concatenate(middle, start, end):
    return start + middle + end

print(concatenate(start = "Hello", middle = "World", end = "!"))
```
# Varargs
Python functions can be called with a variable number of arguments. To do so, the function has to be defined with the following syntax:
```python
def multiply_all(multiplier, *nums):
    return [num * multiplier for num in nums] # nums here is passed as a list.

print(multiply_all(multiplier = 2, 1 , 2 , 3 , 4 , 5 , 6))
```

Simmilarly, functions can be called with an arbitrary number of keyword arguments. Here's the syntax for doing so:
```python
def greet(**kwargs): # typical python notation for variable keyword arguments
    print(f"Hello {kwargs['name']}") # When using f-strings, you must use different types of quotes inside and outside the {}

greet(name = "Bob", neighbour = "Alice")
```


### Positional only arguments
When defining a function, you can specify that it can only be called with positional arguments, not keyword arguments by using `, /` after all the arguments:
```python
def position_only(a, b, /):
    return str(a) + str(b)

print(position_only(3, 4))
print(position_only(b = 3, a = 4)) #error
```

### Keyword only arguments
You can also specify that your function should only be called with keyword arguments by adding `* ,` before arguments:
```python
def keyword_only_divide(*, divident, divisor):
    return divident / divisor

print(keyword_only_divide(divident = 5, divisor = 2))
print(keywork_only_divide(5, 2)) # error
```
This can help avoid confusion when calling the function, since it forces you to acknowledge which argument is which.

### Mixing the two
You can mix the two constraints together by using both `/` and `*`. Arguments before the slash are position only, and arguments after the asterisk are keyword only:
```python
def my_function(a, b, /, c, *, d, e):
  print(a + b + c + d + e)

my_function(5, 6, c = 7, d = 8, e = 9)
my_function(5, 6, 7, d = 8, e = 9)
```

## Practice
1. Create a function that takes a filename and an action. The action should be 'read' by default.
if the action is 'read': return a list of all the lines in the file
if the action is 'write': write "Hello, World!" to the file and returns `None`

2. Create a function that *returns* the weather for a city.
print the weather for the following cities:
['Bucharest', 'Cluj', 'Iasi']
Use the code from last course's 08-http

3. Create a function that checks if a dict can be reversed.
(if dict['a'] is 1 in the original dict, then dict[1] is 'a' in the reversed dict)
A dict is reversible if all *values* are unique.
Your function should take a single dict as a parameter and return `True` if it can be reversed, `False` otherwise.
hint: use the `set` datatype to 

4. Create a function that reverses a dict.
It should first check if it is reversible. If not, return `None`
hint: try to use a *dictionary* comprehension: [link](https://www.geeksforgeeks.org/python-dictionary-comprehension/)