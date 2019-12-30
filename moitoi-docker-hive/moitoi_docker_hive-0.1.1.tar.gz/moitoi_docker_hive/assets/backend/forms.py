from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired


class ClusterSetupForm(FlaskForm):
    clusters = IntegerField('Clusters', validators=[DataRequired()])
    replicas = IntegerField('Replicas', validators=[DataRequired()])
