from flask import *

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    return render_template('index.html', name=name)

@app.route('/blah')
def wtf():
    render_template('')
    return 'Finally my first deploy!!!!!'

if __name__ == '__main__':
    app.run()
