import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from fpdf import FPDF

# Set Streamlit page configuration
st.set_page_config(page_title="Student Score Analysis and Prediction Tool", layout='wide')

# Custom CSS for background color and font style
st.markdown(
    """
    <style>
    .reportview-container, .main, .block-container {
        background-color: #DAF0F7;
    }
    .stSidebar .sidebar-content, .stSidebar .sidebar-content .stHeader {
        color: #ffffff; /* Change sidebar content and header color to white */
    }
    .stMarkdown, .stSelectbox, .stTextInput, .stNumberInput, .stSlider .horizontal {
        font-family: 'Helvetica', sans-serif;
        color: #3B3B3B;
    }
    .stButton>button {
        font-family: 'Helvetica', sans-serif;
        color: #ffffff;
        background-color: #3B3B3B;
        border-color: #3B3B3B;
    }
    .stButton>button:hover {
        background-color: #757575;
        border-color: #757575;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        font-family: serif;
        color: black; /* Added to ensure titles are black */
    }
    .stTitle {
        color: black; /* Added to ensure titles are black */
    }
    .card {
        background-color: #FFE5B4;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define subject weightages and their splits
subject_weightages = {
    "BD": {"M1": 15, "M2": 15, "EndSem": 30, "Others": 40},
    "HPC": {"M1": 10, "M2": 10, "EndSem": 40, "Others": 40},
    "SE": {"M1": 10, "M2": 10, "EndSem": 30, "Others": 50},
    "CN": {"M1": 15, "M2": 15, "EndSem": 30, "Others": 40},
    "CB": {"M1": 10, "M2": 30, "EndSem": 40, "Others": 20}
}

# Define total marks for each component
total_marks = {
    "BD": {"M1": 30, "M2": 30, "EndSem": 100, "Others": 40},
    "HPC": {"M1": 0, "M2": 100, "EndSem": 100, "Others": 40},
    "SE": {"M1": 30, "M2": 30, "EndSem": 100, "Others": 50},
    "CN": {"M1": 40, "M2": 50, "EndSem": 100, "Others": 40},
    "CB": {"M1": 10, "M2": 30, "EndSem": 100, "Others": 20}
}

# Adjusted credits for each course
course_credits = {"BD": 3, "HPC": 3, "SE": 3, "CN": 4, "CB": 3}

# Function to calculate required marks
def calculate_required_marks(target_sgpa, total_marks, subject_weightages):
    required_marks = {}
    total_credits = sum(course_credits.values())
    for subject, components in subject_weightages.items():
        required_marks[subject] = {}
        subject_credit = course_credits[subject]

        for component, weightage in components.items():
            max_marks_for_component = total_marks[subject][component]
            required_marks[subject][component] = min(
                (target_sgpa * total_credits * max_marks_for_component * weightage) / (10 * subject_credit * 100),
                max_marks_for_component
            )

    return required_marks

# Function to adjust marks based on completed exams and obtained marks
def adjust_marks(target_sgpa, current_marks, required_marks, completed_exams):
    adjusted_marks = {subject: components.copy() for subject, components in required_marks.items()}
    
    for subject, components in current_marks.items():
        for component, marks in components.items():
            if component in completed_exams[subject]:
                adjusted_marks[subject][component] = marks
    
    for subject, components in adjusted_marks.items():
        total_weight = sum(subject_weightages[subject].values())
        remaining_weight = total_weight - sum(
            weight for comp, weight in subject_weightages[subject].items() if comp in completed_exams[subject]
        )
        if remaining_weight > 0:
            remaining_diff = sum(
                (required_marks[subject][comp] - current_marks[subject][comp]) 
                for comp in subject_weightages[subject] if comp in completed_exams[subject]
            )
            for comp in subject_weightages[subject]:
                if comp not in completed_exams[subject]:
                    adjusted_marks[subject][comp] = required_marks[subject][comp] + remaining_diff * (subject_weightages[subject][comp] / remaining_weight)
                    adjusted_marks[subject][comp] = min(adjusted_marks[subject][comp], total_marks[subject][comp])

    return adjusted_marks

# Function to check if it's feasible to achieve the target SGPA
def is_feasible(target_sgpa, current_marks, adjusted_marks):
    for subject, components in current_marks.items():
        for component, marks in components.items():
            if component in adjusted_marks[subject] and marks > adjusted_marks[subject][component]:
                return False
    return True

# Function to generate PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Gradesheet', 0, 1, 'C')
    
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
    
    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def generate_pdf(current_marks, adjusted_marks, target_sgpa):
    pdf = PDF()
    pdf.add_page()

    pdf.chapter_title("Target SGPA: {:.2f}".format(target_sgpa))
    pdf.chapter_title("Current Marks and Required Marks")
    
    for subject, components in current_marks.items():
        pdf.chapter_title(f"\n{subject}")
        for component, marks in components.items():
            required = adjusted_marks[subject][component]
            pdf.chapter_body(f"{component} marks: {marks} | Required: {required:.2f}")
    
    return pdf.output(dest='S').encode('latin1')

# Initialize Streamlit app
st.title("🎓 Welcome to the Student Score Analysis and Prediction Tool")
st.write("This tool helps you analyze your current marks and predict the required marks to achieve your target SGPA.")

# Input marks achieved so far
current_marks = {}
st.sidebar.header("Enter Your Marks")
for subject in subject_weightages.keys():
    with st.sidebar.expander(f"Marks for {subject}"):
        current_marks[subject] = {}
        for component in subject_weightages[subject].keys():
            current_marks[subject][component] = st.number_input(f"{subject} - {component} Marks", min_value=0, max_value=total_marks[subject][component], step=1)

# Input completed exams
completed_exams = {}
st.sidebar.header("Completed Exams")
for subject in subject_weightages.keys():
    with st.sidebar.expander(f"Completed Exams for {subject}"):
        completed_exams[subject] = st.multiselect(f"Select completed exams for {subject}", list(subject_weightages[subject].keys()))

# Input target SGPA
target_sgpa = st.sidebar.slider("🎯 Select Your Target SGPA", min_value=0.0, max_value=10.0, step=0.1)

# Calculate required marks and adjust them
required_marks = calculate_required_marks(target_sgpa, total_marks, subject_weightages)
adjusted_marks = adjust_marks(target_sgpa, current_marks, required_marks, completed_exams)

# Display calculated marks and feasibility
st.header("Required Marks to Achieve Target SGPA")
st.write("These are the marks you need to score in the remaining exams to achieve your target SGPA.")

feasibility = is_feasible(target_sgpa, current_marks, adjusted_marks)

for subject, components in adjusted_marks.items():
    st.subheader(subject)
    for component, marks in components.items():
        st.write(f"{component}: {marks:.2f} marks required")

# Display feasibility
if feasibility:
    st.success("🎉 It is feasible to achieve your target SGPA!")
else:
    st.error("⚠ It might not be feasible to achieve your target SGPA with the current marks.")

# Visualization options
st.header("Visualize Your Marks")
visualization_type = st.selectbox("Select Visualization Type", ["Histogram", "Heatmap", "Line Graph", "Scatter Plot", "Pie Chart"])

# Create DataFrame from current and required marks
data = []
for subject, components in current_marks.items():
    for component, marks in components.items():
        data.append([subject, component, marks, adjusted_marks[subject][component]])
df = pd.DataFrame(data, columns=["Subject", "Component", "Current Marks", "Required Marks"])

# Visualizations
if visualization_type == "Histogram":
    st.subheader("Histogram")
    for subject in subject_weightages.keys():
        st.write(f"Histogram for {subject}")
        plt.figure(figsize=(10, 4))
        plt.hist(df[df['Subject'] == subject]['Current Marks'], bins=5, alpha=0.7, label='Current Marks')
        plt.hist(df[df['Subject'] == subject]['Required Marks'], bins=5, alpha=0.7, label='Required Marks')
        plt.legend(loc='upper right')
        plt.title(f"{subject} - Current and Required Marks")
        plt.xlabel("Marks")
        plt.ylabel("Frequency")
        st.pyplot(plt)

elif visualization_type == "Heatmap":
    st.subheader("Heatmap")
    plt.figure(figsize=(10, 6))
    heatmap_data = df.pivot(index="Subject", columns="Component", values="Current Marks")
    sns.heatmap(heatmap_data, annot=True, fmt="g", cmap='viridis')
    st.pyplot(plt)


elif visualization_type == "Line Graph":
    st.subheader("Line Graph")
    for subject in subject_weightages.keys():
        st.write(f"Line Graph for {subject}")
        plt.figure(figsize=(10, 4))
        plt.plot(df[df['Subject'] == subject]['Component'], df[df['Subject'] == subject]['Current Marks'], marker='o', label='Current Marks')
        plt.plot(df[df['Subject'] == subject]['Component'], df[df['Subject'] == subject]['Required Marks'], marker='o', label='Required Marks')
        plt.legend(loc='upper left')
        plt.title(f"{subject} - Current and Required Marks")
        plt.xlabel("Component")
        plt.ylabel("Marks")
        st.pyplot(plt)

elif visualization_type == "Scatter Plot":
    st.subheader("Scatter Plot")
    for subject in subject_weightages.keys():
        st.write(f"Scatter Plot for {subject}")
        plt.figure(figsize=(10, 4))
        plt.scatter(df[df['Subject'] == subject]['Component'], df[df['Subject'] == subject]['Current Marks'], label='Current Marks')
        plt.scatter(df[df['Subject'] == subject]['Component'], df[df['Subject'] == subject]['Required Marks'], label='Required Marks')
        plt.legend(loc='upper left')
        plt.title(f"{subject} - Current and Required Marks")
        plt.xlabel("Component")
        plt.ylabel("Marks")
        st.pyplot(plt)

elif visualization_type == "Pie Chart":
    st.subheader("Pie Chart")
    for subject in subject_weightages.keys():
        st.write(f"Pie Chart for {subject}")
        plt.figure(figsize=(10, 4))
        plt.pie(df[df['Subject'] == subject]['Current Marks'], labels=df[df['Subject'] == subject]['Component'], autopct='%1.1f%%', startangle=140)
        plt.title(f"{subject} - Current Marks Distribution")
        st.pyplot(plt)

# Overall analysis
st.header("📊 Overall Analysis")
st.write("This section provides an overall analysis of your current marks and required marks to achieve your target SGPA.")

# Subject-wise score breakdown
st.header("📝 Subject-wise Score Breakdown")
for subject in subject_weightages.keys():
    st.subheader(subject)
    st.write(df[df['Subject'] == subject])

# Upcoming schedules
st.header("📅 Upcoming Schedules")
upcoming_schedules = {
    "BD": "M2 Exam on 15th August",
    "HPC": "EndSem Exam on 25th August",
    "SE": "M2 Exam on 20th August",
    "CN": "EndSem Exam on 30th August",
    "CB": "M1 Exam on 10th August"
}
for subject, schedule in upcoming_schedules.items():
    st.write(f"{subject}: {schedule}")

# Chatbot for faculty comments
st.header("🗣 Chatbot for Faculty Comments")
faculty_comments = {
    "BD": "Keep up the good work! Aim for consistency.",
    "HPC": "Focus on practical implementations.",
    "SE": "Understand the concepts thoroughly.",
    "CN": "Practice previous years' question papers.",
    "CB": "Revise the topics regularly."
}
selected_subject = st.selectbox("Select Subject for Faculty Comments", list(faculty_comments.keys()))
if st.button("Get Faculty Comments"):
    st.write(f"Faculty Comments for {selected_subject}: {faculty_comments[selected_subject]}")

# Emotion button for component-wise marks
st.header("😊 How do you feel about your component-wise marks?")
for subject, components in current_marks.items():
    st.subheader(subject)
    for component, marks in components.items():
        emotion = st.radio(f"Your feeling about {component} marks in {subject}", ('Happy', 'Neutral', 'Unhappy'), key=f"{subject}_{component}")

# Motivational quotes
st.header("💪 Motivational Quotes")
quotes = [
    "Believe in yourself and all that you are.",
    "The only way to achieve the impossible is to believe it is possible.",
    "Success is not the key to happiness. Happiness is the key to success.",
    "Keep going. Everything you need will come to you at the perfect time.",
    "Believe you can and you're halfway there."
]
st.write(random.choice(quotes))

# Download gradesheet as PDF
st.header("📥 Download Your Gradesheet")
if st.button("Download PDF"):
    pdf_bytes = generate_pdf(current_marks, adjusted_marks, target_sgpa)
    st.download_button(label="Download Gradesheet PDF", data=pdf_bytes, file_name="gradesheet.pdf", mime='application/pdf')