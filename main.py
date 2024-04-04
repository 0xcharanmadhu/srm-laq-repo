import textwrap
import pandas as pd
import requests
import ollama
from pypandoc import convert_text

#Edit your details here! 
# Subject number details: for Sem-2
# 1 Entrepreneurship
# 2 HRManagement
# 3 FinanceManagement
# 4 BusinessStats
# 5 Ethics
# 6 Legal
subject_number = 1
your_name="Charan"
your_regno="100"

def to_markdown(text):
    text = text.replace('•', ' *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

def md2html(md):
    # Convert Markdown to HTML using pypandoc
    return convert_text(md, 'html', format='md')

def html2docx(html_content, output_file):
    # Convert HTML to DOCX using pypandoc
    convert_text(html_content, 'docx', outputfile=output_file, format='html')

file_url = f"https://raw.githubusercontent.com/0xcharanmadhu/srm-laq-repo/main/{subject_number}.xlsx"

urlresponse = requests.get(file_url)

df = pd.read_excel(urlresponse.content)

for subject_index, subject_name in enumerate(df.columns):
    for question_index, question_prompt in enumerate(df[subject_name]):
        if not question_prompt or question_prompt == "":
            continue
        input_size = f" explain with as many words as you can. This topic is related to {subject_name} subject in MBA. Your response should only be in markdown format. Minimum word count should be 1000 words (do not mention this in response)"
        if isinstance(question_prompt, float):
            question_prompt = str(question_prompt)
        
        response = ollama.generate(
            model="llama2", # make sure models are installed and ollama is serving!
            prompt= f"{question_prompt+input_size}"
        )

        response_text = response['response']
        
        
        if response_text:
            markdown_text = f"# {question_prompt}\n \n\nName:**{your_name}**\n \nRegister No:**{your_regno}**\n \n{response_text}"

            # Convert Markdown to HTML
            html_content = md2html(markdown_text)

            # Define the output file name
            output_file = f"{subject_name}-Week-{question_index + 1}.docx"

            # Convert HTML to DOCX
            html2docx(html_content, output_file)

            print(f"Created DOCX file: {output_file}")
        else:
            print(f"Skipping Week {question_index + 1} in {subject_name} due to empty response.")
