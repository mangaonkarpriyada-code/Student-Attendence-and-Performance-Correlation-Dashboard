# Student Attendance & Performance Dashboard

An interactive data analysis and visualization dashboard built using Python, Pandas, NumPy, Matplotlib, and Streamlit to analyze student attendance and academic performance.

## Project Overview

The Student Attendance & Performance Dashboard analyzes student attendance, assignment scores, internal marks, and overall academic performance.

The project applies data preprocessing, statistical analysis, correlation analysis, and data visualization to identify performance patterns and students who may require additional academic attention.

## Objectives

* Analyze student attendance and academic performance
* Study the relationship between attendance and overall performance
* Categorize students based on attendance and performance
* Identify students who may be at risk academically
* Compare attendance and performance across different months
* Provide an interactive dashboard for exploring student data

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Streamlit
* CSV Data Handling

## Key Features

* Interactive KPI cards
* Student name search
* Department filtering
* Student status filtering
* Top 5 performing students
* Individual student performance details
* Attendance vs academic performance analysis
* Attendance-performance correlation analysis
* Performance category distribution
* Attendance category distribution
* Performance percentage pie chart
* Monthly attendance comparison
* Monthly performance comparison
* At-risk student identification
* Complete student data table
* Download filtered student data as CSV

## Data Analysis

The project performs the following data analysis tasks:

* Data loading using Pandas
* Data inspection and preprocessing
* Missing-value detection
* Attendance categorization
* Performance categorization
* Statistical analysis
* Correlation analysis
* Grouping and aggregation
* Monthly performance analysis
* Student risk identification

## Project Structure

text
Student_Attendance_Performance_Dashboard/
│
├── data/
│   ├── student_data.csv
│   └── processed_student_data.csv
│
├── charts/
├── screenshots/
│
├── analysis.py
├── dashboard.py
├── requirements.txt
└── README.md

## Dashboard

The Streamlit dashboard provides an interactive interface for analyzing student data.

Users can:

* Filter students by department and status
* Search for individual students
* View student-specific performance details
* Analyze attendance and performance relationships
* Compare monthly attendance and performance
* Identify at-risk students
* View performance distributions
* Download filtered data

## Project Demo

[Watch the project demonstration on YouTube](https://youtu.be/ZM9gi02OU7E?si=IBbXMqJ75j2p7T_W)

### Dashboard Overview

![Dashboard Overview](screenshots/dashboard.png)

### Analytics

![Analytics](screenshots/analytics.png)

### Risk and Student Data

![Risk and Data](screenshots/risk.png)

## Key Insight

The analysis of the sample dataset shows a strong positive relationship between student attendance and overall academic performance.

The dashboard also helps identify students with lower attendance and academic performance who may require additional academic support.

## Installation and Setup

### 1. Clone the Repository

bash
git clone https://github.com/mangaonkarpriyada-code/Student_Attendance_Performance_Dashboard.git

### 2. Navigate to the Project Directory

bash
cd Student_Attendance_Performance_Dashboard

### 3. Install Required Libraries

bash
pip install -r requirements.txt


### 4. Run the Dashboard

bash
python -m streamlit run dashboard.py

The dashboard will open in your default web browser.

## Requirements

The project requires the following Python libraries:

text
pandas
numpy
matplotlib
streamlit
openpyxl

These dependencies are also listed in `requirements.txt`.

## Future Enhancements

Possible future improvements include:

* Adding larger and real-world datasets
* Adding authentication for different users
* Adding advanced predictive analysis
* Adding downloadable reports
* Deploying the dashboard online
* Adding more advanced interactive visualizations

## Author

Priyada Mangaonkar

Computer Engineering Student

GitHub:
https://github.com/mangaonkarpriyada-code
