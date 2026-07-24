from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>DocCheck AI</title>
    </head>
    <body style="font-family:Arial;text-align:center;padding:50px;">
        <h1>📄 DocCheck AI</h1>
        <h2>AI Document Verification</h2>
        <p>Server is running successfully.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)