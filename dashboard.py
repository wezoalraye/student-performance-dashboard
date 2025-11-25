import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("student_data_with_performance.csv")

# Create Performance_Category column if missing
if "Performance_Category" not in df.columns:
    df["Performance_Category"] = df["GPA"].apply(
        lambda x: "High" if x >= 3 else ("Medium" if x >= 2 else "Low")
    )

st.title("📊 Student Performance Dashboard")

st.write("This dashboard provides insights into GPA, attendance, major, and performance categories of students.")

# Show dataframe
st.subheader("Student Dataset")
st.dataframe(df)

# Bar Chart — GPA by Major
st.subheader("Average GPA by Major")

gpa_by_major = df.groupby("Major")["GPA"].mean()

fig1, ax1 = plt.subplots()
gpa_by_major.plot(kind="bar")
plt.ylabel("Average GPA")
st.pyplot(fig1)

# Pie Chart — Performance Category Distribution
st.subheader("Performance Category Distribution")

perf_counts = df["Performance_Category"].value_counts()

fig2, ax2 = plt.subplots()
ax2.pie(perf_counts, labels=perf_counts.index, autopct='%1.1f%%')
plt.title("Performance Categories")
st.pyplot(fig2)

# Scatter Plot — Attendance vs GPA
st.subheader("AttendanceRate vs GPA")

fig3, ax3 = plt.subplots()
ax3.scatter(df["AttendanceRate"], df["GPA"])
plt.xlabel("AttendanceRate")
plt.ylabel("GPA")
st.pyplot(fig3)
