# Listpy 🐍

Listpy is a Pythonic implementation of a singly linked list that behaves like a built-in Python list.

## Features
- `append`, `insert`, `pop`, `remove`, `clear`
- `count`, `index`, `reverse`, `sort`
- `get(index)`, `set(index, value)`
- Full linked list with familiar list-like behavior

## Example
```python
from listpy import Listpy

lst = Listpy()
lst.insert_values([3, 1, 4])
lst.append(2)
lst.sort()
lst.print()  # Output: 1 --> 2 --> 3 --> 4
```
