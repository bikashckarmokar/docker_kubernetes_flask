from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h2> Hi There </h2>'


if __name__=='__main__':
    app.run()