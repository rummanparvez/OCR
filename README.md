
# OCR Web Application

## Overview
This project is a web application that utilizes Optical Character Recognition (OCR) to extract text from images containing both Hindi and English text. The application is built using Streamlit and employs the Qwen2-VL model for text extraction, providing a simple interface for users to upload images and search for specific keywords within the extracted text.

## Deliverables

### 1. Code Submission
The project includes the following Python scripts:
- `app.py`: The main script for the web application, which handles image uploads, performs OCR, and allows users to search for keywords in the extracted text.
- `requirements.txt`: A file listing all the required Python packages for the project.

### 2. Live Web Application
The live URL of the deployed web application will be provided once the application is deployed on Streamlit Community Cloud. Users can test the OCR and search functionalities through this link.

### 3. Extracted Text and Search Output
The application outputs the extracted text from the uploaded image in JSON or plain text format. Demonstrations of the search functionality with example keywords are included.

## Technologies Used
- **Streamlit**: An open-source app framework for Machine Learning and Data Science projects. Streamlit allows for the quick creation of web applications with minimal effort.
- **Transformers**: A library by Hugging Face that provides pre-trained models and tools for Natural Language Processing (NLP). In this project, the Qwen2-VL model is utilized for OCR.
- **Pillow**: A Python Imaging Library (PIL) fork that provides image processing capabilities. It is used for handling image uploads and conversions.
- **FPDF**: A library to generate PDF files in Python. It is used to allow users to download the extracted text in PDF format.
- **python-docx**: A library for creating and updating Microsoft Word (.docx) files. This is used to save the extracted text in a Word document format.

## How to Set Up the Environment
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/rummanparvez/OCR.git
   cd OCR
   ```

2. Create a virtual environment (optional but recommended).
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages.
   ```bash
   pip install -r requirements.txt
   ```

4. Run the web application locally.
   ```bash
   streamlit run app.py
   ```

## Deployment Process
Once the application is ready and tested locally, deploy it to the Streamlit Community Cloud by connecting your GitHub repository. Follow the deployment instructions provided by Streamlit for a seamless setup.

