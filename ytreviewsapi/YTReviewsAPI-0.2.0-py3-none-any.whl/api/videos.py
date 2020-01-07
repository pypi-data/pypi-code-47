from app.api import bp
from app import db
from app.models import Video, Server_Controller, Admin, Description, Comment, Caption
from flask import jsonify
from flask import request
from app.api.errors import error_response
from app.api.auth import token_auth
from app.api.controllers import return_titles
from app.api.utils import get_movie_titles, get_youtube_list, comment_threads, remove_video_entry, caption_data
from app.videoCaptions import get_video_captions

import requests
import pickle

@bp.route('/checkvideos/<videoid>', methods=['GET'])
@token_auth.login_required
def check_video(videoid):
	video = Video.query.filter_by(id=videoid)
	return_dict = {'status' : 'success'}
	if (video == None):
		return error_response(404, 'video not found')

	return(jsonify(return_dict))

@bp.route('/checkmedia/<title>', methods=['GET'])
@token_auth.login_required
def check_media(title):
	videos = Video.query.filter_by(mediaTitle=title).all()
	return_dict = {'status' : 'success'}
	if (not videos):
		return error_response(404, 'Videos with that title not found')

	return(jsonify(return_dict))


@bp.route('/videos/<title>', methods=['GET', 'DELETE', 'POST'])
@token_auth.login_required
def return_videos(title):
	if (request.method == 'GET'):
		returnAllVideos = title=='all'

		if (returnAllVideos):
			videos = Video.query.all()		
			return_dict = {'list':'resource'}
			l_video_dict = []

			for video in videos:
				l_video_dict.append(video.to_dict())

			return_dict['videos'] = l_video_dict


			return(jsonify(return_dict))


		videos = Video.query.filter_by(mediaTitle=title)
			
		return_dict = {'list':'resource'}
		l_video_dict = []

		for video in videos:
			l_video_dict.append(video.to_dict())

		return_dict['videos'] = l_video_dict

		if (len(l_video_dict) == 0):
			return error_response(404, title + ' not found')


		return(jsonify(return_dict))

	if (request.method == 'DELETE'):
		access_token = Admin.query.get(1).token
		videos = Video.query.filter_by(mediaTitle=title)

		if not videos:
			return error_response(404, 'Videos with that title not found')

		for video in videos:
			remove_video_entry(video.id)

			# if (response.status_code != 200):
			# 	return error_response(response.status_code, "error getting videos")

	if (request.method == 'POST'):
		print("Getting " + title)
		access_token = Admin.query.get(1).token
		videoIDs_JSON = get_youtube_list(title, 5)

		l_videoIDs = videoIDs_JSON['video_IDs']

			#Get the comment threads NOTE: emojis really mess with this
			# print("getting comments")
			# response = comment_threads(video_id, 100)

		#Get the captions
		print("getting captions")
		response = caption_data(l_videoIDs)
		if response['status'] == 'failure':
			print("could not get caption of video ", video_id)


	return(jsonify({"status": "success"}))


@bp.route('/videoentry/<videoid>', methods=['DELETE', 'POST'])
@token_auth.login_required
def edit_video_entry(videoid):
	return_dict= {'status' : 'success'}

	if (request.method == 'DELETE'):
		remove_video_entry(video_id)

	if (request.method == 'POST'):
		video = Video.query.filter_by(id=videoid).first()
		access_token = Admin.query.get(1).token

		if (video is not None):
			return(error_response(405, 'video is already in database'))

		#TODO


	return(jsonify(return_dict))

#This route is for the go backend to call to get the bare minimum data needed to display
@bp.route('/govideos/<title>/<year>', methods=['GET'])
# @token_auth.login_required
def get_go_videos(title,year=None):
	if title == "all":
		#videos = Video.query.all()
		#for video in videos:
			#TODO do score stuff here
		#TODO make the titles have a return all option
		response_JSON=get_movie_titles(year, 2014)
		failed_responses = 0
		for title in response_JSON["titles"]:
			return_dict={"title" : title}
			return_dict["score"]= "75"
			return_dict["date"]="02/04/1999"
			#This should be called naturally
			response = requests.post('http://truereview.network/api/movies/p', json=return_dict)
			if response.status_code != requests.codes.ok:
				failed_responses += 1
		return(jsonify({"failedResponses" : failed_responses}))

	videos = Video.query.filter_by(mediaTitle=title).all()
	#for video in videos:
		#Do stuff here like compress score 
	return_dict={"title" : title}

	#Just does a straight average of the scores
	score = 0
	valid_videos = [video.score for video in videos if video.score != -1]
	score = sum(valid_videos)
	score = score / len(valid_videos)
	score = int(score)

	return_dict["score"]=str(score)

	#TODO get an actual date
	#UPDATE: do we even need a date? Shouldn't this be in App side?
	return_dict["date"]="02/04/1999"
	response = requests.post('http://truereview.network/api/movies/p', json=return_dict)
	print(response.json())

	return jsonify(return_dict)
		









		




