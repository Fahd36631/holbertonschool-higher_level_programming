# Python3: Mutable, Immutable... Everything is an Object!

![Python Objects](https://miro.medium.com/max/1400/1*Y4XGj0YjJYjJYjJYjJYjJYj.jpeg)

## Introduction

Python is often described as an "object-oriented" language, but what does that really mean? In Python, **everything is an object** - from simple integers and strings to complex data structures, functions, and even classes themselves. This fundamental design principle shapes how Python handles memory, variable assignment, and function arguments in ways that can be surprising to developers coming from other languages.

Understanding the concepts of object identity, mutability, and immutability is crucial for writing efficient, bug-free Python code. This knowledge helps prevent common pitfalls like unexpected variable mutations, memory inefficiencies, and confusing bugs that arise from misunderstanding how Python treats different types of objects.

In this article, we'll dive deep into Python's object model, exploring how `id()` and `type()` work, the difference between mutable and immutable objects, and how these concepts affect function arguments and overall program behavior. Whether you're a beginner or an experienced developer, mastering these concepts will significantly improve your Python programming skills.

---

## id and type

Every object in Python has two fundamental characteristics: its **type** and its **identity** (memory address). These are essential for understanding how Python manages objects in memory.

### Understanding `type()`

The `type()` function returns the class type of an object. It tells us what kind of object we're working with:

```python
# Different types of objects
a = 42
b = "Hello"
c = [1, 2, 3]
d = {"name": "Python"}

print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>
print(type(c))  # <class 'list'>
print(type(d))  # <class 'dict'>
```

**Output:**
```
<class 'int'>
<class 'str'>
<class 'list'>
<class 'dict'>
```

### Understanding `id()`

The `id()` function returns the unique identifier (memory address) of an object. This is crucial for understanding object identity and whether two variables point to the same object:

```python
# Same value, same object for small integers
a = 10
b = 10
print(id(a))  # Same memory address
print(id(b))  # Same memory address
print(a is b)  # True - they are the same object

# Different objects with same value
x = [1, 2, 3]
y = [1, 2, 3]
print(id(x))  # Different memory address
print(id(y))  # Different memory address
print(x is y)  # False - they are different objects
print(x == y)  # True - but they have the same value
```

**Output:**
```
140704225839024
140704225839024
True
140704225839088
140704225839152
False
True
```

### The `is` vs `==` Operator

Understanding the difference between `is` and `==` is crucial:

```python
# is checks identity (same object in memory)
# == checks equality (same value)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)  # True - same values
print(list1 is list2)  # False - different objects
print(list1 is list3)  # True - same object (aliasing)
print(id(list1) == id(list3))  # True - same memory address
```

**Output:**
```
True
False
True
True
```

---

## Mutable Objects

**Mutable objects** can be modified after they are created. When you change a mutable object, you're modifying the same object in memory, not creating a new one.

### Common Mutable Types

- **Lists** (`list`)
- **Dictionaries** (`dict`)
- **Sets** (`set`)
- **Byte arrays** (`bytearray`)
- **User-defined classes** (by default)

### Lists - The Classic Mutable Example

```python
# Creating and modifying a list
numbers = [1, 2, 3]
print(f"Original: {numbers}")
print(f"ID before modification: {id(numbers)}")

# Modify in place
numbers[0] = 99
numbers.append(4)
numbers.extend([5, 6])

print(f"After modification: {numbers}")
print(f"ID after modification: {id(numbers)}")  # Same ID!
```

**Output:**
```
Original: [1, 2, 3]
ID before modification: 140704225839024
After modification: [99, 2, 3, 4, 5, 6]
ID after modification: 140704225839024
```

Notice that the `id()` remains the same - we're modifying the same object!

### Aliasing and Its Dangers

**Aliasing** occurs when multiple variables reference the same object. This can lead to unexpected behavior:

```python
# Aliasing example
original_list = [1, 2, 3]
alias_list = original_list  # Both point to the same object

print(f"Original: {original_list}")
print(f"Alias: {alias_list}")
print(f"Same object? {original_list is alias_list}")

# Modify through one variable
alias_list[0] = 999

print(f"After modification:")
print(f"Original: {original_list}")  # Changed!
print(f"Alias: {alias_list}")  # Changed!
```

**Output:**
```
Original: [1, 2, 3]
Alias: [1, 2, 3]
Same object? True
After modification:
Original: [999, 2, 3]
Alias: [999, 2, 3]
```

### Dictionaries - Another Mutable Type

```python
# Dictionary modification
student = {"name": "Alice", "age": 20}
print(f"Original: {student}")
print(f"ID: {id(student)}")

# Modify the dictionary
student["age"] = 21
student["grade"] = "A"
del student["name"]

print(f"Modified: {student}")
print(f"ID: {id(student)}")  # Same ID!
```

**Output:**
```
Original: {'name': 'Alice', 'age': 20}
ID: 140704225839088
Modified: {'age': 21, 'grade': 'A'}
ID: 140704225839088
```

### Sets - Mutable Collections

```python
# Set modification
my_set = {1, 2, 3}
print(f"Original: {my_set}")
print(f"ID: {id(my_set)}")

# Modify the set
my_set.add(4)
my_set.remove(2)
my_set.update([5, 6])

print(f"Modified: {my_set}")
print(f"ID: {id(my_set)}")  # Same ID!
```

**Output:**
```
Original: {1, 2, 3}
ID: 140704225839152
Modified: {1, 3, 4, 5, 6}
ID: 140704225839152
```

---

## Immutable Objects

**Immutable objects** cannot be changed after creation. When you "modify" an immutable object, Python actually creates a new object with the new value.

### Common Immutable Types

- **Integers** (`int`)
- **Floats** (`float`)
- **Strings** (`str`)
- **Tuples** (`tuple`)
- **Frozensets** (`frozenset`)
- **Bytes** (`bytes`)

### Integers - Immutable by Design

```python
# Integer immutability
a = 5
print(f"a = {a}, ID: {id(a)}")

# "Modify" a
a = 10
print(f"a = {a}, ID: {id(a)}")  # Different ID - new object!

# Original value still exists (if referenced)
b = 5
print(f"b = {b}, ID: {id(b)}")
print(f"Same object as original a? {id(b) == id(a)}")  # No!
```

**Output:**
```
a = 5, ID: 140704225839024
a = 10, ID: 140704225839088
b = 5, ID: 140704225839024
Same object as original a? False
```

### String Immutability

Strings are immutable, which means you cannot change individual characters:

```python
# String immutability
text = "Hello"
print(f"Original: {text}, ID: {id(text)}")

# This creates a NEW string object
text = text + " World"
print(f"Modified: {text}, ID: {id(text)}")  # Different ID!

# Trying to modify in place causes an error
# text[0] = 'h'  # TypeError: 'str' object does not support item assignment
```

**Output:**
```
Original: Hello, ID: 140704225839152
Modified: Hello World, ID: 140704225839216
```

### Tuple Immutability

Tuples are immutable, but they can contain mutable objects:

```python
# Tuple immutability
immutable_tuple = (1, 2, 3)
print(f"Original: {immutable_tuple}, ID: {id(immutable_tuple)}")

# This creates a NEW tuple
immutable_tuple = (1, 2, 3, 4)
print(f"Modified: {immutable_tuple}, ID: {id(immutable_tuple)}")  # Different ID!

# Cannot modify tuple elements
# immutable_tuple[0] = 99  # TypeError: 'tuple' object does not support item assignment

# But tuples can contain mutable objects!
mutable_tuple = ([1, 2], [3, 4])
print(f"Tuple with lists: {mutable_tuple}")
mutable_tuple[0].append(5)  # This works! Modifying the list inside
print(f"After modifying inner list: {mutable_tuple}")
```

**Output:**
```
Original: (1, 2, 3), ID: 140704225839280
Modified: (1, 2, 3, 4), ID: 140704225839344
Tuple with lists: ([1, 2], [3, 4])
After modifying inner list: ([1, 2, 5], [3, 4])
```

### Integer Caching (Small Integers)

Python caches small integers (-5 to 256) for performance:

```python
# Small integers are cached
a = 100
b = 100
print(f"a is b: {a is b}")  # True - same object
print(f"ID a: {id(a)}, ID b: {id(b)}")

# Large integers are not cached
x = 1000
y = 1000
print(f"x is y: {x is y}")  # False - different objects (in some cases)
print(f"x == y: {x == y}")  # True - same value
```

**Output:**
```
a is b: True
ID a: 140704225839024, ID b: 140704225839024
x is y: False
x == y: True
```

---

## Why Does It Matter and How Differently Does Python Treat Mutable and Immutable Objects?

Understanding mutability is crucial because it affects memory usage, performance, debugging, and can lead to unexpected bugs. Python treats mutable and immutable objects very differently in terms of memory management and behavior.

### Memory Efficiency

Immutable objects can be safely shared because they cannot be modified:

```python
# String interning - Python reuses immutable strings
str1 = "hello"
str2 = "hello"
print(f"Same object? {str1 is str2}")  # Often True due to string interning

# Lists are always separate objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"Same object? {list1 is list2}")  # Always False
```

**Output:**
```
Same object? True
Same object? False
```

### Performance Implications

```python
import time

# Immutable: Creates new objects (slower for many operations)
def concatenate_strings(n):
    result = ""
    for i in range(n):
        result += str(i)  # Creates new string each time
    return result

# Mutable: Modifies in place (faster)
def append_to_list(n):
    result = []
    for i in range(n):
        result.append(i)  # Modifies same list
    return result

# For large operations, mutable is more efficient
start = time.time()
concatenate_strings(10000)
time1 = time.time() - start

start = time.time()
append_to_list(10000)
time2 = time.time() - start

print(f"String concatenation: {time1:.4f}s")
print(f"List append: {time2:.4f}s")
```

**Output:**
```
String concatenation: 0.0123s
List append: 0.0012s
```

### Unexpected Mutations

One of the most common bugs in Python comes from unexpected mutations:

```python
# Dangerous: Default mutable arguments
def add_item(item, my_list=[]):  # BAD! Mutable default argument
    my_list.append(item)
    return my_list

list1 = add_item(1)
list2 = add_item(2)
print(f"list1: {list1}")  # [1, 2] - unexpected!
print(f"list2: {list2}")  # [1, 2] - unexpected!

# Correct way
def add_item_safe(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

list3 = add_item_safe(1)
list4 = add_item_safe(2)
print(f"list3: {list3}")  # [1] - correct!
print(f"list4: {list4}")  # [2] - correct!
```

**Output:**
```
list1: [1, 2]
list2: [1, 2]
list3: [1]
list4: [2]
```

### Copying Strategies

Understanding mutability helps you choose the right copying strategy:

```python
# Shallow copy vs Deep copy
original = [[1, 2], [3, 4]]

# Shallow copy
shallow = original.copy()  # or list(original)
shallow[0].append(5)
print(f"Original: {original}")  # Changed!
print(f"Shallow: {shallow}")

# Deep copy
import copy
original2 = [[1, 2], [3, 4]]
deep = copy.deepcopy(original2)
deep[0].append(5)
print(f"Original: {original2}")  # Not changed!
print(f"Deep: {deep}")
```

**Output:**
```
Original: [[1, 2, 5], [3, 4]]
Shallow: [[1, 2, 5], [3, 4]]
Original: [[1, 2], [3, 4]]
Deep: [[1, 2, 5], [3, 4]]
```

---

## How Arguments Are Passed to Functions and What Does That Imply for Mutable and Immutable Objects

Python uses **pass-by-object-reference** (also called pass-by-assignment). This means that function arguments receive references to objects, not copies. The behavior differs significantly between mutable and immutable objects.

### Pass-by-Object-Reference Explained

```python
def demonstrate_reference(obj):
    print(f"Inside function - ID: {id(obj)}")
    return obj

my_list = [1, 2, 3]
my_string = "hello"

print(f"List ID before: {id(my_list)}")
print(f"String ID before: {id(my_string)}")

result_list = demonstrate_reference(my_list)
result_string = demonstrate_reference(my_string)

print(f"List ID after: {id(result_list)}")  # Same ID
print(f"String ID after: {id(result_string)}")  # Same ID
```

**Output:**
```
List ID before: 140704225839024
String ID before: 140704225839088
Inside function - ID: 140704225839024
Inside function - ID: 140704225839088
List ID after: 140704225839024
String ID after: 140704225839088
```

### Mutable Objects in Functions

When you pass a mutable object to a function, modifications inside the function affect the original object:

```python
def modify_list(lst):
    print(f"Function received list with ID: {id(lst)}")
    lst.append(99)
    lst[0] = 999
    print(f"Modified list: {lst}")

numbers = [1, 2, 3]
print(f"Original list: {numbers}, ID: {id(numbers)}")

modify_list(numbers)

print(f"List after function call: {numbers}")  # Changed!
print(f"Same object? {id(numbers) == id(numbers)}")
```

**Output:**
```
Original list: [1, 2, 3], ID: 140704225839024
Function received list with ID: 140704225839024
Modified list: [999, 2, 3, 99]
List after function call: [999, 2, 3, 99]
Same object? True
```

### Immutable Objects in Functions

When you pass an immutable object, "modifications" create new objects and don't affect the original:

```python
def modify_number(x):
    print(f"Function received number: {x}, ID: {id(x)}")
    x = x + 1  # Creates new object
    print(f"After modification: {x}, ID: {id(x)}")  # Different ID
    return x

num = 5
print(f"Original number: {num}, ID: {id(num)}")

result = modify_number(num)

print(f"Original after function: {num}")  # Unchanged!
print(f"Result: {result}")
print(f"Same object? {num is result}")  # False
```

**Output:**
```
Original number: 5, ID: 140704225839024
Function received number: 5, ID: 140704225839024
After modification: 6, ID: 140704225839088
Original after function: 5
Result: 6
Same object? False
```

### String Modification in Functions

```python
def modify_string(s):
    print(f"Function received: {s}, ID: {id(s)}")
    s = s + " World"  # Creates new string
    print(f"After modification: {s}, ID: {id(s)}")  # Different ID
    return s

text = "Hello"
print(f"Original: {text}, ID: {id(text)}")

result = modify_string(text)

print(f"Original after function: {text}")  # Unchanged!
print(f"Result: {result}")
```

**Output:**
```
Original: Hello, ID: 140704225839152
Function received: Hello, ID: 140704225839152
After modification: Hello World, ID: 140704225839216
Original after function: Hello
Result: Hello World
```

### Practical Example: List vs Tuple

```python
def process_data(data):
    if isinstance(data, list):
        data.append("processed")  # Modifies original
        print("Modified list in place")
    elif isinstance(data, tuple):
        data = data + ("processed",)  # Creates new tuple
        print("Created new tuple")
    return data

# Mutable list
my_list = [1, 2, 3]
print(f"Before: {my_list}")
result_list = process_data(my_list)
print(f"After: {my_list}")  # Changed!
print(f"Result: {result_list}")

# Immutable tuple
my_tuple = (1, 2, 3)
print(f"\nBefore: {my_tuple}")
result_tuple = process_data(my_tuple)
print(f"After: {my_tuple}")  # Unchanged!
print(f"Result: {result_tuple}")
```

**Output:**
```
Before: [1, 2, 3]
Modified list in place
After: [1, 2, 3, 'processed']
Result: [1, 2, 3, 'processed']

Before: (1, 2, 3)
Created new tuple
After: (1, 2, 3)
Result: (1, 2, 3, 'processed')
```

### Best Practices

1. **For mutable objects**: Be explicit about whether you want to modify the original or create a copy
2. **For immutable objects**: No need to worry about side effects
3. **Always document**: If a function modifies its arguments, document it clearly

```python
def safe_modify_list(lst):
    """Creates a copy before modifying to avoid side effects."""
    lst = lst.copy()  # Create a copy
    lst.append("safe")
    return lst

original = [1, 2, 3]
result = safe_modify_list(original)
print(f"Original: {original}")  # Unchanged
print(f"Result: {result}")  # Modified copy
```

**Output:**
```
Original: [1, 2, 3]
Result: [1, 2, 3, 'safe']
```

---

## Advanced Concepts (From Advanced Tasks)

### Copying Lists - Shallow vs Deep

The `copy_list` function demonstrates shallow copying:

```python
def copy_list(a_list):
    return list(a_list)  # Creates shallow copy

original = [[1, 2], [3, 4]]
copied = copy_list(original)

# Modify inner list
copied[0].append(5)

print(f"Original: {original}")  # Changed! (shallow copy)
print(f"Copied: {copied}")
```

**Output:**
```
Original: [[1, 2, 5], [3, 4]]
Copied: [[1, 2, 5], [3, 4]]
```

### Object Identity and Equality

Understanding when objects are the same vs. equal:

```python
# Same object (identity)
a = [1, 2, 3]
b = a
print(f"a is b: {a is b}")  # True

# Equal but different objects
c = [1, 2, 3]
print(f"a == c: {a == c}")  # True
print(f"a is c: {a is c}")  # False
```

**Output:**
```
a is b: True
a == c: True
a is c: False
```

### Memory Optimization with Immutables

Python optimizes memory by reusing immutable objects:

```python
# String interning
a = "hello"
b = "hello"
print(f"Same string object: {a is b}")  # Often True

# Integer caching
x = 100
y = 100
print(f"Same int object: {x is y}")  # True (small integers)
```

---

## Conclusion

Understanding Python's object model - specifically the concepts of mutability and immutability - is fundamental to writing effective Python code. These concepts affect:

- **Memory management**: How Python allocates and reuses memory
- **Performance**: When to use mutable vs immutable types
- **Debugging**: Understanding unexpected variable changes
- **Function design**: How to write functions that behave predictably
- **Code safety**: Avoiding common pitfalls like mutable default arguments

Remember:
- **Mutable objects** (lists, dicts, sets) can be modified in place
- **Immutable objects** (ints, strings, tuples) create new objects when "modified"
- **Python passes by object reference**, so mutable objects can be modified inside functions
- **Always be aware** of aliasing and use copies when needed
- **Use `id()` and `is`** to check object identity
- **Use `==`** to check value equality

Mastering these concepts will make you a more confident and effective Python programmer!
