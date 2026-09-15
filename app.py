from flask import Flask, render_template, request
from pypdf import PdfReader
from pypdf.errors import PyPdfError

app = Flask(__name__)

# Limit uploads to 10 MB.
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024


@app.route("/", methods=["GET", "POST"])
def home():
    text = ""
    error = ""

    if request.method == "POST":
        pdf = request.files.get("pdf")

        if not pdf or not pdf.filename:
            error = "Please choose a PDF."
        elif not pdf.filename.lower().endswith(".pdf"):
            error = "Please upload a PDF file."
        else:
            try:
                reader = PdfReader(pdf.stream)

                if reader.is_encrypted:
                    error = "Please upload a PDF without password protection."
                else:
                    text = "\n\n".join(
                        " ".join((page.extract_text() or "").split())
                        for page in reader.pages
                    )

                    if not text.strip():
                        error = (
                            "No text was found. This PDF may contain scanned "
                            "images, which need optical character recognition (OCR)."
                        )

            except (PyPdfError, ValueError, OSError):
                error = "This PDF could not be read. Try another file."

    return render_template("index.html", text=text, error=error)


@app.errorhandler(413)
def upload_too_large(error):
    return render_template(
        "index.html",
        text="",
        error="The upload is too large. Please choose a PDF under 10 MB."
    ), 413


if __name__ == "__main__":
    app.run(port=5001, debug=True)