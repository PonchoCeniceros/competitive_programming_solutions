# Competitive Programming Solutions

This repository contains my personal solutions to various competitive programming problems. I use this space to track my progress, improve my algorithmic thinking, and maintain a clean collection of implementations.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![LeetCode](https://img.shields.io/badge/-LeetCode-FFA116?style=for-the-badge&logo=LeetCode&logoColor=black)

---

## 📂 Project Structure

All solutions are stored in the exercises/ directory and are named following the convention ID_problem_name.py.

```
.
├── exercises/              # Python solution files
├── create_exercise.sh      # Automation script
└── README.md               # Documentation
```


## 🛠️ Automation

I use a Bash script to automate the creation of new solution files. This ensures a consistent template and saves time.

### How to use it:

1. Give execution permissions (only needed once):
    `chmod +x create_exercise.sh`

2. Generate a new exercise file:
   `./create_exercise.sh 3074_apple_distribution`

The script will automatically create a file inside exercises/ with the following boilerplate:
```python
from log import Log

#
# Exercise ...
#

if __name__ == "__main__":
    solver = Solution()
    Log.green(f"{solver}")
```

## 🎯 Goals
- [ ] Reach 50+ solved problems.
