# Dojo Data Structures

## Practical Exercise

The objective of this exercise is to practice different programming concepts and techniques related to CSV data manipulation using list comprehension, dict comprehension, set comprehension, iterators, iterables, generators, and coroutines.

The provided CSV file contains information about students, including their name, last name, city, country, age, and university major. The following tasks should be performed:

1. Read the CSV file and load the data into a suitable data structure.

2. Create a menu where the user can query the following information and generate a report in a new file:
   - Get all students belonging to a given city.
   - Get all students living in a given country.
   - Get all students within a given age range.
   - Get all cities of residence of the students.
   - Identify the average age per major.
   - Indicate, for each major, whether the student is above or below the average age.
   - Group the students into different age ranges (18-25, 26-35, over 35).
   - Identify the city with the greatest variety of university majors among the students.

Note: You can add any additional information you want to the report.

It is important to use the appropriate Python tools, such as the `csv` library, to read and manipulate the CSV file data. Additionally, the mentioned techniques and concepts should be applied to practice and demonstrate understanding of them.

The exercise aims to reinforce the use and combination of these techniques to efficiently and elegantly manipulate and analyze data.

## Installation

1. **Fork the Project:** First, create your own copy of this project repository by "forking" it on GitHub. If you're not familiar with forking, you can learn more about it [here](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo).

2. Clone the **repository**

   ```
   git clone https://github.com/jpcadena/dojo_datastructures.git
   ```

3. Change the directory to the **root project**

   ```
   cd dojo_datastructures
   ```

4. Create a **virtual environment** named _venv_

   ```
   python3 -m venv venv
   ```

5. Activate the **environment** on Windows

   ```
   .\venv\Scripts\activate
   ```

   Or on Unix/Mac OS X

   ```
   source venv/bin/activate
   ```

6. Install the required packages using PIP
   ```
   pip install -r requirements.txt
   ```

## Exercise

For this exercise, you need to implement various functions to manipulate and analyze the data from the CSV file. You should organize your code into modules and functions to ensure modularity and reusability.

The tasks to be implemented are as follows:

1. Read the CSV file and load the data into a suitable data structure.

2. Implement functions to query and generate reports based on user input. These functions should handle the following queries:

   - Get all students belonging to a given city.
   - Get all students living in a given country.
   - Get all students within a given age range.
   - Get all cities of residence of the students.
   - Identify the average age per major.
   - Indicate, for each major, whether the student is above or below the average age.
   - Group the students into different age ranges (18-25, 26-35, over 35).
   - Identify the city with the greatest variety of university majors among the students.

3. Implement a function to write the generated reports to separate CSV files.

4. Create a main program that provides a user interface to interact with the functions and generate the reports based on user input.

After completing the exercise, make sure to document your code, add comments, and follow good coding practices to ensure readability and maintainability of the project.

## How to Contribute

1. Fork the repository to create your own copy.

2. Create a new branch for your changes.

3. Make the necessary changes and additions to the code.

4. Test your changes to ensure they work as expected.

5. Commit your changes and push them to your forked repository.

6. Create a pull request to submit your changes for review.

7. Wait for the maintainers to review your changes and merge them into the main repository.

8. Thank you for contributing! Your efforts are greatly appreciated.

## Resources

- [Python CSV Documentation](https://docs.python.org/3/library/csv.html)
- [List Comprehensions](https://realpython.com/list-comprehension-python/)
- [Dict Comprehensions](https://realpython.com/python-dicts/)
- [Set Comprehensions](https://realpython.com/python-sets/)
- [Iterators and Iterables](https://realpython.com/python-iterators/)
- [Generators](https://realpython.com/introduction-to-python-generators/)
- [Coroutines](https://realpython.com/async-io-python/)
