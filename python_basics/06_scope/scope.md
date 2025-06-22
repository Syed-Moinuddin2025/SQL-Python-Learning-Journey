# 06_scope

This folder contains practical examples demonstrating **variable scope** in Python.  
Scope determines where a variable can be accessed or modified within a program.

---

## 🧠 Scope Levels Covered

| No. | Topic                   | Description                                                                 | File Name                    |
|-----|-------------------------|-----------------------------------------------------------------------------|------------------------------|
| 1   | Local Scope             | Variable defined inside a function — only accessible within that function. | 01_local_scope.py            |
| 2   | Global Scope            | Variable defined outside all functions — accessible anywhere.              | 02_global_scope.py           |
| 3   | Global Keyword          | Modifying global variables inside a function using `global`.               | 03_global_keyword.py         |
| 4   | Enclosed Scope          | Accessing variables from enclosing (outer) function in nested functions.   | 04_enclosed_scope.py         |
| 5   | Function vs Block Scope | Explains how Python handles `if`, `for` blocks inside functions.           | 05_function_vs_block_scope.py|
| 6   | LEGB Rule               | Demonstrates Python's name resolution order: Local → Enclosed → Global → Built-in. | 06_LEGB_rule_demo.py         |

---

## 🔍 Summary of Scope Types

- **Local**: Inside the current function
- **Enclosed**: Inside any outer (enclosing) function
- **Global**: Top-level of the script
- **Built-in**: Predefined in Python like `print()`, `len()`

---

📂 Use these files to understand where variables live and how they behave in different scopes.
