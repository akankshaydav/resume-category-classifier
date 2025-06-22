import streamlit as st
import pickle
import docx
import PyPDF2
import re

# Load models
model = pickle.load(open('clf.pkl', 'rb'))
vectorizer = pickle.load(open('tfidf.pkl', 'rb'))
label_encoder = pickle.load(open('encoder.pkl', 'rb'))

# Preprocessing
def preprocess_resume(text):
    text = re.sub(r"http\S+|www\S+|https\S+", ' ', text)
    text = re.sub(r"\@\w+|\#", ' ', text)
    text = re.sub(r"[^\w\s]", ' ', text)
    text = re.sub(r"\s+", ' ', text)
    return text.strip()

# File readers
def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    return ' '.join([page.extract_text() for page in reader.pages])

def read_docx(file):
    doc = docx.Document(file)
    return '\n'.join([para.text for para in doc.paragraphs])

def read_txt(file):
    try:
        return file.read().decode("utf-8")
    except:
        return file.read().decode("latin-1")

def extract_resume_text(file):
    ext = file.name.split('.')[-1].lower()
    if ext == 'pdf':
        return read_pdf(file)
    elif ext == 'docx':
        return read_docx(file)
    elif ext == 'txt':
        return read_txt(file)
    else:
        return None

# Prediction logic
def predict_category(text):
    cleaned = preprocess_resume(text)
    vector = vectorizer.transform([cleaned]).toarray()
    prediction = model.predict(vector)
    return label_encoder.inverse_transform(prediction)[0]

# Streamlit App
st.set_page_config("Smart Resume Classifier", layout="wide")
st.title("📄 Smart Resume Category Classifier")

st.sidebar.markdown("## 📌 Upload Instructions")
st.sidebar.info("Accepted formats: PDF, DOCX, TXT\n\nMax size: 200 MB")

uploaded_file = st.file_uploader("📤 Upload your Resume", type=['pdf', 'docx', 'txt'])

if uploaded_file:
    try:
        text = extract_resume_text(uploaded_file)
        st.success("Resume text successfully extracted ✅")
        
        with st.expander("🔍 Preview Extracted Text"):
            st.text_area("", text, height=300)

        st.markdown("---")
        st.markdown("### 🔮 Prediction")
        category = predict_category(text)
        st.success(f"✅ This resume is most suitable for: **{category}**")

    except Exception as e:
        st.error(f"Something went wrong while processing the file.\n\n{e}")
