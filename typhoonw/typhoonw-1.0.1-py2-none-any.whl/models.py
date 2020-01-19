#-*- coding:utf-8 -*-

from typhoonw.extensions import db

class Total(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_name = db.Column(db.String(99))
    strength = db.Column(db.String(99))
    affect_strength = db.Column(db.String(99))
    landing_place = db.Column(db.String(99))
    affect_period = db.Column(db.String(99))
    affect_month = db.Column(db.String(99))
    yuhuan_rainfall = db.Column(db.String(99))
    hongjia_rainfall = db.Column(db.String(99))
    wenling_rainfall = db.Column(db.String(99))
    linhai_rainfall = db.Column(db.String(99))
    xianju_rainfall = db.Column(db.String(99))
    sanmen_rainfall = db.Column(db.String(99))
    tiantai_rainfall = db.Column(db.String(99))
    watershed_average = db.Column(db.String(99))
    path = db.Column(db.String(99))
    rainstorm_type = db.Column(db.String(99))

class PathDesc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_num = db.Column(db.String(99))
    type_desc = db.Column(db.String(99))
    typhoon_count = db.Column(db.String(99))
    typhoon_id = db.Column(db.String(99))

class RainstormDesc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(99))
    name = db.Column(db.String(99))
    middle_high_latitude = db.Column(db.String(99))
    through_ridge_strength = db.Column(db.String(99))
    subtropical_high588 = db.Column(db.String(99))
    location_of_ridge_axis = db.Column(db.String(99))
    point = db.Column(db.String(99))
    max_speed = db.Column(db.String(99))
    hold_time = db.Column(db.String(99))