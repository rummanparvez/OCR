import streamlit as st
from transformers import AutoTokenizer, Qwen2VLModel
from PIL import Image
import torch
from io import BytesIO
from docx import Document
from fpdf import FPDF
import os

# Load the Qwen2-VL-7B-Instruct model and tokenizer
@st.cache_resource(show_spinner=False)
def load_model():
    token = os.getenv("HUGGINGFACE_TOKEN")  # Get Hugging Face token from environment variable
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-VL-7B-Instruct", use_auth_token=token)
    model = Qwen2VLModel.from_pretrained("Qwen/Qwen2-VL-7B-Instruct", use_auth_token=token)
    return tokenizer, model

tokenizer, model = load_model()

# Function to perform OCR using Qwen2-VL-7B-Instruct
def perform_ocr(image):
    # Convert the image to a tensor suitable for the model
    inputs = tokenizer(images=image, return_tensors="pt")
    with torch.no_grad():  # Disable gradient tracking for inference
        outputs = model(**inputs)
    extracted_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return extracted_text

# Function to search for a keyword in the extracted text
def search_keyword(extracted_text, keyword):
    if keyword.lower() in extracted_text.lower():
        return f"'{keyword}' found in the text."
    else:
        return f"'{keyword}' not found."

# Function to save extracted text as PDF
def save_text_as_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    
    # Add text to PDF
    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)
    
    # Save the PDF to a BytesIO object
    pdf_bytes = BytesIO()
    pdf.output(pdf_bytes)
    pdf_bytes.seek(0)
    return pdf_bytes

# Function to save extracted text as Word
def save_text_as_word(text):
    doc = Document()
    doc.add_paragraph(text)
    
    # Save the Word file to a BytesIO object
    word_bytes = BytesIO()
    doc.save(word_bytes)
    word_bytes.seek(0)
    return word_bytes

# Streamlit web application
def main():
    st.title("OCR Application with Qwen2-VL-7B-Instruct and Search Functionality")

    # Upload an image
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_image:
        # Display the uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Convert the image for OCR
        image = image.convert("RGB")

        # Extract text from the image using the OCR model
        with st.spinner('Extracting text...'):
            extracted_text = perform_ocr(image)
        
        # Display the extracted text
        st.subheader("Extracted Text:")
        st.write(extracted_text)

        # Allow the user to download the extracted text
        st.subheader("Download Extracted Text:")
        col1, col2 = st.columns(2)
        with col1:
            pdf_bytes = save_text_as_pdf(extracted_text)
            st.download_button("Download as PDF", pdf_bytes, file_name="extracted_text.pdf", mime="application/pdf")
        with col2:
            word_bytes = save_text_as_word(extracted_text)
            st.download_button("Download as Word", word_bytes, file_name="extracted_text.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

        # Allow the user to enter a keyword to search within the extracted text
        keyword = st.text_input("Enter a keyword to search:")
        if keyword:
            search_result = search_keyword(extracted_text, keyword)
            st.write(search_result)

if __name__ == "__main__":
    main()
