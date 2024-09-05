# Various other things you should be aware of

## Exception handling
Python has a mechanism for raising and catching exceptions.  
If a piece of code can throw exceptions, you should wrap it in a try block:

```python
try:
    print(risky_function(argument))
except:
    print("exception occured!")
```
We won't dive into handling specific types of exceptions in this course.
More info on exception handling [here](https://www.geeksforgeeks.org/python-exception-handling/)

A pattern you might see a lot of or even use is the following:
```python
try:
    risky_code()
except:
    pass
```
It means that in case an exception happens, don't do anything. It's not a healthy pattern to take into production, but it can help get past exceptions when one time scripting.
### Raising exceptions

```python
def divide(divident, divisor):
    if divisor == 0:
        raise ValueError("Divisor cannot be 0")
    return divident / divisor

```
Built in error types [here](https://docs.python.org/3/library/exceptions.html)

## The `type` function
You can pass a variable or object to the `type` function and it will tell you what you're working with.
```python
>>> a = 1
>>> type(a)
<class 'int'>
>>> l = []
>>> type(l)
<class 'list'>
>>> type({})
<class 'dict'>
```

## The `dir` function

Returns a list of all available methods of an object passed as a parameter.
```python
>>> dir([])
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
```
In the above example, we have a list of all available methods of a list object. Methods with `__method_name__` should not be used.  