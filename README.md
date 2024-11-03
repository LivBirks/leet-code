# leetcode
A repository for LeetCode or NeetCode problems.

## Description
This is a repository where I will be storing my solutions and explanations for LeetCode or NeetCode problems, while I am learning algorithms and data structures. The solutions will be in either Python, JavaScript, or C#.

## Directory Structure
```
leet-code/
├── stacks/
│   ├── problem-name-1/
│   │   ├── python
│   │   │   ├── python
│   │   │   │   ├── solution.py
│   │   │   │   ├── test_solution.py
│   │   │   │   └── processor.py
│   │   │   ├── javascript
│   │   │   └── c-sharp
│   │   ├── javascript
│   │   ├── c-sharp
│   │   └── README.md
│   ├── problem-name-2/
│   │   ├── python
│   │   ├── javascript
│   │   ├── c-sharp
│   │   └── README.md
│   ├── problem-name-3/
│   │   ├── python
│   │   ├── javascript
│   │   └── c-sharp
│   │   └── README.md
│   ├── README.md
├── arrays-and-hashing/
│   ├── problem-name-1
│   ├── problem-name-2/
│   └── problem-name-3/
├── .github/
│   └── workflows/
│       └── test.yml
└── README.md
```

## Explanation
- Each problem is organized into a category (e.g., `stacks/`, `arrays-and-hashing`) and a separate problem folder (e.g., `problem-name-1/`, `problem-name-2/`).
- Inside each problem folder, there are subfolders for the solutions in each programming language (where necessary):
  - `python/`
  - `javascript/`
  - `csharp/`
- Each subfolder contains the solution file (`solution.*`) and test cases (`test_solution.*`) for the respective language, in addition to a processor file to run the class solution when testing (`processor.*`).
- Every problem folder includes a `README.md` file explaining the problem, approach, and complexity analysis.
- GitHub Actions workflows for automated testing can be found in the `.github/workflows/` directory.
