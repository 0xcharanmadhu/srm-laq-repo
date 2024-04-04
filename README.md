# SRM LAQ Generator Repo:

## Generate LAQ's on Colab:

The API key for Google GEMINI will be public only till 02/05/2024. After that you can use your own Google GEMINI API key which is for paid or else you can choose the `open source` models which will run on your local machine. You can find the related detail below.

## Generate LAQ's Locally:

Make sure you use this when google colab file goes down or Google Gemini API cost's you more. This is free and opensource.

## Prerequisites

- **Python 3.10 or higher**: Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
- **Ollama**: Follow the installation instructions for your operating system (macOS, Windows, or Linux) as provided in the Ollama README.md.
- **Models**: Choose the model you want to use from the list provided in the Ollama README.md. For example, to use the Llama 2 model, you would run `ollama run llama2` in your terminal.

## Installation

1. **Install Python Packages**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing your Python script.
   - Install the required Python packages using pip:
     ```bash
     pip install -r requirements.txt
     ```
   This command installs `pandas`, `requests`, and `pypandoc`, which are required for the script to run.

2. **Install `pandoc`**:
   - Install `pandoc` on your system. You can download it from [pandoc.org](https://pandoc.org/installing.html).
   - Ensure `pandoc` is added to your system's PATH.

3. **Configure Ollama**:
   - Follow the instructions in the Ollama README.md to install and configure the model you want to use. For example, to install the Llama 2 model, you would run `ollama run llama2`.

## Running the Script

1. **Ensure Ollama is Running**:
   - Start Ollama by running `ollama serve` in your terminal. This starts the Ollama server, which your script will communicate with to generate responses.

2. **Run the Python Script**:
   - In the terminal, navigate to the directory containing your Python script.
   - Run the script using Python:
     ```bash
     python main.py
     ```
   Replace `main.py` with the actual name of your script file.

3. **Output**:
   - The script will generate DOCX files for each question in the Excel file.
   - The files will be saved in the same directory as the script, with names based on the subject and week number.

## Troubleshooting

- If you encounter errors related to `pandoc`, ensure it's correctly installed and added to your system's PATH.
- If you have issues with the Ollama package, ensure you have the correct model installed and configured.
- For any other issues, refer to the error messages for clues and consult the documentation for the relevant packages.

## Contributing

Contributions are welcome. Please feel free to submit issues or pull requests.

## License

This tool is licensed under the MIT License. See the LICENSE file for details.
