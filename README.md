



# MathVerse 

 MathVerse is a simple, modular, and user-friendly terminal-based mathematical calculator built with Python. It brings together common mathematical operations like statistics, matrix calculations, polynomial operations, geometry, and number theory in one place.

 I built MathVerse to make everyday mathematical calculations easier from the terminal. Instead of relying on complicated tools or large third-party libraries, the project focuses on being lightweight, easy to understand, and reliable. It also handles invalid inputs properly, so a simple typo does not crash the entire program.

 ## Features

 ###  Descriptive Statistics

 Enter a list of numbers separated by spaces and quickly calculate:

 - Mean
- Median
- Mode and multi-modal data
- Variance
- Population standard deviation
- Sample standard deviation

 ###  Matrix Operations

 MathVerse supports several basic matrix operations, including:

 - Matrix addition
- Matrix subtraction
- Matrix multiplication
- Matrix transpose
- Matrix determinant

 The program checks matrix dimensions before performing operations to prevent invalid calculations and confusing errors.

 ###  Polynomial Calculator

 The polynomial module allows you to:

 - Evaluate polynomials for a given value of x
- Calculate the symbolic derivative of a polynomial
- Use Horner's method for efficient polynomial evaluation

 ###  Geometry Calculator

 The geometry module provides calculations for common 2D and 3D shapes, including:

 - Circles
- Rectangles
- Triangles
- Spheres
- Cylinders

 For triangles, the program uses Heron's formula and checks whether the given side lengths can form a valid triangle.

 ###  Number Theory

 The number theory section includes:

 - Greatest Common Divisor (GCD)
- Least Common Multiple (LCM)
- Prime factorization

 The GCD and LCM calculations are implemented using the Euclidean algorithm.

 ### 📝 Calculation History

 MathVerse keeps a record of calculations in:

 logs/session\_history.txt

 Each entry includes a timestamp, making it easy to review previous calculations.

 ## Project Structure

 The project is divided into separate modules so that each part of the application has a clear responsibility.

 mathverse/\
 │\
 ├── main.py # Main menu and program entry point\
 │\
 ├── utils/\
 │ ├── validators.py # Handles and validates user input\
 │ └── logger.py # Saves calculation history\
 │\
 ├── modules/\
 │ ├── statistics\_calc.py # Statistical calculations\
 │ ├── matrix\_calc.py # Matrix and linear algebra operations\
 │ ├── polynomial\_calc.py # Polynomial operations\
 │ ├── geometry\_calc.py # 2D and 3D geometry calculations\
 │ └── number\_theory.py # GCD, LCM, and prime factorization\
 │\
 ├── tests/\
 │ └── test\_math\_modules.py # Tests for core calculation modules\
 │\
 ├── statement.md # Project scope and problem description\
 └── README.md # Project documentation

 ## Why I Built It

 The main goal of MathVerse is to create a calculator that is simple, modular, and easy to use while demonstrating important Python concepts such as functions, modules, input validation, error handling, algorithms, file handling, and unit testing.

 Instead of putting everything into one large file, the project separates different mathematical operations into their own modules. This makes the code easier to understand, maintain, test, and expand in the future.

 ## Technologies Used

 - Python
- Python Standard Library
- Modular programming
- File handling
- Unit testing
- Basic mathematical algorithms

 ## Future Improvements

 Some features that could be added in the future include:

 - More advanced statistical functions
- Additional matrix operations
- Graph plotting
- More geometry formulas
- A graphical user interface
- Exporting calculation history
- More automated tests

 ## Conclusion

MathVerse is a practical Python project designed to make common mathematical calculations simple and accessible through the terminal.
 MathVerse is a practical Python project designed to make common mathematical calculations simple and accessible through the terminal.

 MathVerse 🧮 — Making everyday mathematics simpler, one calculation at a time.
