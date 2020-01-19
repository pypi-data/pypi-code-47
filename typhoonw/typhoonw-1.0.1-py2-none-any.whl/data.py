#-*- coding:utf-8 -*-

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify,
    make_response
)
from typhoonw.models import PathDesc, RainstormDesc, Total
from typhoonw.extensions import db
import flask_excel as excel
from sqlalchemy import or_
from typhoonw.auth import login_required

data_bp = Blueprint('data', __name__, url_prefix='/data')

@data_bp.route('/index', methods=('GET', 'POST'))
@login_required
def index():
    if request.method == 'POST':
    	# output_string = request.get_array(field_name='file')[0][11]
        # return output_string
        data = request.get_array(field_name='file',sheet_name=u"总表")
        for data_line in data:
        	# print data_line[0]
        	db.session.add(Total(num_name=data_line[0], 
        		strength=data_line[1],
        		affect_strength=data_line[2],
        		landing_place=data_line[3],
        		affect_period=data_line[4],
        		affect_month=data_line[5],
                yuhuan_rainfall=data_line[6],
                hongjia_rainfall=data_line[7],
                wenling_rainfall=data_line[8],
                linhai_rainfall=data_line[9],
                xianju_rainfall=data_line[10],
                sanmen_rainfall=data_line[11],
                tiantai_rainfall=data_line[12],
                watershed_average=data_line[13],
                path=data_line[14],
                rainstorm_type=data_line[15]
        		))

        data = request.get_array(field_name='file',sheet_name=u"路径说明")
        for data_line in data:
        	db.session.add(PathDesc(type_num=data_line[0],
        		type_desc=data_line[1],
        		typhoon_count=data_line[2],
        		typhoon_id=data_line[3]
        		))

        data = request.get_array(field_name='file', sheet_name=u"暴雨天气型说明")
        for data_line in data:
        	db.session.add(RainstormDesc(type=data_line[0],
        		name=data_line[1],
                middle_high_latitude=data_line[2],
                through_ridge_strength=data_line[3],
                subtropical_high588=data_line[4],
                location_of_ridge_axis=data_line[5],
                point=data_line[6],
                max_speed=data_line[7],
                hold_time=data_line[8]
        		))
    return render_template('data/index.html')

@data_bp.route("/parting_intro", methods=['GET'])
@login_required
def parting_intro():
    return render_template('data/parting_intro.html')

@data_bp.route("/landing_intro", methods=['GET'])
@login_required
def landing_intro():
    return render_template('data/landing_intro.html')

@data_bp.route("/query", methods=['GET', 'POST'])
@login_required
def query():
    storm_types = ["A1","A2","B","C","D","E","F","G","H","J","K"]
    if request.method == 'POST':
        storm_type = request.form['storm_type']
        error = None
        if storm_type is None:
            error = '请输入一种暴风类型！'
        if storm_type not in storm_types:
            error = '输入有误！'

        if error is None:
            return redirect(url_for('data.total_data', type_str=storm_type))
        else:
            flash(error)
    return render_template('data/query.html')

# @data_bp.route("/handson_view", methods=['GET'])
# def handson_table():
#     return excel.make_response_from_tables(
#         db.session, [Total, PathDesc, RainstormDesc], 'handsontable.html')

@data_bp.route("/total_data/<string:type_str>", methods=['GET'])
@login_required
def total_data(type_str):
    try:
        q = Total.query.filter(or_(Total.id==2,Total.rainstorm_type==type_str)).all()
        return excel.make_response_from_query_sets(query_sets=q, column_names=['num_name',
        'strength','affect_strength','landing_place','affect_period','affect_month',
        'yuhuan_rainfall','hongjia_rainfall','wenling_rainfall','linhai_rainfall',
        'xianju_rainfall','sanmen_rainfall','tiantai_rainfall','watershed_average',
        'path','rainstorm_type'], file_type='handsontable.html')
    except Exception, e:
        return "something wrong!"

@data_bp.route("/add_item", methods=['GET', 'POST'])
@login_required
def add_item():
    if request.method == 'POST':
        num_name = request.form['num_name']
        strength = request.form['strength']
        affect_strength = request.form['affect_strength']
        landing_place = request.form['landing_place']
        affect_period = request.form['affect_period']
        affect_month = request.form['affect_month']
        yuhuan_rainfall = request.form['yuhuan_rainfall']
        hongjia_rainfall = request.form['hongjia_rainfall']
        wenling_rainfall = request.form['wenling_rainfall']
        linhai_rainfall = request.form['linhai_rainfall']
        xianju_rainfall = request.form['xianju_rainfall']
        sanmen_rainfall = request.form['sanmen_rainfall']
        tiantai_rainfall = request.form['tiantai_rainfall']
        watershed_average = request.form['watershed_average']
        path = request.form['path']
        rainstorm_type = request.form['rainstorm_type']
        error = None

        new_item = Total(num_name = num_name,
            strength = strength,
            affect_strength = affect_strength,
            landing_place = landing_place,
            affect_period = affect_period,
            affect_month = affect_month,
            yuhuan_rainfall=yuhuan_rainfall,
            hongjia_rainfall=hongjia_rainfall,
            wenling_rainfall=wenling_rainfall,
            linhai_rainfall=linhai_rainfall,
            xianju_rainfall=xianju_rainfall,
            sanmen_rainfall=sanmen_rainfall,
            tiantai_rainfall=tiantai_rainfall,
            watershed_average=watershed_average,
            path=path,
            rainstorm_type=rainstorm_type
            )
        db.session.add(new_item)
        db.session.commit()

        if error is not None:
            flash(error)

    return render_template('data/add_item.html')
