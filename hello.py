from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/next')
def next_function():
    return 'Testing!'

app.debug = True #setting debug mode to true
if __name__ == '__main__':
    app.run()