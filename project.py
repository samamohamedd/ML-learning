import PyPDF2
import openai

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

# Function to summarize the extracted text using GPT
def summarize_text(text):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that summarizes text."},
        {"role": "user", "content": f"Summarize this text: {text}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

# Example usage
pdf_path = "a.pdf"  # Replace with your PDF file path
pdf_text = extract_text_from_pdf(pdf_path)
summary = summarize_text(pdf_text)

print("Summary of PDF:")
print(summary)

def func(x, lst=[]):
    lst.append(x)
    return lst

print(func(1))  # [1]
print(func(2))  # [2]
