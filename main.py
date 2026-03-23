import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This will render the file 'templates/index.html'
    return render_template('index.html')

# Optional: add a simple error handler to see the actual error (for debugging)
@app.errorhandler(500)
def internal_error(error):
    return f"500 Internal Server Error: {error}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)