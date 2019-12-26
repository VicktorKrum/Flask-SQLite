from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'
@app.route('/home')
def hello():
    return 'Hello-World'
@app.route('/holla')
def world():
    return 'HelloWorld!'

if __name__ == '__main__':
   app.run()
