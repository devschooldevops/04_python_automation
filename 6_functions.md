# Functions
Functions are reusable pieces of code, similar to those in bash.
```text
def function_name( [parameters] ):
   [statement(s)]
   [return [expression]]
```
In python functions are more configurable:

### Pass by reference
Parameters are passed by reference, meaning changes in parameters are reflected outside the function scope:

```python
#!/bin/python3

def change_me(parameter_list):
    """This changes a passed list into this function"""
    print("Values inside the function before change: ", parameter_list)

    parameter_list[2] = 50
    print("Values inside the function after change: ", parameter_list)
    return # nothing


my_list = [10, 20, 30]
change_me(my_list)
print("Values outside the function: ", my_list)
```

### Function Arguments
We have some ways to play with function arguments and add some functionality:
```python
#!/bin/python3

def print_data( x, y = 2 ):
   print (x ** y)
   return

# x is a required parameter, it must always be supplied to the function
print_data( y = 3, x = 2 )     # notice we can rearrange parameters by naming them (keyword args)
print_data( x = 5 )            # notice we have can have default values for parameters
```
We also have variable parameters functions:
```text
def function_name( [formal_args,] *var_args_tuple ):
   [statement(s)]
   [return [expression]]
```
```python
#!/bin/python3

def print_data( arg, *tup):
   print (arg)
   
   for var in tup:
      print (var)
       
   print ()    
       
   return

print_data(1)
print_data(1, 2, 3, 4, 5, 6)
```

### Return statement
We can return multiple values from a function:
```python
#!/bin/python3

def print_data():
   return 1, 2, [3, 4]

a, b, l = print_data()
print (a)
print (b)
print (l)
```