# Variables
```python
#!/bin/python3

# basic variables
integer = 100
number = 1000.0
string = "John"

print (integer)
print (number)
print (string)

# multiple assignment, this is very useful
# in this way a function can return multiple values in python, we'll see that later
a, b, c = 1, 2, "john"
```

## Numbers
In python, we have number types int, float and complex.
```python
#!/bin/python3

integer = 1
floating_point = 2.0
complex_number = complex(1, 2)

print (integer)
print (floating_point)
print (complex_number)
```

## String
Strings in Python are identified as a contiguous set of characters represented in the quotation marks. 
Subsets of strings can be taken using the slice operator ([ ] and [:] ) 
with indexes starting at 0 in the beginning of the string and working their 
way from -1 to the end.
```python
#!/bin/python3

hello = 'Hello World!'

print (hello)          # Prints complete string
print (hello[0])       # Prints first character of the string
print (hello[-1])      # Prints last character of the string
print (hello[2:4])     # Prints characters starting from 3rd to 4th
print (hello[1:])      # Prints string starting from 2nd character ('e')
print (hello * 2)      # Prints string two times
print (hello + "TEST") # Prints concatenated string
```

## Lists
A list contains items separated by commas and enclosed within square brackets. Each element can be of any type (even another list).
```python
#!/bin/python3

sample_list = [ 'a', 22 , 'h', 4.20, 'asdf', [2, 3] ]

print (sample_list)                        # Prints complete list
print (sample_list[0])                     # Prints first element of the list
print (sample_list[-1])                    # Prints last element of the list
print (sample_list[1:3])                   # Prints elements starting from 2nd till 3rd 
print (sample_list[2:])                    # Prints elements starting from 3rd element
print (sample_list * 2)                    # Prints list two times
print (sample_list[0:3] + sample_list[5:]) # Prints concatenated lists
```

## Tuples
The main difference between lists and tuples are − Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, 
while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. 
Tuples can be thought of as read-only lists.
```python
#!/bin/python3

sample_tuple = ( 'a', 22 , 'h', 4.20, 'asdf', [2, 3] )

print (sample_tuple)                         # Prints complete tuple
print (sample_tuple[0])                      # Prints first element of the tuple
print (sample_tuple[-1])                     # Prints last element of the tuple
print (sample_tuple[1:3])                    # Prints elements starting from 2nd till 3rd 
print (sample_tuple[2:])                     # Prints elements starting from 3rd element
print (sample_tuple * 2)                     # Prints tuple two times
print (sample_tuple[0:3] + sample_tuple[5:]) # Prints concatenated tuple

sample_tuple[0] = 'b'                        # will generate error
```

## Dictionary
Dictionaries hold pairings of key -> value type. Keys are usually numbers or strings and values can be literally anything.
```python
#!/bin/python3

my_dict = {'a': 2}
my_dict['one'] = "asdf"
my_dict[2] = "abcd"
my_dict[223] = [1, 2, 3, 4]

print (my_dict['one'])       # Prints value for 'one' key
print (my_dict[2])           # Prints value for 2 key
print (my_dict)              # Prints complete dictionary
print (my_dict.keys())       # Prints all the keys
print (my_dict.values())     # Prints all the values
print (my_dict[123])         # Generates error
```

## Utilities
For these data types, there are a lot of utilities in python.<br>
Some examples:
```python
x = -2
print(abs(x)) # absolute values, there are also utility functions for square root, logarithm etc.

y = [1, 2, 3]
print(min(y)) # there is also max, avg etc.
print(y.reverse()) # there is also sort, count, append, remove etc.
```
Before going on a crusade to rewrite python, please check the utility functions for your data types.

### Practice
- Play around with this types