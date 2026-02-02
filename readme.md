# Competitive Programming Solutions

This repository contains my personal solutions to various competitive programming problems. I use this space to track my progress, improve my algorithmic thinking, and maintain a clean collection of implementations.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)![LeetCode](https://img.shields.io/badge/-LeetCode-FFA116?style=for-the-badge&logo=LeetCode&logoColor=black)

---

## 📂 Project Structure

All solutions are stored in the `codes/` directory with a simplified naming convention using only the problem ID.
```
.
├── codes/                # Current Python solution files (pytest format)
│   ├── 1.py              # Two Sum
│   ├── 20.py             # Valid Parentheses
│   ├── 26.py             # Remove Duplicates from Sorted Array
│   ├── 28.py             # Find the Index of the First Occurrence in a String
│   ├── 70.py             # Climbing Stairs
│   └── ...
├── utils/                # Utilities
├── create.sh             # Automation script for creating new exercises
└── README.md             # Documentation
```

---

## 🧪 Testing Framework

All solutions use **pytest** with parametrized tests for comprehensive testing:

```python
# Unit tests

@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        (input1, expected1),
        (input2, expected2),
        (input3, expected3),
    ],
)
def test_solution_function(input_params, expected_output):
    sol = Solution()
    assert sol.method(input_params) == expected_output
```

### Running Tests

```bash
# Run all tests
pytest codes/

# Run specific test
pytest codes/1.py

# Run with verbose output
pytest codes/ -v
```

---

## 🛠️ Automation

I use a Bash script to automate the creation of new solution files with the updated pytest template.

### How to use it:

1. Give execution permissions (only needed once):
    ```bash
    chmod +x create.sh
    ```

2. Generate a new exercise file (LeetCode format):
    ```bash
    ./create.sh "9. Palindrome Number"
    ./create.sh "125 Valid Palindrome"
    ```

The script will automatically create a file inside `codes/` with the following boilerplate:
```python
import pytest
from typing import List, Optional, Dict
from utils.log import Log


#
# Exercise Problem Name
#
class Solution:
    # [Implement your solution here]
    ...


# Unit tests


@pytest.mark.parametrize(
    # [Add your parameters here]
    "",
    [
        # [Add your test cases here]
    ],
)
def test_# [test_function_name](# [parameters]):
    sol = Solution()
    assert sol.# [method_name](# [arguments]) == # [expected]
```

### Features

- ✅ **Modern pytest framework** with parametrized tests
- ✅ **Type hints** for better code documentation
- ✅ **Simplified naming** (e.g., `9.py` instead of `9_palindrome_number.py`)
- ✅ **Full problem names** in exercise comments
- ✅ **Standardized logging** with `utils.log`

---
