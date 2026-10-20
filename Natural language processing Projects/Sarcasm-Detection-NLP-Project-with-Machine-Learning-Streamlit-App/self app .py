import streamlit as st
import pickle
import PyPDF2
import docx  # For reading .docx files
from io import BytesIO
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from contractions import fix  # To handle contractions like don't -> do not

# Load the trained model and TF-IDF vectorizer
model = pickle.load(open("model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

nltk.download('punkt')
nltk.download('punkt_tab')  # This might be necessary if punkt_tab is specifically required
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize stopwords and lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text_advanced(text):
    # Expand contractions
    text = fix(text)

    # Remove URLs
    text = re.sub(r'http\S+', '', text)

    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords and lemmatize
    cleaned_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]

    # Join tokens back to a single string
    cleaned_text = ' '.join(cleaned_tokens)

    # Remove excessive whitespaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    return cleaned_text

# Function to predict sarcasm
def detect_sarcasm(new_headline):
    cleaned_headline = clean_text_advanced(new_headline)
    transformed_headline = tfidf.transform([cleaned_headline])
    prediction = model.predict(transformed_headline)

    if prediction == 1:
        return "Sarcastic"
    else:
        return "Not Sarcastic"


def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


# Function to extract text from DOCX
def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text


# Function to extract text from TXT with explicit encoding handling
def extract_text_from_txt(file):
    # Try using utf-8 encoding for reading the text file
    try:
        text = file.read().decode('utf-8')
    except UnicodeDecodeError:
        # In case utf-8 fails, try 'latin-1' encoding as a fallback
        text = file.read().decode('latin-1')
    return text




def handle_file_upload(uploaded_file):
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension == 'pdf':
        text = extract_text_from_pdf(uploaded_file)
    elif file_extension == 'docx':
        text = extract_text_from_docx(uploaded_file)
    elif file_extension == 'txt':
        text = extract_text_from_txt(uploaded_file)
    else:
        raise ValueError("Unsupported file type. Please upload a PDF, DOCX, or TXT file.")
    return text

st.sidebar.header("About the Sarcasm Detection App ")
st.sidebar.info("""
**Sarcasm Detection App** allows you to detect sarcasm in text through three methods:
1. Upload a PDF, TXT, or DOCX document, and the app will extract the text and analyze it to check for sarcasm.
2. Enter text directly into the search bar, and the app will detect whether it contains sarcasm.

**Output:** The app provides an easy-to-read prediction of whether the text is 'Sarcastic' or 'Not Sarcastic'. 
Whether you're analyzing customer reviews, social media comments, or any other text, this app simplifies sarcasm detection.
""")

# Streamlit app interface
st.title("Sarcasm Detection App")
st.markdown("This app detects **sarcasm** in text using advanced **machine learning models**. "
            "You can upload **PDF, TXT, DOCX** files or input text directly. Let's see if the text has a sarcastic tone!")
# Footer at the bottom of the sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("**Created by Khan**")


uploaded_file = st.file_uploader("Upload a PDF, TXT, or DOCX file", type=["pdf", "txt", "docx"])

search_query = st.text_input("Or, directly input the text to check for sarcasm:")



if uploaded_file is not None:
        # Extract text from the uploaded file
    try:
        resume_text = handle_file_upload(uploaded_file)
        st.write("Successfully extracted the text from the uploaded resume.")

        # Display extracted text (optional)
        if st.checkbox("Show extracted text", False):
            st.text_area("Extracted Resume Text", resume_text, height=300)

        # Make prediction
        st.subheader("Predicted Category")
        category = detect_sarcasm(resume_text)
        st.success(f"The predicted category of the uploaded resume is: **{category}**")

    except Exception as e:
        st.error(f"Error processing the file: {str(e)}")
        
elif search_query:
    result=detect_sarcasm(search_query)
    st.success(f"Prediction (from input text): {result}")
else:
    pass