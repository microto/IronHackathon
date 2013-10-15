from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/<name>')
def hello_world(name=None):
    # return 'Hello World!'
    return render_template('ui.html', name=name)

if __name__ == '__main__':
    app.run()