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

- [Interactive Input: Users can input the objective function and constraints in plain text.]
- [Step-by-Step Execution: Displays the Simplex Tableau at each iteration.]
- [Optimal Solution Display: Shows final values of decision variables and the optimal objective value.]
- [Graphical Visualization: For 2-variable problems, the feasible region and optimal point are plotted.]
- [Error Handling: Basic input validation and feedback.]


## Screenshots

![Main Interface](https://private-user-images.githubusercontent.com/154216157/457574166-9c51117e-2309-4401-a06f-2068cdf2e2d9.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTA1MDQ3MDcsIm5iZiI6MTc1MDUwNDQwNywicGF0aCI6Ii8xNTQyMTYxNTcvNDU3NTc0MTY2LTljNTExMTdlLTIzMDktNDQwMS1hMDZmLTIwNjhjZGYyZTJkOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYyMVQxMTEzMjdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zOTUzY2JiYjlkNGJkN2UxZDgxMTVhY2RiY2QxOTJkYTIxYzZjMWY0ZGQxNGVmNjE1NjE1NzcwZGQxOWQ5OWY3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.HEAx9RDM9iUbEooml0Z-IuMx1O2jLpV2n6ZZNnfl0Oo)


![Algorithm in Action](https://private-user-images.githubusercontent.com/154216157/457574218-49e08ad5-2c78-4319-a6a9-851531842cee.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTA1MDQ3MzMsIm5iZiI6MTc1MDUwNDQzMywicGF0aCI6Ii8xNTQyMTYxNTcvNDU3NTc0MjE4LTQ5ZTA4YWQ1LTJjNzgtNDMxOS1hNmE5LTg1MTUzMTg0MmNlZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYyMVQxMTEzNTNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iNDZjYzBlMjM1MGQyZDg1ODY3YmE5MWM2MDI0ZTAwYzFlYjU5ZDRmN2VhYzg1NTcwNmI1MTIyYzE3YmVmYjhkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.D30vuPqbDZ5IHI1baXvPFFQj8W0yDTN3X2qDvKr6fYk)

![Algorithm in Action 2](https://private-user-images.githubusercontent.com/154216157/457574246-2e499591-46d4-4e92-8f2c-4708bf38f859.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTA1MDQ3NDUsIm5iZiI6MTc1MDUwNDQ0NSwicGF0aCI6Ii8xNTQyMTYxNTcvNDU3NTc0MjQ2LTJlNDk5NTkxLTQ2ZDQtNGU5Mi04ZjJjLTQ3MDhiZjM4Zjg1OS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYyMVQxMTE0MDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01NmFjODQyMWFmYTNhY2ZkNTA3MTFlMmNkMGY0NDkyNjllYTRlY2FkZDkzNmNlOGRkY2E1ZjdiMTc5OGVjOGZlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.F2UBF2TvJiVhX6QSErTjt2CM7frwyvFPIBDD6w8thv4)




## Installation

### Prerequisites

- Python 3.8 or higher
- Git
- Streamlit Cloud

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

1. [Enter the objective function coefficients
      Provide the coefficients of the function you want to maximize]
2. [Enter the constraints in matrix form (A·x ≤ b)
      Input the constraint coefficients (A) row by row, and the right-hand side values (b) in a separate field.]
3. [Click "Solve" to compute the solution
      The app will run the Simplex algorithm and compute the optimal solution step by step.]
4. [Review the results and solution steps
      Examine the optimal values, final objective value, and each iteration's Simplex tableau.
      If your problem has two variables, the feasible region will be plotted automatically.]

### Example Inputs

- [Objective Function:
   Maximize Z = 3x₁ + 2x₂

   Constraints:
   x₁ + 3x₂ ≤ 15  
   x₁ + x₂ ≤ 7  
   2x₁ + x₂ ≤ 12  
   x₁,x₂ ≥ 0

   Output:
   x₁ = 5  
   x₂ = 2  
   Max Z = 19]

- [Objective Function:
   Maximize Z = 5x₁ + 4x₂

   Constraints:
   6x₁ + 4x₂ ≤ 24  
   x₁ + 2x₂ ≤ 6  
   –x₁ + x₂ ≤ 1  
   x₁,x₂ ≥ 0

   Output:
   x₁ = 3  
   x₂ = 1.5 
   Max Z = 21]

- [Objective Function:
   Maximize Z = 3x₁ + 4x₂

   Constraints:
   -x₁ + 2x₂ ≤ 8  
   1x₁ + 2x₂ ≤ 12  
   2x₁ + 1x₂ ≤ 16 
   x₁,x₂ ≥ 0

   Output:
   x₁ = 6.66666
   x₂ = 2.66666
   Max Z = 30.66666]

## Implementation Details

### Key Components

- `algorithm.py`: Implements the core Simplex algorithm logic, including tableau generation, pivot operations, and solution steps.
- `app.py`: The main Streamlit web application that handles user input, triggers the algorithm, and displays results and visualizations.
- `utils.py`: Contains helper functions for parsing user input (objective function and constraints) and formatting the simplex tableau.
- `test_algorithm.py`: Includes unit tests to validate correctness of the algorithm under various input conditions.

### Code Highlights

```python
# Include a few key code snippets that demonstrate the most important parts of your implementation
def pivot(tableau, pivot_row, pivot_col):
    """
    Perform a pivot operation on the simplex tableau.
    
    - Divides the pivot row by the pivot element to make it 1.
    - Eliminates other values in the pivot column to make them 0.
    """
    pivot_element = tableau[pivot_row][pivot_col]
    tableau[pivot_row] = [val / pivot_element for val in tableau[pivot_row]]

    for i in range(len(tableau)):
        if i != pivot_row:
            multiplier = tableau[i][pivot_col]
            tableau[i] = [
                tableau[i][j] - multiplier * tableau[pivot_row][j]
                for j in range(len(tableau[i]))
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
