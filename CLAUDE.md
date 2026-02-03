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

Python 3.10+ (uses modern type hints: PEP 604 `X | None` and PEP 585 `list[int]`).

## Code Conventions

- Files are numbered by topic: `01` hash tables, `02` linked lists, `03` stack, `04` queue, `05` trees/heaps/tries, `06` graphs, `07` search, `08` sorting, `09` union-find, `10` MST. Letter suffixes group variants (e.g., `08a`–`08f` for different sorts).
- Every method has a one-line docstring stating time/space complexity.
- Iterative implementations are preferred over recursive where both exist (recursive versions may be commented out). Exceptions: `UnionFind.find()` uses recursion for conciseness (standard textbook path compression), and `BinarySearchTreeNode.delete()` uses recursion as iterative BST deletion is significantly more complex.
- Type hints from `typing` (`Any`) and PEP 604 union syntax (`X | None`) are used throughout.
- All files include `from __future__ import annotations` for consistent forward reference handling.
- No external dependencies — only Python stdlib.

## Complexity Notation

Every method includes a one-line docstring with time and space complexity. Variables used: `n` (elements), `k` (key length), `m` (word/prefix length), `h` (tree height), `d` (node depth), `V` (vertices), `E` (edges), `α(n)` (inverse Ackermann). Unlabeled complexity is worst case; only average/best cases are explicitly labeled. Space complexity is auxiliary (excluding inputs/outputs) and includes the cost of called methods.

## Commented Code

**IMPORTANT:** Commented-out code sections are educational and show alternative implementations (e.g., recursive vs iterative approaches). They must be maintained with the same standards as active code:

- Apply the same type hint conventions (PEP 604 `X | None`, no `Optional`, no quoted forward references)
- Keep docstrings and complexity annotations accurate
- Update commented code when refactoring affects it

When making changes to the codebase, always check if similar changes are needed in commented sections.
