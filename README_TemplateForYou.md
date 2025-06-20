# [Linear Programming Simplex Method] - Interactive Visualization

## Project Overview

This project is an interactive web application that implements and visualizes [Linear Programming Simplex Method], developed as part of the Algorithms and Programming II course at Fırat University, Software Engineering Department.

## Algorithm Description

[Provide a comprehensive explanation of your algorithm here. Include the following elements:]

### Problem Definition

[The Simplex Algorithm is used to solve linear programming (LP) problems that aim to optimize (maximize or minimize) a linear objective function, subject to a set of linear inequality or equality constraints.]

### Mathematical Background

[The Simplex Algorithm iteratively moves along the edges of the feasible region defined by constraints to find the optimal vertex (corner point) where the objective function is optimized.]

### Algorithm Steps

1. Convert the constraints into standard form (add slack variables).
2. Create the initial simplex tableau.
3. Identify the entering and leaving variables.
4. Perform pivot operations to improve the objective value.
5. Repeat until no further improvement is possible (optimal solution found).

### Pseudocode

```
1. Initialize simplex tableau.
2. While there is a negative value in the bottom row (objective row):
   a. Choose entering variable (most negative coefficient).
   b. Determine leaving variable using minimum ratio test.
   c. Pivot to make entering variable basic.
3. Read solution from the final tableau.]
```

## Complexity Analysis

### Time Complexity

- **Best Case:** O(n) - [Solution found in first iteration]
- **Average Case:** O(mn) - [Polynomial time in practice]
- **Worst Case:** - [Exponential (rare in real problems)]

### Space Complexity

- O(mn) - [Where m is number of constraints and n is number of variables]

## Features

- [Interactive input of objective function and constraints]
- [Step-by-step visualization of the Simplex Tableau]
- [Displays optimal solution and maximum value]
...

## Screenshots

![Main Interface](docs/screenshots/main_interface.png)
*Caption describing the main interface*

![Algorithm in Action](docs/screenshots/algorithm_demo.png)
*Caption describing the algorithm in action*

## Installation

### Prerequisites

- Python 3.8 or higher
- Git

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. Create a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage Guide

1. [Enter the objective function        coefficients.]
2. [Enter constraints in matrix form Ax ≤ b.]
3. [Click Solve Linear Program to       compute solution.]
4. [Review the result and simplex tableau.]

### Example Inputs

- [Objective Function:
   Maximize Z = -3x₁ - 2x₂

   Constraints:
   x₁ + x₂ ≤ 4
   2x₁ + x₂ ≤ 5

   Output:
   x₁ = 1, x₂ = 3
   Max Z = -9]
- [Example 2 with expected output]
- [Example 3 with expected output]

## Implementation Details

### Key Components

- `algorithm.py`: Implements the simplex logic
- `app.py`: Streamlit web app interface
- `utils.py`: Helper methods for input parsing and formatting
- `visualizer.py`: Simplex tableau and steps visualizer

### Code Highlights

```python
# Include a few key code snippets that demonstrate the most important parts of your implementation
def pivot(tableau, pivot_row, pivot_col):
    """
    Performs a pivot operation to update the tableau
    """
    pivot_element = tableau[pivot_row][pivot_col]
    tableau[pivot_row] = [val / pivot_element for val in tableau[pivot_row]]
    for i in range(len(tableau)):
        if i != pivot_row:
            multiplier = tableau[i][pivot_col]
            tableau[i] = [
                val - multiplier * tableau[pivot_row][j]
                for j, val in enumerate(tableau[i])
            ]

```

## Testing

This project includes a test suite to verify the correctness of the algorithm implementation:

```bash
python -m unittest test_algorithm.py
```

### Test Cases

- [Test with multiple constraints and variables]
- [Validate optimality and pivot correctness]
- [Handle unbounded or infeasible cases]

## Live Demo

A live demo of this application is available at: [(https://algorithms-and-programming-ii-semester-capstone-project-itahap.streamlit.app/)]

## Limitations and Future Improvements

### Current Limitations

- [Limited to ≤ type constraints only]
- [Cannot handle equality (=) or ≥ directly]
- [No sensitivity analysis module]

### Planned Improvements

- [Add support for dual simplex]
- [Add graphical method for 2D problems]
- [Allow saving and loading LP problems]

## References and Resources

### Academic References

1. [Hillier & Lieberman (2015) - McGraw-Hill Education
   ISBN: 978-0073523453
   Simplex Method Chapter: Chapter 4 & 5]
2. [Winston, W.L. (2004) - Cengage Learning
   Simplex method with real-world examples]
3. [Taha, H.A. (2016) - Pearson Education]

### Online Resources

- [https://en.wikipedia.org/wiki/Simplex_algorithm]
- [(https://www.youtube.com/watch?v=9YKLXFqCy6E)]
- [https://www.pnw.edu/wp-content/uploads/2020/03/attendance5-1.pdf]

## Author

- **Name:** [Ibrahim Taha Pinar]
- **Student ID:** [230543019]
- **GitHub:** [itahapinar]

## Acknowledgements

I would like to thank Assoc. Prof. Ferhat UÇAR for guidance throughout this project, and [any other acknowledgements].

---

*This project was developed as part of the Algorithms and Programming II course at Fırat University, Technology Faculty, Software Engineering Department.*
