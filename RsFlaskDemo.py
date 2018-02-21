from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template()


if __name__ == '__main__':
    app.run()
