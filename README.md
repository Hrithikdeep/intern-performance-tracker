# Intern Performance Tracker 📊

A real-world HR analytics project built with **Python**, **Streamlit**, and the **IBM HR Analytics Dataset**. This tool tracks intern performance, analyzes emotional feedback, detects burnout risk, and predicts potential attrition.

---

## 🔍 Project Overview

This project simulates a system that HR teams can use to monitor and support interns in real time. By combining structured HR data with feedback sentiment, the dashboard delivers key insights like:

* Intern sentiment trends
* Burnout detection
* Attrition risk scoring
* Interactive performance visualization

---

## 📄 Dataset

* **Source**: [IBM HR Analytics Employee Attrition & Performance Dataset (Kaggle)](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
* **Modified to simulate intern data** by filtering:

  * `Age <= 25` or `YearsAtCompany <= 1`
  * Added synthetic `Feedback` column for sentiment analysis

---

## 🧠 Features

* **Sentiment Analysis** using TextBlob
* **Burnout Score** based on negative sentiment + overtime
* **Attrition Risk** prediction using rule-based logic
* **Streamlit Dashboard** with visual reports

---

## 📅 How to Run

### 1. Clone this repo or download the files

### 2. Install dependencies

```bash
pip install pandas streamlit textblob
python -m textblob.download_corpora
```

### 3. Run the app

```bash
streamlit run intern_dashboard.py
```

Dashboard opens at: `http://localhost:8501`

---

## 🔍 Project Files

* `intern_dashboard.py`  → Streamlit dashboard app
* `intern_performance_dataset.csv` → Cleaned + feedback-added dataset
* `intern_tracker_eda.ipynb` → Jupyter notebook with logic + model
* `intern_dashboard.pdf` → Sample output of the working app

---

## 🚀 Future Improvements

* Use real feedback from employee review datasets
* Train ML models for burnout and attrition prediction
* Connect to live HR databases or Slack/Email input
* Deploy online via Streamlit Cloud or Azure

---

## 🌟 Author

**Hrithik \\**
Aspiring Data Scientist | Building real-world portfolio projects | Focused on solving practical problems with AI

