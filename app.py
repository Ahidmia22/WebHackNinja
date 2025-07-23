from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "✅ WebHack Toolkit Server is Running!"

if __name__ == "__main__":
    app.run()