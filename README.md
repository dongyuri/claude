# Claude

A simple Python project with utility functions.

## Functions

- `hello_world()` - Prints "Hello, World!"
- `read_file(filepath)` - Read and return file contents
- `write_file(filepath, content)` - Write content to a file
- `append_file(filepath, content)` - Append content to a file

## Usage

```bash
python3 main.py
```

```python
from main import read_file, write_file, append_file

write_file('example.txt', 'Hello!')
content = read_file('example.txt')
append_file('example.txt', '\nMore content')
```

## Tests

```bash
python3 -m unittest test_main -v
```
