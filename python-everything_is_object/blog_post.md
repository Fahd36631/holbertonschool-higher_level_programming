Introduction
In Python, everything is an object. Numbers, strings, lists, and even functions are objects stored in memory. Understanding how objects behave helps developers avoid unexpected behavior and write more predictable code.

This project helped me understand identity, mutability, aliasing, and how Python handles variables and function arguments.

id and type
Every object in Python has:

A type
An identity (memory address)
We can check them using type() and id().

Example:

a = 10
print(type(a))
print(id(a))
Example output:

<class 'int'>
140704225839024
Mutable Objects
Mutable objects can be changed after creation.

Common mutable types:

list

dictionary

set

Example:

numbers = [1, 2, 3]
numbers[0] = 9
print(numbers)
Output:

[9, 2, 3]
Aliasing example:

a = [1, 2, 3]
b = a
a[0] = 100
print(b)
Output:

[100, 2, 3]
Immutable Objects
Immutable objects cannot be changed after creation.

Common immutable types:

int

float

string

tuple

Example:

a = 5
b = a
a = 7
print(b)
Output:

5
Why It Matters
Understanding mutability is important because it affects memory usage, debugging, and unexpected variable changes.

Example:

list1 = [1, 2, 3]
list2 = list1
list1.append(4)
print(list2)
Output:

[1, 2, 3, 4]
To avoid this, we can copy:

list2 = list1.copy()
How Arguments Are Passed to Functions
Python passes arguments as references to objects.

Mutable example:

def modify_list(lst):
    lst.append(99)

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)
Output:

[1, 2, 3, 99]
Immutable example:

def modify_number(x):
    x = x + 1

num = 5
modify_number(num)
print(num)
Output:

5
What I Learned
From this project, I learned:

Python variables store references to objects

Mutable objects can be modified in place

Immutable objects create new objects when changed

Aliasing can cause unexpected bugs

Using id() helps understand memory behavior