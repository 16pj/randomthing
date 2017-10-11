from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello_world'

@app.route('/square/<int:input>')
def square_func(input):
    return input*input

app.run('0.0.0.0',5000)
