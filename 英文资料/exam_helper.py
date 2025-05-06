import lila_api
from bs4 import BeautifulSoup
from docx import Document
import PyPDF2

# 设置 Lila API 密钥
lila_api.api_key = "sk-ba8cc844b61d435bb2e7cce12bcd40b6"

def generate_answer_and_explanation(question):
    prompt = f"请为以下专四词汇与语法题生成答案和解析：{question}"
    response = lila_api.ChatCompletion.create(
        model="实际的 Lila 模型名",
        messages=[
            {"role": "system", "content": "你是一个专四词汇与语法题的讲题老师，需要为题目生成答案和解析，并总结归纳知识点。"},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

def process_word_file(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    text = '\n'.join(full_text)
    result = generate_answer_and_explanation(text)
    print(result)

def process_pdf_file(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    result = generate_answer_and_explanation(text)
    print(result)

def process_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    questions = soup.find_all('div', class_='question')
    for question in questions:
        question_text = question.get_text()
        result = generate_answer_and_explanation(question_text)
        # 这里可以将结果插入到 HTML 文件中
        print(result)

if __name__ == "__main__":
    file_path = "TEM4_Vocabulary.html"
    process_html_file(file_path)