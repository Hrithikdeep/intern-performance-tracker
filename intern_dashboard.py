
import streamlit as st
import pandas as pd
import os

# Debug: show where Streamlit is running from
st.write("📁 Current directory:", os.getcwd())

# Try loading the file normally
try:
    df = pd.read_csv("intern_performance_dataset.csv")
except FileNotFoundError:
    # Try with absolute path fallback (update this path if needed)
    df = pd.read_csv("/Users/hrithik/intern_performance_dataset.csv")

st.title("📊 Intern Performance Dashboard")

st.write("### 💬 Sentiment Scores")
st.bar_chart(df["Sentiment"])

st.write("### 🔥 Burnout Cases")
st.bar_chart(df["Burnout"].value_counts())

st.write("### 🚨 Attrition Risk")
st.bar_chart(df["AttritionRisk"].value_counts())

st.write("### 📁 Full Intern Data")
st.dataframe(df)
