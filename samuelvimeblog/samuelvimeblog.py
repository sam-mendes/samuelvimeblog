from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/blah')
def wtf():
    return 'Finally my first deploy!!!!!'

if __name__ == '__main__':
    app.run()
