# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Personal collection of Python implementations of common data structures and algorithms. All code lives in `src/` as standalone `.py` files (no package structure, no build system, no external dependencies).

## Running and Testing

Each file has inline tests via `assert` statements in `if __name__ == '__main__':` blocks. Run any file directly:

```bash
python src/05b_BinarySearchTree.py
```

Successful execution prints "All tests passed!" — there is no test framework.

To run all tests:
```bash
for f in src/*.py; do python "$f"; done
```

## Requirements

Python 3.9+ (uses modern type hints like `list[int]` instead of `typing.List[int]`).

## Code Conventions

- Files are numbered by topic: `01` hash tables, `02` linked lists, `03` stack, `04` queue, `05` trees/heaps/tries, `06` graphs, `07` search, `08` sorting, `09` union-find, `10` MST. Letter suffixes group variants (e.g., `08a`–`08f` for different sorts).
- Every method has a one-line docstring stating time/space complexity.
- Iterative implementations are preferred over recursive where both exist (recursive versions may be commented out).
- Type hints from `typing` (`Optional`, `Any`) are used throughout.
- No external dependencies — only Python stdlib.
