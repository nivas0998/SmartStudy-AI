# SmartStudy AI 📚

SmartStudy AI is a simple educational web application that analyzes student academic information and provides personalized study recommendations.

## Features

- Student performance prediction
- Attendance analysis
- Study-hour analysis
- Personalized recommendations
- Suggested daily study plan
- Performance visualization
- Interactive Streamlit interface

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Git
- GitHub

## Project Structure

```text
SmartStudy-AI/
├── app.py
├── requirements.txt
└── README.md
```

## How to Run

1. Install Python.
2. Open the project folder in VS Code.
3. Create and activate a virtual environment if required.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
streamlit run app.py
```

6. Open the local Streamlit URL shown in the terminal.

## Machine Learning

A Random Forest Regression model is used in this prototype to estimate a student's performance from study hours, attendance, and previous score.

> Note: The included dataset is a small demonstration dataset intended for an academic prototype, not for real-world prediction.
