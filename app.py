import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="SmartStudy AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 SmartStudy AI")
st.write("A simple student performance analyzer and personalized study planner.")

# Demo training data
training_data = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "attendance": [55, 60, 65, 70, 75, 78, 82, 88, 92, 96],
    "previous_score": [45, 50, 55, 60, 65, 70, 74, 80, 86, 92],
    "score": [48, 53, 58, 63, 68, 73, 77, 83, 89, 95]
})

X = training_data[
    ["study_hours", "attendance", "previous_score"]
]

y = training_data["score"]

# Machine Learning Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Sidebar
st.sidebar.header("Enter Your Details")

study_hours = st.sidebar.slider(
    "Daily study hours",
    0.0,
    12.0,
    4.0,
    0.5
)

attendance = st.sidebar.slider(
    "Attendance (%)",
    0,
    100,
    75
)

previous_score = st.sidebar.slider(
    "Previous score (%)",
    0,
    100,
    65
)

# Analyze button
if st.sidebar.button("Analyze Performance"):

    input_data = pd.DataFrame({
        "study_hours": [study_hours],
        "attendance": [attendance],
        "previous_score": [previous_score]
    })

    # Prediction
    prediction = float(model.predict(input_data)[0])
    prediction = np.clip(prediction, 0, 100)

    # Performance Analysis
    st.subheader("📊 Performance Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Predicted Score",
            f"{prediction:.1f}%"
        )

    with col2:
        st.metric(
            "Attendance",
            f"{attendance}%"
        )

    with col3:
        st.metric(
            "Study Hours",
            f"{study_hours:.1f} hrs/day"
        )

    # Attendance recommendation
    if attendance < 75:
        attendance_advice = (
            "Try to improve attendance and avoid missing important classes."
        )
    else:
        attendance_advice = (
            "Your attendance is in a good range. Keep maintaining it."
        )

    # Study recommendation
    if study_hours < 3:
        study_advice = (
            "Consider increasing focused study time gradually."
        )
    else:
        study_advice = (
            "Your study time is reasonable. Focus on consistency and revision."
        )

    # Previous score recommendation
    if previous_score < 60:
        score_advice = (
            "Spend extra time on concepts and practice questions."
        )
    else:
        score_advice = (
            "Continue regular revision and practice to maintain your performance."
        )

    # Recommendations
    st.subheader("🎯 Personalized Recommendations")

    st.info(attendance_advice)
    st.info(study_advice)
    st.info(score_advice)

    # Study Plan
    st.subheader("📅 Suggested Daily Study Plan")

    plan = pd.DataFrame({
        "Activity": [
            "Concept Learning",
            "Problem Practice",
            "Revision",
            "Short Break"
        ],
        "Suggested Time": [
            f"{max(1, round(study_hours * 0.35, 1))} hrs",
            f"{max(0.5, round(study_hours * 0.35, 1))} hrs",
            f"{max(0.5, round(study_hours * 0.20, 1))} hrs",
            "15–30 min"
        ]
    })

    st.table(plan)

    # Visualization
    st.subheader("📈 Performance Visualization")

    chart_data = pd.DataFrame({
        "Metric": [
            "Previous Score",
            "Predicted Score",
            "Attendance"
        ],
        "Percentage": [
            previous_score,
            prediction,
            attendance
        ]
    })

    fig, ax = plt.subplots()

    ax.bar(
        chart_data["Metric"],
        chart_data["Percentage"]
    )

    ax.set_ylim(0, 100)
    ax.set_ylabel("Percentage")
    ax.set_title("Academic Performance Overview")

    st.pyplot(fig)

else:
    st.info(
        "Enter your details in the sidebar and click "
        "'Analyze Performance'."
    )

st.divider()

st.caption(
    "SmartStudy AI | Educational project prototype"
)