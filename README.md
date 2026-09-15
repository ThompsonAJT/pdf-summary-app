# PDF Summary App

A Flask web application that extracts text from PDFs and generates summaries using a local AI model through Ollama.

I’m building this project to practice Python backend development, file processing, API integration, and JavaScript.

## Features

- Upload PDFs and extract their text.
- Generate summaries locally with Llama 3.2 3B.
- Copy extracted text or summaries to the clipboard.
- Display processing messages and disable submit buttons while processing.
- Handle missing files, unreadable PDFs, and model connection errors.

## Technology

- **Python and Flask:** backend and page rendering
- **pypdf:** PDF text extraction
- **Ollama and Llama 3.2 3B:** local AI summaries
- **Requests:** communication with Ollama's local API
- **HTML, CSS, and JavaScript:** interface and clipboard functionality

## How It Works

1. The user uploads a PDF and chooses extraction or summarization.
2. Flask reads the PDF using pypdf.
3. The extracted text is cleaned to remove excessive whitespace.
4. If summarization is selected, Flask sends the text to Ollama's local API.
5. The page displays the extracted text and any generated summary.

PDF text is sent to the locally running Ollama service for summarization. The application does not intentionally save uploaded PDFs to a permanent folder.

## Getting Started

The commands below are for macOS. Install Python 3.9 or newer, Git, and [Ollama](https://ollama.com/download) first.

### 1. Clone the repository

```bash
git clone https://github.com/ThompsonAJT/pdf-summary-app.git
cd pdf-summary-app
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Download the local model

Open the Ollama application, then run:

```bash
ollama pull llama3.2:3b
```

Keep Ollama running while using AI summaries. No paid API key is required.

### 5. Start Flask

```bash
python app.py
```

Open http://127.0.0.1:5001 in your browser.

This command starts a local development server with debugging enabled. It is not a production deployment configuration.

## Usage

1. Select a PDF containing selectable text.
2. Click **Extract text** or **Extract and summarize**.
3. Wait for the results.
4. Use **Copy text** or **Copy summary** to copy the desired output.

Summaries may take a few minutes depending on the document and available hardware.

## Project Files

| File | Purpose |
|---|---|
| `app.py` | Flask routes, upload handling, and error messages |
| `summarizer.py` | Requests to Ollama and summary response handling |
| `templates/index.html` | Page layout, styling, and JavaScript |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Files excluded from version control |

## Current Limitations

- Upload requests are limited to 10 MB, including form data.
- Summarization supports up to 6,000 extracted characters.
- Scanned PDFs require OCR, which is not implemented.
- Password-protected PDFs are not supported.
- Text cleanup removes paragraph and list formatting within each page.
- Complex PDF layouts may produce incorrect reading order.
- AI summaries can omit details or introduce errors; important information should be checked against the source.
- Summary length and formatting can vary.
- Clipboard access depends on browser permissions and requires localhost or HTTPS.
- Other users must install and run Ollama to use local summaries.

## Planned Improvements

- Support longer documents through chunking.
- Add summary length options.
- Improve document formatting.
- Add automated tests for upload and summarization behavior.
- Improve the interface and mobile layout.