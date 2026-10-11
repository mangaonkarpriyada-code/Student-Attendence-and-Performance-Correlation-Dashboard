import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="📊Student Attendance & Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load processed data
df = pd.read_csv("data/processed_student_data.csv")

# Sidebar Filter
st.sidebar.header("Filters")

departments = ["All"] + list(df["Department"].unique())

selected_department = st.sidebar.selectbox(
    "Select Department",
    departments
)

if selected_department != "All":
    df = df[df["Department"] == selected_department]

# Student Status Filter
statuses = ["All"] + list(df["Status"].unique())

selected_status = st.sidebar.selectbox(
    "Select Student Status",
    statuses
)

if selected_status != "All":
    df = df[df["Status"] == selected_status]

# Student Name Search
search_name = st.sidebar.text_input(
    "Search Student Name"
)

if search_name:
    df = df[
        df["Student_Name"].str.contains(
            search_name,
            case=False,
            na=False
        )
    ]

# Dashboard Title
st.title("Student Attendance & Performance Dashboard")

st.write(
    "An interactive dashboard to analyze student attendance "
    "and academic performance."
)

# KPI Cards
total_students = len(df)

average_attendance = df["Attendance_Percentage"].mean()

average_performance = df["Overall_Percentage"].mean()

at_risk_students = len(
    df[df["Status"] == "At Risk"]
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Students",
    total_students
)

col2.metric(
    "Average Attendance",
    f"{average_attendance:.1f}%"
)

col3.metric(
    "Average Performance",
    f"{average_performance:.1f}%"
)

col4.metric(
    "At-Risk Students",
    at_risk_students
)

# Top 5 Performing Students
st.subheader("Top 5 Performing Students")

top_students = df.sort_values(
    by="Overall_Percentage",
    ascending=False
).head(5)

st.dataframe(
    top_students[
        [
            "Student_ID",
            "Student_Name",
            "Attendance_Percentage",
            "Overall_Percentage",
            "Performance_Category"
        ]
    ],
    use_container_width=True
)

# Student Details
st.subheader("Student Details")

student_names = df["Student_Name"].tolist()

if len(student_names) > 0:

    selected_student = st.selectbox(
        "Select a Student",
        student_names
    )

    student = df[
        df["Student_Name"] == selected_student
    ].iloc[0]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Attendance",
        f"{student['Attendance_Percentage']}%"
    )

    col2.metric(
        "Assignment Score",
        student["Assignment_Score"]
    )

    col3.metric(
        "Internal Marks",
        student["Internal_Marks"]
    )

    col4.metric(
        "Overall Performance",
        f"{student['Overall_Percentage']}%"
    )

    st.write(
        f"**Performance Category:** "
        f"{student['Performance_Category']}"
    )

    st.write(
        f"**Attendance Category:** "
        f"{student['Attendance_Category']}"
    )

    st.write(
        f"**Student Status:** "
        f"{student['Status']}"
    )

else:
    st.warning("No students found with the selected filters.")

# Attendance vs Performance
st.subheader("Attendance vs Academic Performance")

correlation = df["Attendance_Percentage"].corr(
    df["Overall_Percentage"]
)

st.metric(
    "Attendance-Performance Correlation",
    f"{correlation:.2f}"
)

st.scatter_chart(
    df,
    x="Attendance_Percentage",
    y="Overall_Percentage"
)

# Average Performance by Attendance Category
st.subheader("Average Performance by Attendance Category")

category_performance = df.groupby(
    "Attendance_Category"
)["Overall_Percentage"].mean()

st.bar_chart(category_performance)

# Performance Category Distribution
st.subheader("Performance Category Distribution")

performance_counts = df["Performance_Category"].value_counts()

st.bar_chart(performance_counts)

# Attendance Category Distribution
st.subheader("Attendance Category Distribution")

attendance_counts = df["Attendance_Category"].value_counts()

st.bar_chart(attendance_counts)

# Performance Category Pie Chart
st.subheader("Performance Category Percentage")

performance_pie = df["Performance_Category"].value_counts()

fig, ax = plt.subplots(figsize=(3, 3))

ax.pie(
    performance_pie,
    labels=performance_pie.index,
    autopct="%1.1f%%",
    textprops={"fontsize": 8}
)

ax.set_title(
    "Performance Category Percentage",
    fontsize=10
)

st.pyplot(fig)

# Monthly Performance Comparison
st.subheader("Monthly Performance Comparison")

monthly_performance = df.groupby(
    "Month"
)["Overall_Percentage"].mean()

st.line_chart(monthly_performance)

# Monthly Attendance Comparison
st.subheader("Monthly Attendance Comparison")

monthly_attendance = df.groupby(
    "Month"
)["Attendance_Percentage"].mean()

st.line_chart(monthly_attendance)

# At-Risk Students
st.subheader("At-Risk Students")

at_risk_df = df[df["Status"] == "At Risk"]

if len(at_risk_df) > 0:

    st.dataframe(
        at_risk_df[
            [
                "Student_ID",
                "Student_Name",
                "Attendance_Percentage",
                "Overall_Percentage",
                "Status"
            ]
        ],
        use_container_width=True
    )

else:
    st.success("No students are currently at risk.")

# Student Data
st.subheader("Student Data")

st.dataframe(
    df,
    use_container_width=True
)

# Download Filtered Student Data
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Student Data",
    data=csv,
    file_name="student_data.csv",
    mime="text/csv"
)