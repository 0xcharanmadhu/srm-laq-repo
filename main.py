import textwrap
import pandas as pd
import requests
import ollama
import markdown
from docx import Document
from htmldocx import HtmlToDocx

# Edit your details here!
# Subject number details: for Sem-2
# 1 Entrepreneurship
# 2 HRManagement
# 3 FinanceManagement
# 4 BusinessStats
# 5 Ethics
# 6 Legal
subject_number = 3
your_name = "Charan M"
your_regno = "EA2352001010051"

def to_markdown(text):
    text = text.replace('•', ' *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

def md2html(md):
    # Convert Markdown to HTML using Python-Markdown
    return markdown.markdown(md)



file_url = f"https://raw.githubusercontent.com/0xcharanmadhu/srm-laq-repo/main/{subject_number}.xlsx"

urlresponse = requests.get(file_url)

df = pd.read_excel(urlresponse.content)

for subject_index, subject_name in enumerate(df.columns):
    for question_index, question_prompt in enumerate(df[subject_name]):
        if not question_prompt or question_prompt == "":
            continue
        input_size = " explain with as many words as you can. This topic is related to {} subject in MBA. Your response should only be in markdown format. Minimum word count should be 1000 words (do not mention this in response)".format(subject_name)
        if isinstance(question_prompt, float):
            question_prompt = str(question_prompt)
            print(question_prompt)

        response = ollama.generate(
            model="wizardlm2",  # make sure model is installed and ollama is serving!
            prompt=f"{question_prompt}{input_size}"
        )
        response_text = response['response']

        if response_text:
            document = Document()
            new_parser = HtmlToDocx()
            markdown_text = f"# {question_prompt}\n \n\nName:**{your_name}**\n \nRegister No:**{your_regno}**\n \n{response_text}"
            html_content = md2html(markdown_text)
            new_parser.add_html_to_document(html_content, document)
            output_file = f"{subject_name}-Week-{question_index + 1}.docx"
            document.save(output_file)
            print(html_content)
        else:
            print(f"Skipping Week {question_index + 1} in {subject_name} due to empty response.")
