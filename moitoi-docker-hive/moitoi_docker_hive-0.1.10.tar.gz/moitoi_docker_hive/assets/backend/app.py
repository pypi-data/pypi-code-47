import os
import logging
import re

from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Link, Separator
from config import BaseConfig
from forms import ClusterSetupForm

cluster_id = os.environ.get("MDH_CLUSTER_ID")

nav = Nav()

# registers the "top" menubar
nav.register_element('frontend_top', Navbar(
    View('MDH', 'index'),
    Subgroup(
        'Service',
        Link('Add service', 'Service?cmd=add_service'.format(cluster_id)),
        Separator(),
        Link('Add node', 'Service?cmd=add_node&cluster_id={}'.format(cluster_id)),
        Link('Remove node', 'Service?cmd=rm_node&cluster_id={}'.format(cluster_id)),
        Separator(),
        Link('Cluster state', 'State?cluster_id={}'.format(cluster_id)),
        Link('Clusters state', 'State'),
        Separator(),
        Link('Grafana', 'Grafana'),

    ),
))

app = Flask(__name__)
app.config['DEBUG'] = re.match("(1|TRUE|Y|True)", os.environ.get('DEBUG', "false"))
nav.init_app(app)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

app.config.from_object(BaseConfig)
Bootstrap(app)


@app.route('/', methods=('GET', 'POST'))
def index():
    form = ClusterSetupForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('index.html', hostname=os.environ.get("MDH_HOSTNAME"), mdh_cluster_id=cluster_id, form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
