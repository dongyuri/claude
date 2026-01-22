def hello_world():
    print("Hello, World!")


def read_file(filepath):
    """Read and return the contents of a file."""
    with open(filepath, 'r') as f:
        return f.read()


def write_file(filepath, content):
    """Write content to a file."""
    with open(filepath, 'w') as f:
        f.write(content)


def append_file(filepath, content):
    """Append content to a file."""
    with open(filepath, 'a') as f:
        f.write(content)


if __name__ == "__main__":
    hello_world()
