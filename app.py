#1. Import Flask
from flask import Flask
# 2.Create an app, being sure to pass__name__
app = Flask(__name__)
# 3. DEfine what to do when a user goes to index route
@app.route('/')
def hello_world():
    return 'Hello World'


