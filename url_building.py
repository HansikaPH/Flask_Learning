from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass

#test_request_context method tells Flask to behave as though it is handling a request,
with app.test_request_context(): #ensures that the resource is "cleaned up" when the code that uses it finishes running, even if exceptions are thrown.
  print url_for('index')
  print url_for('login')
  print url_for('login', next='/')
  print url_for('profile', username='John Doe')