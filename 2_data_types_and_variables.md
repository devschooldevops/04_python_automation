# Variables
```python3
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
```python3
#!/bin/python3

integer = 1
floating_point = 2.0
complex_number = complex(1, 2)
num = int("123", 10)

print (integer)
print (floating_point)
print (complex_number)
print (num)
```

## String
Strings in Python are identified as a contiguous set of characters represented in the quotation marks. 
Subsets of strings can be taken using the slice operator ([ ] and [:] ) 
with indexes starting at 0 in the beginning of the string and working their 
way from -1 to the end.
```python3
#!/bin/python3

hello = 'Hello World!'

print (hello)          # Prints complete string
print (hello[0])       # Prints first character of the string
print (hello[-1])      # Prints last character of the string
print (hello[2:4])     # Prints characters starting from 3rd to 4th
print (hello[1:])      # Prints string starting from 2nd character ('e')
print (hello * 2)      # Prints string two times
print (hello + "TEST") # Prints concatenated string

# string formatting
print ("We can add strings %s, decimal numbers %d" % ("abcd", 2)) 

# triple quote
long_string = """
very
very
long
string
"""
print (long_string)

print(len(hello))
```

## Lists
A list contains items separated by commas and enclosed within square brackets. Each element can be of any type (even another list).
```python3
#!/bin/python3

sample_list = [ 'a', 22 , 'h', 4.20, 'asdf', [2, 3] ]

print (sample_list)                        # Prints complete list
print (sample_list[0])                     # Prints first element of the list
print (sample_list[-1])                    # Prints last element of the list
print (sample_list[1:3])                   # Prints elements starting from 2nd till 3rd 
print (sample_list[2:])                    # Prints elements starting from 3rd element
print (sample_list * 2)                    # Prints list two times
print (sample_list[0:3] + sample_list[5:]) # Prints concatenated lists

sample_list[1] = 21
print(sample_list[1])    # 21, not 22, this is an update

del sample_list[1]
print(sample_list[1])    # prints h, 21 has been removed

sample_list.append('abcd')
print(sample_list[-1])   # abcd

sample_list.insert(1, 22)
print(sample_list[1])    # 22 is back !!

sample_list.reverse()
sample_list.reverse()    # double revert, same list

sample_list.remove(22)
print(sample_list)       # removed 22
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
del sample_tuple[0]                          # same, not possible

print(len(sample_tuple))                     # 6 elements
```

## Dictionary
Dictionaries hold pairings of key -> value type. Keys are usually numbers or strings and values can be literally anything.
```python
#!/bin/python3

my_dict = {'a': 2}
my_dict.clear()              # clear all pairs

my_dict['a'] = 2
my_dict['one'] = "asdf"
my_dict[2] = "abcd"
my_dict[223] = [1, 2, 3, 4]

print (my_dict['one'])       # Prints value for 'one' key
print (my_dict[2])           # Prints value for 2 key
print (my_dict)              # Prints complete dictionary
print (my_dict.keys())       # Prints all the keys
print (my_dict.values())     # Prints all the values
print (my_dict[123])         # Generates error

print(len(my_dict))
print('a' in my_dict)        # True

another_dict = {'b': 3}
my_dict.update(another_dict)
print('b' in my_dict)        # True
```