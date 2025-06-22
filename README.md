# 📄 Resume Category Classifier

A simple web application built using **Python**, **Streamlit**, and **Machine Learning** that predicts the most suitable job category for a resume. Just upload a resume file (PDF, DOCX, or TXT), and the app will classify it into a predefined category using a pre-trained ML model.

---

## ✨ Features

- Upload resumes in PDF, DOCX, or TXT format
- Extract text using file parsers
- Clean and preprocess resume text
- Predict job category using a trained machine learning model
- Simple and responsive UI with Streamlit

---

## ⚙️ How It Works

1. Upload your resume.
2. The app extracts and cleans the text.
3. It vectorizes the text using a TF-IDF model.
4. A Support Vector Classifier (SVC) model predicts the job category.
5. You see the predicted job role on screen.

---

## 🛠 Built With

- Python
- Streamlit
- scikit-learn (TF-IDF vectorizer + SVM)
- PyPDF2
- python-docx

---

## 🚀 Getting Started

### ✅ Prerequisites

Install required packages:

```bash
pip install -r requirements.txt
