from flask import Flask
import flask
from flask import render_template
# from security_groups_manager import IpTablesManager
app = Flask(__name__)
app.config.from_object(__name__)


class IronWeb(flask.views.MethodView):
    def get(self):
        # post request to server to get ip blacklist
        # return 'Hello World!'
        blacklist = [{'ip' : '8.8.8.8/255.255.255.255'}]
        return render_template('ui.html', blacklist = blacklist)

    def post(self):
        #add to whitelist
        pass

app.add_url_rule('/', view_func=IronWeb.as_view('main'), methods=['GET', 'POST'])

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=80)