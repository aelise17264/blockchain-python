from flask import Flask

app = Flask(__name__)

# endpoints

@app.route('/')
def default():
    return 'Welcome to the Blockchain'

app.run()