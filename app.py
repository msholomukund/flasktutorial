from flask import Flask

app = Flask(__name__)
@app route('/')
def hello_world():
    return "W3C schools Hello World !"
if __name__ = "main" :
    app.run(debug=True)
    
