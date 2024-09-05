# Questions from last time?

<details>
  <summary>Homework solutions</summary>
  
## basic io
```python
import sys
in_file = sys.argv[1]
out_file = sys.argv[2]

name = input("Please enter your name")

greet = None
with open(in_file) as f:
    greet = f.read()
with open(out_file, "w") as f:
    f.write(greet + name)
```

## loops
```python
num = int(input("Please enter a number"))

divisors = [x for x in range(2, num) if num % x == 0]
print(len(divisors))
```

### point 2
```python
num = int(input("Please enter a number"))
for x in range(2, num):
    print(len([y for y in range(2, x) if x % y == 0]))
```
</details>

## Recap

We've seen variable types:
```python
x = 1
s = "abc"
my_list = [1, 2, 3, 4]
my_dict = {'a': 1, 'b': 2}
my_set = {'a', 'b', 'c'}
my_tuple = (1, 2, 3, 4)
```

We did maths and logic:
```python
print(1 + 2)
print(5 // 2)

print(not True and False)
print("py" in "python3")
```

We did logic:
```python
x = 10
parity = "even" if x % 2 == 0 else "odd"

if x % 3 == 0:
    print("X is divisible by 3")
```

IO and loops:
```python
import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    for index, line in enumerate(f):
        print(f"this is the line {line} at index {index}")
```

