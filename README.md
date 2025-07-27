# OOPythonic

OOPythonic is a repository dedicated to mastering Object-Oriented Programming (OOP) in Python the Pythonic way. From classes and objects to inheritance, polymorphism, and encapsulation, this repo offers clean examples, real-world use cases, and best practices to write efficient, elegant, and reusable Python code.

---

---

# 🐍 Everything in Python is an Object — Even Functions!

If you've been learning Python, you've probably heard the phrase: **"Everything in Python is an object."** But what does that actually mean?

In this section, we'll explore this powerful idea with simple examples. By the end, you’ll understand why Python treats **numbers, strings, lists, functions, and even classes** as objects—and how that makes Python so flexible and powerful.

## 🎯 What Does "Everything Is an Object" Mean?

In Python:

- **Every value has a type**.
- **Every type is a class**.
- **Every value is an instance of some class**—in other words, an object.

This includes basic data types like integers and strings, but also more complex things like functions and classes themselves.

## 🔢 1. Numbers Are Objects

Let’s take a basic number:

```python
x = 10
print(type(x))         # <class 'int'>
print(x.bit_length())  # Output: 4
```

Even a simple number like `10` is an **object** of class `int`. It has methods like `.bit_length()` which returns how many bits are needed to represent the number in binary.

## 🔤 2. Strings Are Objects

```python
s = "hello"
print(type(s))       # <class 'str'>
print(s.upper())     # Output: "HELLO"
```

Here, `s` is an object of type `str`. It has methods like `.upper()`, `.lower()`, and `.replace()`—which are all behaviors defined by the `str` class.

## 📦 3. Lists Are Objects

```python
lst = [1, 2, 3]
print(type(lst))      # <class 'list'>
lst.append(4)
print(lst)            # Output: [1, 2, 3, 4]
```

`lst` is an object of class `list`. The method `.append()` modifies the object in-place.

## 🧠 4. Functions Are Objects

Here’s where things get interesting.

In Python, **functions are first-class objects**. That means:

- You can assign them to variables.
- You can pass them as arguments.
- You can return them from other functions.

```python
def greet(name):
    return f"Hello, {name}"

print(type(greet))      # <class 'function'>

say_hello = greet       # assign function to variable
print(say_hello("Alice"))  # Output: Hello, Alice
```

Here, `greet` is an object of type `function`. Just like strings and lists, it can be manipulated and passed around.

## 🏗️ 5. Classes Are Objects Too

Yes, even classes are objects. When you define a class in Python, that class is itself an object—specifically, an instance of `type`.

```python
class Person:
    def __init__(self, name):
        self.name = name

print(type(Person))  # <class 'type'>
```

This might feel strange at first, but it’s what makes **metaprogramming** and powerful features like decorators and class factories possible.

## 📚 Quick Summary

Here’s a table to recap:

| Python Construct | Type       | Is it an Object? |
| ---------------- | ---------- | ---------------- |
| `10`             | `int`      | ✅ Yes           |
| `"hello"`        | `str`      | ✅ Yes           |
| `[1, 2, 3]`      | `list`     | ✅ Yes           |
| `greet` function | `function` | ✅ Yes           |
| `Person` class   | `type`     | ✅ Yes           |

## 💡 Real-World Analogy: The LEGO World

Imagine Python as a giant LEGO world:

- Each LEGO piece (data or function) is an object.
- Some pieces have built-in behaviors (methods).
- You can pass them around, plug them together, and build more complex creations.
- Even the **instructions to make LEGO models (classes)** are LEGO pieces themselves!

This consistent design makes Python **intuitive**, **flexible**, and a great language for both beginners and advanced developers.

---
