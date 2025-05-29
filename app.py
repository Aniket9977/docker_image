from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/')
def home():
    return "home page"


if __name__ == "__main__":
    app.run(host="0.0.0.0" , port = 5000 , debug=True)