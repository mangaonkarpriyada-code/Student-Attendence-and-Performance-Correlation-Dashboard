import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load student dataset
df = pd.read_csv("data/student_data.csv")

# Display the first 5 records
print("First 5 Student Records:")
print(df.head())

# Display information about the dataset
print("\nDataset Information:")
print(df.info())

# Display basic statistics
print("\nStatistical Summary:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Students with attendance below 75%
low_attendance = df[df["Attendance_Percentage"] < 75]

print("\nStudents with Attendance Below 75%:")
print(low_attendance[["Student_ID", "Student_Name", "Attendance_Percentage"]])


# Top-performing students
top_students = df.sort_values(
    by="Overall_Percentage",
    ascending=False
).head(5)

print("\nTop 5 Performing Students:")
print(top_students[["Student_ID", "Student_Name", "Overall_Percentage"]])


# Lowest-performing students
low_students = df.sort_values(
    by="Overall_Percentage",
    ascending=True
).head(5)

print("\nLowest 5 Performing Students:")
print(low_students[["Student_ID", "Student_Name", "Overall_Percentage"]])

# Create Attendance Category

def attendance_category(attendance):
    if attendance >= 85:
        return "High"
    elif attendance >= 75:
        return "Moderate"
    else:
        return "Low"


df["Attendance_Category"] = df["Attendance_Percentage"].apply(
    attendance_category
)

print("\nAttendance Categories:")
print(
    df[
        [
            "Student_Name",
            "Attendance_Percentage",
            "Attendance_Category"
        ]
    ]
)

# Create Performance Category

def performance_category(marks):
    if marks >= 75:
        return "Excellent"
    elif marks >= 60:
        return "Good"
    elif marks >= 40:
        return "Average"
    else:
        return "Poor"


df["Performance_Category"] = df["Overall_Percentage"].apply(
    performance_category
)

print("\nPerformance Categories:")
print(
    df[
        [
            "Student_Name",
            "Overall_Percentage",
            "Performance_Category"
        ]
    ]
)

# Calculate correlation between attendance and performance

correlation = df["Attendance_Percentage"].corr(
    df["Overall_Percentage"]
)

print("\nAttendance-Performance Correlation:")
print(correlation)

import matplotlib.pyplot as plt

# Scatter plot with trendline

x = df["Attendance_Percentage"]
y = df["Overall_Percentage"]

plt.scatter(x, y, label="Students")

# Calculate trendline
import numpy as np

trendline = np.polyfit(x, y, 1)
trendline_function = np.poly1d(trendline)

plt.plot(
    x,
    trendline_function(x),
    label="Trendline"
)

plt.xlabel("Attendance Percentage")
plt.ylabel("Overall Percentage")
plt.title("Attendance vs Academic Performance")
plt.legend()

plt.show()

# Average performance by attendance category

average_performance = df.groupby(
    "Attendance_Category"
)["Overall_Percentage"].mean()

print("\nAverage Performance by Attendance Category:")
print(average_performance)

# Bar chart: Average performance by attendance category

average_performance.plot(kind="bar")

plt.xlabel("Attendance Category")
plt.ylabel("Average Overall Percentage")
plt.title("Average Performance by Attendance Category")

plt.show()

# Histogram: Attendance Distribution
plt.hist(df["Attendance_Percentage"], bins=5)

plt.xlabel("Attendance Percentage")
plt.ylabel("Number of Students")
plt.title("Attendance Distribution")

plt.show()

# Pie Chart: Performance Category Distribution
performance_counts = df["Performance_Category"].value_counts()

performance_counts.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Performance Category Distribution")
plt.ylabel("")

plt.show()

# Student Status Analysis
def student_status(row):
    if (
        row["Attendance_Percentage"] < 75
        and row["Overall_Percentage"] < 60
    ):
        return "At Risk"
    elif row["Attendance_Percentage"] < 75:
        return "Low Attendance"
    elif row["Overall_Percentage"] < 60:
        return "Low Performance"
    else:
        return "Normal"


df["Status"] = df.apply(student_status, axis=1)

print("\nStudent Status:")
print(
    df[
        [
            "Student_Name",
            "Attendance_Percentage",
            "Overall_Percentage",
            "Status"
        ]
    ]
)

# Save processed student data
df.to_csv("data/processed_student_data.csv", index=False)

print("\nProcessed student data saved successfully!")