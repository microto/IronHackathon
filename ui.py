from flask import Flask
import flask
from flask import render_template, views
from iptables_manager import IpTablesManager

app = Flask(__name__)
app.config.from_object(__name__)


class IronWeb(flask.views.MethodView):
    def get(self):
        # post request to server to get ip blacklist
        # return 'Hello World!'
        # blacklist = [{'ip' : '8.8.8.8/255.255.255.255'}]
        blacklist = []
        o = IpTablesManager()
        res = o.get_blacklist()
        for item in res:
            blacklist.append(item['IP'])
        return render_template('ui.html', blacklist = blacklist)

    def post(self):
        #add to whitelist
        ip = flask.request.form['ip']
        o = IronBlockIPS()
    	o.add_to_white_list(ip)
        pass

app.add_url_rule('/', view_func=IronWeb.as_view('main'), methods=['GET', 'POST'])

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=80)
