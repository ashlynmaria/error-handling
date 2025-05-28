# Python Exception Handling Examples

A comprehensive collection of Python programs demonstrating exception handling concepts including try-except blocks, different exception types, and control flow structures.

## 📋 Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Tasks Overview](#tasks-overview)
  - [Task 1: Understanding Python Exceptions](#task-1-understanding-python-exceptions)
  - [Task 2: Types of Exceptions](#task-2-types-of-exceptions)
  - [Task 3: Complete Exception Handling](#task-3-complete-exception-handling)
- [Learning Objectives](##learning-objectives)
- [Exception Types Covered](##exception-types-covered)
- [Example Outputs](##example-outputs)
- [Best Practices](##best-practices)
- [Contributing](##contributing)

## 🎯 Overview

This repository contains three Python programs that demonstrate fundamental exception handling concepts. Each task builds upon the previous one, providing a progressive learning experience for understanding how to handle errors gracefully in Python applications.

## 📋 Requirements

- Python 3.6 or higher
- No external libraries required (uses only built-in Python modules)

## 🚀 Installation

1. Clone or download this repository
2. Ensure Python is installed on your system
3. Run the programs directly using Python

```bash
python3 error-handling.py
```

## 💻 Usage

Each task can be run independently. The program demonstrates different aspects of exception handling:

1. **Task 1**: Interactive division calculator with error handling
2. **Task 2**: Demonstrates common exception types with examples
3. **Task 3**: Complete exception handling workflow with all control blocks

## 📚 Tasks Overview

### Task 1: Understanding Python Exceptions

**Purpose**: Learn basic exception handling with `try-except` blocks and control flow.

**Features**:
- Interactive user input
- Division by zero handling
- Invalid input validation
- Continuous loop until valid input
- Clean error messages

**Key Concepts**:
- `try-except` blocks
- `ZeroDivisionError`
- `ValueError`
- `continue` statement
- `break` statement

### Task 2: Types of Exceptions

**Purpose**: Explore different built-in exception types and their causes.

**Features**:
- Intentional exception generation
- Multiple exception types demonstration
- Error message customization
- Exception object access

**Key Concepts**:
- `IndexError` - Array bounds violations
- `KeyError` - Dictionary key lookup failures
- `TypeError` - Incompatible data type operations
- Exception object properties

### Task 3: Complete Exception Handling

**Purpose**: Implement comprehensive exception handling with all control blocks.

**Features**:
- Multiple exception handling
- Success path execution
- Cleanup operations
- Complete workflow demonstration

**Key Concepts**:
- `try` block - Code that may raise exceptions
- `except` block - Exception handling
- `else` block - Success path execution
- `finally` block - Cleanup operations

## 🎓 Learning Objectives

By completing these tasks, you will learn:

1. **Exception Handling Fundamentals**
   - How to use try-except blocks
   - When and why exceptions occur
   - How to handle different types of exceptions

2. **Python Exception Types**
   - Understanding built-in exception hierarchy
   - Recognizing common exception scenarios
   - Accessing exception information

3. **Control Flow with Exceptions**
   - Using else and finally blocks
   - Managing program flow with exceptions
   - Implementing robust error handling

4. **Best Practices**
   - Writing user-friendly error messages
   - Proper exception handling patterns
   - Code organization and readability

## 🔍 Exception Types Covered

| Exception Type | Description | Example Scenario |
|----------------|-------------|------------------|
| `ZeroDivisionError` | Division by zero | `100 / 0` |
| `ValueError` | Invalid value for operation | `float("abc")` |
| `IndexError` | List index out of range | `list[999]` |
| `KeyError` | Dictionary key not found | `dict['missing_key']` |
| `TypeError` | Incompatible types | `"string" + 123` |

## 📖 Example Outputs

### Task 1 Output
```
Enter a number: 0
Oops! You cannot divide by zero.
Enter a number: abc
Invalid input! Please enter a valid number.
Enter a number: 4
100 divided by 4.0 is 25.0.
```

### Task 2 Output
```
IndexError occurred! List index out of range. list index out of range
KeyError occurred! Key not found in the dictionary. 'c'
TypeError occurred! Unsupported operand types. can only concatenate str (not "int") to str
```

### Task 3 Output
```
Enter the first number: 10
Enter the second number: 2
The result is 5.0.
This block always executes.
```

## ✅ Best Practices Demonstrated

1. **Specific Exception Handling**: Catch specific exceptions rather than using broad `except` clauses
2. **User-Friendly Messages**: Provide clear, actionable error messages
3. **Proper Flow Control**: Use `continue` and `break` appropriately
4. **Resource Cleanup**: Utilize `finally` blocks for cleanup operations
5. **Input Validation**: Always validate user input before processing
6. **Error Documentation**: Include comments explaining why exceptions occur

## 🏗️ Code Structure

```
exception_handling_demo.py
├── Task 1: Basic Exception Handling
│   ├── Input validation loop
│   ├── ZeroDivisionError handling
│   └── ValueError handling
├── Task 2: Exception Types Demo
│   ├── IndexError example
│   ├── KeyError example
│   └── TypeError example
└── Task 3: Complete Exception Workflow
    ├── Try block
    ├── Multiple except blocks
    ├── Else block
    └── Finally block
```

## 🤝 Contributing

Feel free to contribute improvements or additional examples:

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request


## 🔗 Additional Resources

- [Python Official Documentation - Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python Exception Hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
- [Best Practices for Exception Handling](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)

---

**Happy Coding!** 🐍✨
