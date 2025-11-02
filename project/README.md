# Bit Packing Compression Project

**Software Engineering Project 2025 – Université Côte d’Azur**  
**Author:** Benjamin Foulcher  
**Supervisor:** JC Regin  

---

## Description

This project implements several integer compression methods using **Bit Packing**, with the goal of reducing transmission time while preserving **direct access** to elements in the compressed form.

Three independent compression strategies are implemented:

| **v1** | Aligned compression — each integer fits exactly into a 32-bit block. |
| **v2** | Overlapping compression — integers may span across two consecutive 32-bit blocks. |
| **overflow** | Compression with overflow zones for outliers requiring more bits. |

Each version supports the following methods:
- `compress(array)` → compresses a list of integers  
- `decompress()` → reconstructs the original list  
- `get(i)` → directly retrieves the *i*-th element without decompressing the entire array  

---

## Requirements

**Python version:** 3.10 or later (my version is 3.13.2)
(no additional external dependencies required)

To verify your Python version:
python --version


## How to Run

### 1. Run the benchmark (compare all versions)

To execute the benchmark that compares the three compression strategies, open a terminal **at the root of the project** and type:

python -m benchmark.test

### 2. Run the main (an example)

A simple demonstration is available in examples/example_main.py to test one compression mode directly.
To execute the main, open a terminal **at the root of the project** and type:

python -m example_main

You can modify the code inside example_main.py to test other modes:

bp = make_bitpacker("simple", 12)
bp = make_bitpacker("overlap", 12)
bp = make_bitpacker("overflow", 12, overflow_limit=8)