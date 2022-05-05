# Decision-Making
If statement syntax:
```text
if expression1:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   else
      statement(s)
elif expression4:
   statement(s)
else:
   statement(s)
```
Example from internet:
```python
# !/usr/bin/python3

num = int(input("enter number"))
if num % 2 == 0:
   if num % 3 == 0:
      print ("Divisible by 3 and 2")
   else:
      print ("divisible by 2 not divisible by 3")
else:
   if num % 3 == 0:
      print ("divisible by 3 not divisible by 2")
   else:
      print  ("not Divisible by 2 not divisible by 3")
```
Notice the indentation, this is how blocks of code (scopes) are delimited in python.