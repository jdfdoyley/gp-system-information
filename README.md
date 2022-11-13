# System Information

In this program I will demonstrate how to use Python to get system information.

## Table of Content

- [What I learned](#what-i-learned)

### What I learned

In order for me to get access to the system information, I had to use the `platform` Python module.

- `platform.platform()`: Returns a single string identifying the underlying platform with as much useful information as possible.

- `platform.machine()`: Returns the machine type, e.g. 'AMD64'. An empty string is returned if the value cannot be determined.

- `platform.node()`: Returns the computer’s network name (may not be fully qualified!). An empty string is returned if the value cannot be determined.

- `platform.processor()`: Returns the (real) processor name, e.g. 'amdk6'.

- `platform.win32_edition()`: Returns a string representing the current Windows edition, or None if the value cannot be determin

Read more about the [platform module](https://docs.python.org/3/library/platform.html)
