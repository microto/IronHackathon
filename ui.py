from flask import Flask
from flask import render_template
# from security_groups_manager import IpTablesManager
app = Flask(__name__)

@app.route('/')
def hello_world():
	# post request to server to get ip blacklist
    # return 'Hello World!'
    blacklist = [{'ip' : '8.8.8.8/255.255.255.255'}]
    return render_template('ui.html', blacklist = blacklist)

if __name__ == '__main__':
    app.run()