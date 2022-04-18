# Operators

## Arithmetic operators

| Operator | Description                                                                     | 
|----------|---------------------------------------------------------------------------------|
| +        | Addition: x + y will give the sum of x and y.                                   |
| -        | Subtraction: x - y will subtract y from x.                                      |
| *        | Multiplication: x * y will give the produce of x and y.                         |
| /        | Division: x / y will give the quotient of x divided by y.                       |
| %        | Modulus: x % y will give the reminder of x divided by y.                        |
| **       | Exponent: x ** y will raise x to the power of y.                                |
| =        | Assignment: x = $y x takes the value of y.                                      |
| !=       | Negated Equality: [ $x != $y ] will return false is x equals y, true otherwise. |
```python3
#!/bin/python3

# assignment
x = 10
y = 5

print (x + y)
print (x * y)
# same for the others
```

## Comparison operators

| Operator | Description                                                                               | 
|----------|-------------------------------------------------------------------------------------------|
| ==       | Equals: x == y is true if both x and y hold the same values.                              |
| !=       | Not Equals: x != y is true if x and y hold different values.                              |
| >        | Greater than: x > y true if x holds a greater value than y.                               |
| <        | Lower than: x < y true if x holds a lower value than y.                                   |
| >=       | Greater than or equal to: x >= y true if x holds a greater value than y or if x equals y. |
| <=       | Lower than or equal to: x <= y true if x holds a lower value than y or if x equals y.     |                   

```python3
#!/bin/python3

x = 10
y = 5

print (x > y)
# same for the others
```

## Assignment operators

| Operator | Description                                                             | 
|----------|-------------------------------------------------------------------------|
| +=       | Addition: x += y will assign x the sum of x and y.                      |
| -=       | Subtraction: x -= y will assign x the subtraction of y from x           |
| *=       | Multiplication: x *= y will assign x the produce of x and y.            |
| /=       | Division: x /= y will assign x the quotient of x divided by y.          |
| %=       | Modulus: x %= y will assign x the reminder of x divided by y.           |
| **=      | Exponent: x **= y will assign x the value of x risen to the power of y. |
```python3
#!/bin/python3

# basic assignment
x = 10
y = x

# the assignment operator can be combined with the arithmetic operators:
z = 10
z += y # this expands to z = z + x, z will hold 20
print (z)
```

## Boolean operators

| Operator | Description                                            | 
|----------|--------------------------------------------------------|
| not      | Logical NOT: not false is true.                        |
| or       | Logical OR: x or y is true if either x or y is true.   |
| and      | Logical AND: x and y is true if either x or y is true. |
```python3
#!/bin/python3

x = True
y = False

print (x and  y)
print (x or  y)
print (not x)
```

## Membership operators
We can test if a value is part of a sequence in python.

| Operator | Description                                                          | 
|----------|----------------------------------------------------------------------|
| in       | x in y is true if x is in y, where y can be a list, tuple or string  |
| not in   | x not in y is true if x is not in y                                  |
```python3
#!/bin/python3

x = [1, 2, 3]           # same if x is tuple, dictionary
y = 2
z = 4

print (y in x)
print (z not in x)
# print (x not in z)    # error !

print ('p' in "python3")# True
```

### Practice
- play around with operators, compute the solutions of a 1st grade function (f(x) = ax+b).