# Python: Everything is an Object — What You Need to Know

---

## Introduction

In Python, **everything is an object** — integers, strings, lists, functions, even classes themselves. Understanding how Python handles objects in memory is fundamental to writing correct and efficient code. This post covers the key concepts: identity, type, mutability, and how function arguments really work.

---

## `id` and `type`

Every object in Python has two core properties:

- **`type(obj)`** — returns the type/class of the object
- **`id(obj)`** — returns the unique identifier of the object (its memory address in CPython)

```python
a = 42
print(type(a))   # <class 'int'>
print(id(a))     # 140234567891234 (example)

b = [1, 2, 3]
print(type(b))   # <class 'list'>
print(id(b))     # 140234567891456 (example)
```

Two operators let you compare objects:
- `==` compares **values**
- `is` compares **identity** (same object in memory)

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True  (same value)
print(a is b)   # False (different objects)
```

---

## Immutable Objects

Immutable objects **cannot be modified** after creation. If you "change" them, Python creates a new object.

Immutable types: `int`, `float`, `str`, `tuple`, `bool`, `frozenset`

```python
a = "Hello"
print(id(a))     # 140234567891234

a = a + " World"
print(id(a))     # 140234567899999 — new object!
```

Python **caches** small integers (-5 to 256) and string literals to save memory:

```python
a = 89
b = 89
print(a is b)    # True — same cached object

a = 1000
b = 1000
print(a is b)    # False — outside cache range
```

---

## Mutable Objects

Mutable objects **can be modified in place** without creating a new object.

Mutable types: `list`, `dict`, `set`, `bytearray`

```python
l = [1, 2, 3]
print(id(l))     # 140234567891234

l.append(4)
print(l)         # [1, 2, 3, 4]
print(id(l))     # 140234567891234 — same object!
```

Be careful with aliasing:

```python
l1 = [1, 2, 3]
l2 = l1          # l2 points to the SAME object
l1.append(4)
print(l2)        # [1, 2, 3, 4] — l2 is also modified!
```

---

## Why Does It Matter?

Python treats mutable and immutable objects very differently:

| | Immutable | Mutable |
|---|---|---|
| Can be modified | No | Yes |
| `+=` creates new object | Yes | No |
| Safe to alias | Yes | Risky |

```python
# Immutable — += creates a new object
a = (1, 2)
print(id(a))
a += (3,)
print(id(a))     # Different id!

# Mutable — += modifies in place
l = [1, 2]
print(id(l))
l += [3]
print(id(l))     # Same id!
```

---

## How Arguments Are Passed to Functions

Python uses **"pass by object reference"** (also called pass by assignment). The function receives a reference to the same object, not a copy.

**With immutable objects** — the original is never modified:

```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)    # 1 — unchanged
```

**With mutable objects** — the original CAN be modified if you mutate it in place:

```python
def add_item(lst):
    lst.append(4)

l = [1, 2, 3]
add_item(l)
print(l)    # [1, 2, 3, 4] — modified!
```

But reassigning the parameter does NOT affect the original:

```python
def replace(lst):
    lst = [4, 5, 6]   # only changes local reference

l = [1, 2, 3]
replace(l)
print(l)    # [1, 2, 3] — unchanged
```

---

## Conclusion

Understanding mutability and object identity in Python helps you avoid subtle bugs, especially when passing objects to functions or aliasing variables. Always ask yourself: *am I creating a new object, or modifying an existing one?*
