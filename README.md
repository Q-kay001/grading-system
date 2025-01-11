# School Grading System

This is a Python-based school grading system that allows users to input students' names and scores to assign appropriate grades based on a predefined grading scale.

## Features

- Accepts user input for student names and scores.
- Assigns grades (A, B, C, D, F) based on the input scores.
- Handles invalid inputs gracefully.
- Interactive and user-friendly command-line interface.

## Grading Scale

| Score Range       | Grade |
|-------------------|-------|
| 90 - 100         | A     |
| 80 - 89          | B     |
| 70 - 79          | C     |
| 60 - 69          | D     |
| 0 - 59           | F     |

## Getting Started

### Prerequisites

Ensure you have Python installed on your system (version 3.6 or higher).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/school-grading-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd school-grading-system
   ```

### Usage

1. Run the script:
   ```bash
   python grading_system.py
   ```
2. Follow the prompts to:
   - Enter the student's name.
   - Input the student's score (between 0 and 100).
3. The system will display the student's name, score, and corresponding grade.

### Example

```text
Welcome to the School Grading System
Enter "exit" at any time to quit.

Enter the student's name: Alice
Enter Alice's score: 85
Alice's grade is: B

Enter the student's name: Bob
Enter Bob's score: 45
Bob's grade is: F

Enter the student's name: exit
Exiting the grading system. Goodbye!
```

## Error Handling

- **Invalid Score Input**: If the input is not numeric or out of the 0-100 range, the system will prompt the user to enter a valid score.
- **Exit Command**: Users can type "exit" at any time to terminate the program.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by the need for simple and interactive grading tools.
- Designed for educational purposes.
