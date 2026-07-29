from flask import Flask

# Create the Flask application
app = Flask(__name__)


# Home page route
@app.route("/")
def home():
    return "Welcome to Budget-Flow!"


# Start the development server
if __name__ == "__main__":
    app.run(debug=True)
