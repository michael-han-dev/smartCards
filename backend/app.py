from dotenv import load_dotenv
import os
import cohere
from flask_cors import CORS
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from genCards import init, generate_cards
from pdfHelper import extract_text

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
init()

# COHERE_API_KEY = os.getenv("COHERE_API_KEY")
# co = cohere.Client(COHERE_API_KEY)

# Summarization
# text = """Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.
# """

# response = co.summarize(
#     text, model="summarize-xlarge", length="medium", extractiveness="high"
# )

# summary = response.summary

# print(summary)


# test
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello world!"})


# Define the API endpoint for handling PDF uploads
@app.route("/api/generate", methods=["POST"])
def upload_file():
    flashcards = []

    # check if the post request has the file part
    if "pdf" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files["pdf"]
    
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    # check if the file a PDF
    if not allowed_file(file.filename) or file.filename == "":
        return (
            jsonify(
                {
                    "error": "Invalid file type or no file selected. Only PDF files are allowed."
                }
            ),
            400,
        )
    # pass the file object to the function to extract text
    text = extract_text(file)
    generate_cards(flashcards, text)
    return jsonify({"prompt": text, "cards": flashcards}), 200


# check if a file is allowed based on its file extension
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in {"pdf"}


if __name__ == "__main__":
    app.run(debug=True)
