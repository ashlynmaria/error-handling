# Python Exception Handling Examples

A comprehensive collection of Python programs demonstrating exception handling concepts including try-except blocks, specific exception handling, and best practices for control flow in error-prone operations.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Tasks](#tasks)
  - [Task 1: Understanding Python Exceptions](#task-1-understanding-python-exceptions)
  - [Task 2: Types of Exceptions](#task-2-types-of-exceptions)
  - [Task 3: Using try...except...else...finally](#task-3-using-tryexceptelsefinally)
- [Contributing](#contributing)
- [License](#license)

## Overview
This repository contains example scripts to demonstrate how to handle exceptions in Python gracefully. Each task focuses on different aspects of exception handling, from basic try-except blocks to more advanced use of `else` and `finally` clauses.

## Prerequisites
- Python 3.6 or higher installed on your system

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/python-exceptions-demo.git
   cd python-exceptions-demo
   ```
2. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Usage
Run the Python scripts directly from the command line:

```bash
# Task 1
python task1_exceptions.py

# Task 2
python task2_exception_types.py

# Task 3
python task3_else_finally.py
```

Follow the on-screen prompts for interactive inputs.

## Tasks

### Task 1: Understanding Python Exceptions
- Prompts the user to enter a number and divides 100 by the input.
- Handles `ZeroDivisionError` for division by zero.
- Handles `ValueError` for invalid numeric inputs.
- Continues prompting until a valid division occurs.

### Task 2: Types of Exceptions
- Demonstrates handling of common exception types:
  - `IndexError` for invalid list indices.
  - `KeyError` for missing dictionary keys.
  - `TypeError` for unsupported operand types.

### Task 3: Using try...except...else...finally
- Prompts for two numbers and attempts division.
- Uses `else` to execute code when no exception occurs.
- Uses `finally` to execute code regardless of errors.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for improvements.

