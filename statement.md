
# Problem & Scope Statement: MathVerse

## 1. Problem Statement
When studying or working through coursework in engineering and computer science, students frequently need to check intermediate computational steps across varied mathematical topics—such as descriptive statistics, linear algebra, calculus, geometry, and number theory[cite: 7]. 

Most quick command-line scripts are written as fragile, monolithic one-offs that crash immediately if a user accidentally enters a space, letter, or mismatched dimension[cite: 3, 7]. On the other end of the spectrum, professional mathematical tools often require extensive package installations or complex syntax just to check a quick 3x3 determinant or evaluate a polynomial[cite: 3, 7]. 

MathVerse solves this by providing a reliable, zero-dependency, crash-resistant terminal application that handles common academic computations with clear error messages, formatted step-by-step output, and automatic session logging[cite: 7].

---

## 2. Scope of the Project
MathVerse covers core foundational math domains commonly encountered in early engineering curricula[cite: 7]:

* **Descriptive Statistics**: Real-time evaluation of data spreads, including mean, median, multi-modal analysis, and both sample and population dispersion metrics[cite: 5, 7].
* **Linear Algebra**: Matrix addition, subtraction, dimension-checked matrix multiplication, transposition, and recursive Laplace expansion for determinants of square matrices[cite: 3, 7].
* **Polynomial Operations**: Evaluation of polynomials using Horner's method ($O(n)$ time complexity) along with automatic generation and evaluation of symbolic first derivatives[cite: 4, 7].
* **2D & 3D Euclidean Geometry**: Dimension, perimeter, surface area, and volume calculations, including validity checks like the triangle inequality theorem prior to computing Heron's formula[cite: 1, 7].
* **Number Theory**: Prime factorization and Euclidean algorithm implementations for Greatest Common Divisor (GCD) and Least Common Multiple (LCM)[cite: 6, 7].
* **Session Persistence**: Automatic recording of calculations and outputs to a local log file for auditing and later review[cite: 7].

The project deliberately scopes out heavy symbolic calculus systems, graphical plotting interfaces, and external binary dependencies to remain lightweight and fully portable across any environment with standard Python 3[cite: 7].

---

## 3. Target Users
* **Engineering & CS Students**: For quickly verifying assignment steps, verifying matrix multiplication hand calculations, or checking statistical summaries[cite: 3, 5, 7].
* **Academic Instructors & Tutors**: For quickly generating verified solution keys and step checks during grading[cite: 7].
* **Self-Learners & Programmers**: As a reference implementation of pure Python mathematical algorithms without third-party libraries[cite: 7].

---

## 4. High-Level Features
* **Zero External Dependencies**: Implemented strictly using the Python Standard Library (`math`, `collections`, `os`, `sys`, `datetime`, `unittest`)[cite: 1, 5, 7].
* **Robust Input Guarding**: Input prompts loop continuously on unexpected characters or empty entries instead of crashing the program with unhandled exceptions[cite: 7].
* **Human-Readable Output Formatting**: Displays formatted matrices, clean polynomial string representations ($P(x)$ and $P'(x)$), and clear metric tables[cite: 3, 4, 7].
* **Automated Unit Test Suite**: Comprehensive tests validating mathematical edge cases (e.g., multi-modal datasets, determinant signs, prime numbers)[cite: 3, 5, 7].
* **Session Logging**: Maintains a timestamped history in `logs/session_history.txt` so users never lose prior calculations when closing a menu[cite: 7].
