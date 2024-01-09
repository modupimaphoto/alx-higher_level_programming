# 0x0B. Python - Input/Output

### File Operations in Python:

#### How to open a file:
```python
# Open a file in read mode
file = open('filename.txt', 'r')

# Open a file in write mode (creates a new file or overwrites existing content)
file = open('filename.txt', 'w')

# Open a file in append mode (creates a new file or appends to existing content)
file = open('filename.txt', 'a')
```

#### How to write text in a file:
```python
# Writing to a file
with open('filename.txt', 'w') as file:
    file.write('Hello, this is a line of text.\n')
    file.write('This is another line of text.\n')
```

#### How to read the full content of a file:
```python
# Reading the full content of a file
with open('filename.txt', 'r') as file:
    content = file.read()
    print(content)
```

#### How to read a file line by line:
```python
# Reading a file line by line
with open('filename.txt', 'r') as file:
    for line in file:
        print(line)
```

#### How to move the cursor in a file:
```python
# Moving the cursor in a file
with open('filename.txt', 'r') as file:
    file.seek(5)  # Move to the 6th character (0-based index)
    content = file.read()
    print(content)
```

#### How to make sure a file is closed after using it:
Python provides a `with` statement that automatically takes care of closing the file:
```python
with open('filename.txt', 'r') as file:
    # File operations go here
# File is automatically closed when the block is exited
```

### JSON (JavaScript Object Notation):
- **JSON (JavaScript Object Notation)** is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.
- It is often used to transmit data between a server and web application, as well as to store configuration data.

#### Serialization:
- **Serialization** is the process of converting a data structure or object into a format that can be easily stored or transmitted.

#### Deserialization:
- **Deserialization** is the process of converting a serialized format (like JSON) back into a data structure or object.

### JSON

- `json.dumps()`: Used to convert Python data structure to JSON string.
- `json.loads()`: Used to convert JSON string to Python data structure
