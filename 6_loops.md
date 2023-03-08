# Loops
Python provides us for and while loops for us to create repetitive structures of code.

### For
```text
for iterating_var in sequence:
   statements(s)
```
Example:
```python
#!/bin/python3

l = [1, 2, 3]

for num in l:
    print(num)
# notice the indentation !!!

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    print ('Current fruit :', fruits[index])

for letter in "word":
    print(letter)

my_dict = {'a': 1, 'b': 2}
for key in my_dict.keys():
    print(my_dict[key])
```

### While
```text
while expression:
   statement(s)
```
Example:
```python
#!/bin/python3

a = 0
while a < 9:
   print (a)
   a += 1
# notice the indentation !!!
```

## Loop control

There are some mechanisms we can use to alter loop control, such as **break** and **continue** statements.
Below are some examples:

```python
#!/bin/python3

a = 0
while True:
   print (a)
   a += 1
   if a == 10:
       break
# stop when a reaches value 10

l = [1, 2, 3, 4, 5, 6, 7]

for num in l:
    if num % 2 == 0:
        continue
    print(num)
# print only odd numbers
```

## Practice

Compute the fibonacci sequence for a given input.
Compute the greatest common denominator for two given numbers.