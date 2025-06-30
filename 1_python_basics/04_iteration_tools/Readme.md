# 🔁 Python Iteration Tools

This folder contains Python examples that demonstrate **smart and efficient ways to loop** through data using built-in tools like `range()`, `enumerate()`, `zip()`, and file reading techniques.

---

## 📚 Index of Files

| #   | File Name                  | Concept/Tool Covered                        | Description                                                  |
|-----|----------------------------|---------------------------------------------|--------------------------------------------------------------|
| 1️⃣ | `01_range_basics.py`       | `range()`                                   | Loop over numbers with start, stop, and step                 |
| 2️⃣ | `02_enumerate_list.py`     | `enumerate()`                               | Loop with index + value from list                            |
| 3️⃣ | `03_zip_two_lists.py`      | `zip()`                                     | Loop over two lists together                                 |
| 4️⃣ | `04_break_continue.py`     | `break`, `continue`                         | Control loop flow by exiting or skipping                    |
| 5️⃣ | `05_loop_with_else.py`     | `for...else`, `while...else`                | Execute else only if loop finishes without `break`          |
| 6️⃣ | `06_pass_statement.py`     | `pass`                                      | Empty block placeholder to avoid syntax error               |
| 7️⃣ | `07_file_readline.py`      | `open()`, `readline()`, file loop           | Read files line-by-line using loops and context manager     |

---

## 🧠 Why Learn These?

| Benefit             | What It Helps With                                     |
|---------------------|---------------------------------------------------------|
| ✅ Cleaner Code      | Avoids manual indexing and flags                       |
| ✅ Real-World Usage  | Used in data processing, automation, file handling     |
| ✅ Interview Ready   | Commonly asked in basic Python coding interviews       |
| ✅ Productivity Boost| Helps write fast and readable logic                    |

---

## 🔁 Sample Snippets

### 🔹 `enumerate()` Example:
```python
for i, fruit in enumerate(["apple", "banana"]):
    print(i, fruit)
