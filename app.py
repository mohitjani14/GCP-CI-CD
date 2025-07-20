from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>🌟 GCP CI/CD Demo</title>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #f06, #4a90e2);
                color: white;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                text-align: center;
            }
            h1 {
                font-size: 4em;
                margin-bottom: 0.2em;
                text-shadow: 2px 2px 5px #000;
            }
            p {
                font-size: 1.5em;
                margin: 0.5em 0;
                color: #f0f0f0;
            }
            .tag {
                background: rgba(0, 0, 0, 0.2);
                padding: 0.5em 1em;
                border-radius: 20px;
                margin-top: 20px;
                display: inline-block;
                font-size: 1em;
            }
        </style>
    </head>
    <body>
        <h1>🚀 Welcome to GCP CI/CD Demo</h1>
        <p>Powered by <strong>Mohit Jani</strong></p>
        <p class="tag">Colorful, Simple, & One Page</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
