# Working with strings

## f-strings

It's very easy to format strings using f-strings. Here's an example:
```python
num = 25 
print(f"It took {num} years to get here")

```

Here's an earlier example rewritten to use f-strings
```python
dict = {'cat': 'meow', 'dog': 'bark', 'cow': 'moo'}
for animal, sound in dict.items():
    print(f"{animal} says {sound}")
# This will print cat says meow etc. 
```
f-strings can also evaluate expressions:
```python
print(f"The result is {1 + 2}") # Prints The result is 3
```

You can also get the same result by using the `.format` method:
```python
num = 25
s = "it took {} years to get here"
print(s.format(num))
```
In the wild, when reading other people's code you'll see string concatenation, f-strings and other methods of formatting strings. Check out the [cheatsheet](https://www.pythoncheatsheet.org/cheatsheet/string-formatting) for more.

## String methods

Strings have lots of methods to make working with them easier.

Capitaliziation:
```python
text = "Hello, world"
print(text.upper()) # HELLO, WORLD
print(text.lower()) # hello, world
```


You can remove whitespace at the start and end of a string:
```python
print("    hello    \n".strip()) # prints hello
```
You can remove only the left or right whitespace:
```python
print("    hello    ".lstrip()) # prints hello    #
print("    hello    ".rstrip()) # prints     hello#
```

You can join and split strings:
```python
print("one two three".split(" ")) # ["one", "two", "three"]
print("one two three".split())    # ["one", "two", "three"]
print("oneABCtwoABCthree".split("ABC")) # ["one", "two", "three"]

print(" ".join(["one", "two", "three"])) # "one two three"
print("".join(["one", "two", "three"])) # "onetwothree"
```

Replacing with .replace:
```python
print("Hello, World!".replace("Hello", "Howdy"))
```

## Escaping
You can escape characters inside a string with a `\` before. Eg `\n` -> newline or `\t` -> tab
```python
print("Hello\nWorld!")
```


Feel free to check out the [cheatsheet](https://www.pythoncheatsheet.org/cheatsheet/manipulating-strings) for more string manipulation.

## Practice
Rewrite the "remainder is" bit from 04 using `.format`.