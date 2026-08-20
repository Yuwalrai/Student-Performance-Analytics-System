# Student Performance Analytics System

A Python-based student performance analytics system designed to analyze academic performance, attendance, study habits, engagement, and academic risk.

The project started as a data-analysis project using Pandas and gradually evolved into a structured, modular application with data cleaning, feature engineering, student reports, risk analysis, leaderboard generation, dashboard summaries, and a command-line interface.

The main goal of this project is to move beyond simply calculating student scores and instead use student data to identify patterns, performance levels, risks, engagement issues, and areas where students may need support.

---

## Project Goals

The system is designed to:

* Clean and validate student data.
* Analyze academic performance.
* Calculate and use student performance metrics.
* Identify academic risk levels.
* Analyze student engagement.
* Identify primary concerns and contributing factors.
* Generate individual student reports.
* Generate student rankings and leaderboards.
* Generate an overall dataset dashboard.
* Provide a simple command-line interface for interacting with the system.
* Keep responsibilities separated across modules for maintainability and future scalability.

---

## Main Features

### 1. Data Cleaning and Validation

The system processes the raw student dataset before analysis.

The cleaning workflow includes:

* Reading student data from CSV.
* Preserving the raw dataset.
* Handling missing values.
* Converting numeric columns to appropriate numeric types.
* Validating score ranges.
* Validating attendance values.
* Handling invalid or missing study-hour values.
* Checking duplicate roll numbers.
* Generating validation information before and after cleaning.

The project follows the principle that raw data should remain separate from processed data.

---

### 2. Feature Engineering

The system derives analytical features from the cleaned student data.

Examples include:

* Average score
* Best subject score
* Weakest subject score
* Best subject
* Weakest subject
* Risk level
* Engagement level
* Student status
* Risk contributing factors
* Engagement primary concern
* Risk primary concern
* Status primary concern
* Short and detailed explanations
* Recommended actions

The feature-engineering stage is responsible for creating analytical columns rather than the reporting layer.

This separation allows the reporting system to focus on displaying information instead of performing calculations.

---

## Risk Analysis

Students are categorized into different academic risk levels based on their performance.

The current risk categories are:

### HIGH_RISK

Students whose average score is below the high-risk threshold.

### MEDIUM_RISK

Students whose average score falls within the monitoring range.

### SAFE

Students whose performance currently meets the expected academic level.

The system also examines additional factors such as:

* Attendance
* Study hours
* Weakest subject

These factors are used to provide more meaningful explanations instead of simply displaying a risk label.

---

## Engagement Analysis

Student engagement is evaluated using attendance and study hours.

The current engagement categories include:

* HIGH_ENGAGEMENT
* MEDIUM_ENGAGEMENT
* LOW_ENGAGEMENT

The system can also identify contributing factors such as:

* Low attendance
* Limited study hours
* No significant contributing factors

It can determine which factor represents the primary engagement concern.

---

## Student Status

The system combines academic risk and engagement information to produce an overall student status.

Current statuses include:

* `CRITICAL_SUPPORT_NEEDED`
* `MONITOR_PROGRESS`
* `HIGH_POTENTIAL`
* `GENERAL`

This allows the system to move from isolated metrics toward a more meaningful overall interpretation of student performance.

---

# Individual Student Reports

The system can generate a report for an individual student using their roll number.

The report supports two detail levels:

* **Short**
* **Detailed**

The short version provides concise information suitable for normal viewing.

The detailed version provides additional explanation and context when more information is required.

The search interface validates the roll number and asks the user which report detail level they want.

---

# Leaderboard

The system provides a student leaderboard based on academic performance.

Students are ranked using their average score.

The leaderboard displays information such as:

* Rank
* Roll number
* Student name
* Average score
* Grade

The leaderboard supports requesting the top N ranks.

An important design decision is that **top N ranks means rank range, not necessarily N students**.

For example:

```text
Rank 1    Student A
Rank 2    Student B
Rank 2    Student C
Rank 3    Student D
```

Requesting the top 2 ranks includes:

```text
Student A
Student B
Student C
```

because both Student B and Student C hold rank 2.

The ranking logic is kept separate from the display/reporting logic.

---

# Dashboard

The system provides an overall command-line dashboard containing several analytical sections.

The dashboard currently includes:

## Dataset Overview

Displays:

* Total students
* Average score
* Highest score
* Lowest score
* Average attendance
* Average study hours

## Grade Distribution

Displays the number of students in each grade category.

## Risk Level Distribution

Displays the number of students in each risk category.

## Engagement Level Distribution

Displays the number of students in each engagement category.

## Student Status Distribution

Displays the number of students in each overall status category.

The dashboard is designed as a reporting layer and does not create analytical columns itself.

---

# Command-Line Interface

The system includes a menu-driven command-line interface.

Current menu options:

```text
1. Search Student Report
2. View Leaderboard
3. View Dashboard
4. Exit
```

The menu system is separated into individual responsibilities.

### Menu Components

#### `display_menu()`

Builds and returns the menu interface.

#### `get_menu_choice()`

Handles menu input and validation.

It repeatedly asks the user for input until a valid choice between 1 and 4 is provided.

#### `handle_search()`

Coordinates the student report workflow.

It:

1. Requests a roll number.
2. Validates the roll number.
3. Checks whether the student exists.
4. Requests the report detail level.
5. Generates the student report.
6. Returns the report.

#### `handle_leaderboard()`

Coordinates leaderboard interaction.

It:

1. Requests the maximum rank.
2. Validates the requested range.
3. Calls the leaderboard builder.
4. Returns the result.

#### `handle_dashboard()`

Calls the dashboard builder and returns the generated dashboard.

#### `handle_exit()`

Creates and returns the exit message.

#### `run_menu()`

Acts as the main controller for the CLI.

It:

1. Displays the menu.
2. Gets the user's choice.
3. Routes the choice to the appropriate handler.
4. Prints the returned result.
5. Repeats until the user selects Exit.

---

# Modular Design

One of the main goals of this project was learning how to structure a growing Python application rather than putting everything into one file.

The project separates responsibilities into different modules.

A simplified structure is:

```text
student_performance_system/
│
├── src/
│   ├── main.py
│   ├── cleaning.py
│   ├── feature_engineering.py
│   ├── reports.py
│   ├── ranking.py
│   ├── students_report.py
│   ├── menu.py
│   └── ...
│
├── students.csv
├── README.md
├── .gitignore
└── ...
```

The exact structure may change as the project evolves.

The main architectural principle is:

```text
Data
  ↓
Cleaning
  ↓
Feature Engineering
  ↓
Analysis
  ↓
Reporting
  ↓
CLI Interface
```

Each layer has its own responsibility.

---

# Reporting Design

The reporting layer focuses on **displaying existing data** rather than recalculating or creating analytical features.

For example, distribution reporting uses existing columns such as:

```text
risk_flag
engagement_level
student_status
```

A reusable distribution-building function was created so multiple sections can share the same logic.

Conceptually:

```text
build_distribution_section()
        ↑
        │
 ┌──────┼────────┬─────────────┐
 │      │        │             │
Grade   Risk   Engagement    Status
```

This improves:

* Reusability
* Maintainability
* Readability
* Scalability

---

# Design Principles Practiced

Throughout the project, the implementation focused on several software-engineering principles.

### Single Responsibility

Functions and modules should have clear responsibilities.

For example:

* Cleaning cleans.
* Feature engineering creates features.
* Reporting displays information.
* Handlers manage user interaction.
* `run_menu()` controls application flow.

### Reusability

Common logic is extracted into reusable functions rather than duplicated.

### Maintainability

The project is structured so that changing one part does not require rewriting unrelated parts.

### Scalability

The menu and reporting architecture are designed so that additional features can be added later without turning the application into one large function.

### Separation of Concerns

Data processing, analysis, reporting, and user interaction are kept separate.

---

# Technologies Used

* Python
* Pandas
* Matplotlib
* CSV
* Git
* GitHub

---

# What I Learned

This project was not only about learning Pandas.

It was also used to practice moving from writing individual pieces of Python code toward designing a larger application.

Key areas practiced include:

* Data cleaning
* Pandas DataFrames
* Feature engineering
* Conditional logic
* Data analysis
* `value_counts()`
* `mean()`
* `max()`
* `min()`
* Ranking
* Sorting DataFrames
* Iterating through DataFrames
* String formatting
* Input validation
* Exception handling
* Nested loops
* Function return values
* Modular programming
* Separation of responsibilities
* CLI application design
* Git and GitHub workflow

A particularly important lesson was understanding that good code is not only about making the program work. It should also be readable, maintainable, reusable, and capable of growing.

---

# Future Improvements

This version represents the completed baseline CLI application.

Possible future improvements include:

* Web-based dashboard
* Interactive visualizations
* Database integration
* Student comparison
* More advanced analytics
* Historical performance tracking
* More detailed recommendations
* Authentication and user roles
* Teacher/admin interfaces
* Exporting reports to PDF
* API integration
* Automated testing
* More advanced machine-learning-based risk prediction

These features are intentionally left for future iterations rather than being mixed into the current baseline project.

---

# Project Status

**Completed — Baseline CLI Version**

The current version provides the core student-performance analytics workflow, reporting system, leaderboard, dashboard, and command-line interface.

Future development can build on this foundation without changing the core separation of responsibilities.
