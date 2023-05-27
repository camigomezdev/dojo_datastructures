# Dojo Data Structures

## Practical exercise

# Student Report Generation Script

This Python script allows you to generate student reports based on data from a CSV file. It provides a menu-driven interface with various options for querying and analyzing the student data. This script is specifically designed as a practical exercise for Dojo Data Structure.

## Prerequisites

- Python 3.11
- CSV file named `data.csv` containing student data with columns: `nombre`, `apellido`, `ciudad`, `pais`, `edad`, and `carrera`

## Usage

1. Place the `data.csv` file in the same directory as the script file, `report.py`.
2. Run the script using Python 3.11: `python3.11 report.py`
3. The script will display a menu with options. Enter the desired option number to perform the corresponding action.
4. Follow the prompts to input any required information, such as city, country, or age range.
5. Reports will be generated as separate CSV files, providing relevant information based on the selected options.

## Options

1. Get all students from a given city
2. Get all students from a given country
3. Get all students within an age range
4. Get all cities of residence of the students
5. Identify the average age per major
6. Indicate for each major if the student is above or below the average age
7. Group the students into different age ranges
8. Identify the city with the highest variety of majors among the students
9. Exit

## Generated Reports

The script generates reports in CSV format. Each report corresponds to the selected option and contains relevant student information based on the chosen criteria.

## Contributing

Contributions to this script are welcome! If you have any suggestions, bug reports, or feature requests, please feel free to open an issue or submit a pull request on the GitHub repository.