from app.api import bp
from app import db
from app import APP_URL
from app.models import Video, Server_Controller, Admin
from flask import jsonify
from flask import request
from app.api.errors import error_response
from flask_login import current_user, login_user
from app.api.auth import token_auth
from app.api.utils import get_movie_titles

import requests

@bp.route('/web/serverstatus', methods=['GET'])
def return_server_status():
	server_controller = Server_Controller.query.get(1)

	return_dict={'server_controller':'status'}

	if (server_controller == None):
		return_dict['status'] = 'No collection running'
		return_dict['CurrentMovie'] = 0
		return_dict['isRunning'] = False
		return_dict['currentYear'] = 2014
		return(jsonify(return_dict))

	return_dict['CurrentMovie'] = server_controller.CURRENT_MOVIE
	return_dict['isRunning'] = server_controller.is_running

	if (server_controller.CURRENT_MOVIE // 50  == 0):
		return_dict['currentYear'] = 2014
	if (server_controller.CURRENT_MOVIE // 50  == 1):
		return_dict['currentYear'] = 2015
	if (server_controller.CURRENT_MOVIE // 50  == 2):
		return_dict['currentYear'] = 2016
	if (server_controller.CURRENT_MOVIE // 50  == 3):
		return_dict['currentYear'] = 2017
	if (server_controller.CURRENT_MOVIE // 50  == 4):
		return_dict['currentYear'] = 2018

	return(jsonify(return_dict))

@bp.route('/web/videostatus/<year>', methods=['GET'])
def get_video_status(year):
	access_token = Admin.query.get(1).token
	print(APP_URL + '/api/titles/' + year)
	response = requests.get(APP_URL + '/api/titles/' + year, headers={'Authorization': 'Bearer '+ access_token})
	print('response received: ', response)
	if (response.status_code == 404):
		return(error_response(404, 'could not find titles'))

	response_JSON = response.json()
	return_dict = {'title': 'status'}
	l_status_tuples = []

	if (current_user.is_authenticated):
		for title in response_JSON["titles"]:
			response = requests.get(APP_URL +'/api/checkmedia/'+title, headers={'Authorization': 'Bearer '+ access_token})
			if (response.status_code == 404):
				l_status_tuples.append((title, "0"))
			else:
				l_status_tuples.append((title, "1"))

		return_dict['mediaStatus'] = l_status_tuples

		return(jsonify(return_dict))

	return(error_response(401, "user unauthorized"))



@bp.route('/web/authentication', methods=['POST'])
def check_auth():
	data = request.get_json() or {}
	presumed_admin = Admin.query.filter_by(username=data['username']).first()
	return_dict= {'loginStatus' : True}

	if (presumed_admin == None):
		return_dict['loginStatus'] = False
		return(error_response(401, 'username or password incorrect'))

	if (presumed_admin.check_password(data['password']) != True):
		return_dict['loginStatus'] = False
		return(error_response(401, 'username or password incorrect'))


	login_user(presumed_admin)
	return(jsonify(return_dict))

@bp.route('/web/controlauthentication/<maxVideos>', methods=['POST'])
def check_control_auth(maxVideos):

	if (current_user.is_authenticated):
		response = requests.get(APP_URL + "/api/startservercontroller/"+ maxVideos,
		  headers={'Authorization': 'Bearer '+ current_user.token})
		return(response.content, response.status_code, response.headers.items())

	return(error_response(401, 'not logged in'))


@bp.route('/web/videoentry/<videoid>', methods=['DELETE', 'POST'])
def call_videos(videoid):
	if (current_user.is_authenticated):
		if (request.method == 'DELETE'):
			access_token = Admin.query.get(1).first().token
			response = requests.delete(APP_URL + '/api/videoentry/'+videoid,
				 headers={'Authorization': 'Bearer '+ access_token})
			return(response.content, response.status_code, response.headers.items())

		if (request.method == 'POST'):
			return_dict= {'status' : 'TODO'}
			return(jsonify(return_dict))

	return(error_response(401, 'not logged in'))

@bp.route('/web/mediaentry/<title>', methods=['DELETE', 'POST'])
def call_mediaentry(title):
	if (current_user.is_authenticated):
		if (request.method == 'DELETE'):
			access_token = Admin.query.get(1).token
			response = requests.delete(APP_URL +'/api/videos/'+title,
				 headers={'Authorization': 'Bearer '+ access_token})
			return(response.content, response.status_code, response.headers.items())

		if (request.method == 'POST'):
			access_token = Admin.query.get(1).token
			response = requests.post(APP_URL+'/api/videos/'+title,
				 headers={'Authorization': 'Bearer '+ access_token})
			return(response.content, response.status_code, response.headers.items())


	return(error_response(401, 'not logged in'))

@bp.route('/web/videoview/<title>', methods=['GET', 'POST'])
def get_video_views(title):
	if (current_user.is_authenticated):
		if (request.method == 'GET'):
			videos = Video.query.filter_by(mediaTitle=title).all()
			l_video_views = []
			for video in videos:
				l_video_views.append({
					"title" : video.title,
					"score" : video.score,
					"id" : video.id
					})
			return(jsonify({"videoViews" : l_video_views}))

		if (request.method == 'POST'):
			data = request.get_json() or {}
			videos = Video.query.filter_by(mediaTitle=data['mediaTitle']).all()
			for videoView in data['videos']:
				for video in videos:
					if (video.id == videoView['id']):
						video.score = videoView['score']
						db.session.add(video)
						break
			db.session.commit()
			response = requests.get(APP_URL+'/api/govideos/'+data['mediaTitle'])

			return(jsonify({"status":"success"}))


	return(error_response(401, 'not logged in'))	












