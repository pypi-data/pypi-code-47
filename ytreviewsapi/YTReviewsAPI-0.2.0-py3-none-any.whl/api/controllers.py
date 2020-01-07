from app.api import bp
from app import db
from app.api.errors import bad_request
from app.models import Video, Description, Comment, Caption, Server_Controller, Admin
from app.YouTubeAPICalls import search_videos_list, get_video_stats, get_comment_threads
from app.videoCaptions import get_video_captions
from app.api.auth import token_auth
from flask_login import current_user, login_user

from app.api.utils import get_movie_titles, get_youtube_list, get_comment_threads

from flask import jsonify
import pickle
import logging
import threading

@bp.route('/startservercontroller/<maxVideos>', methods=['GET'])
@token_auth.login_required
def start_server_thread(maxVideos):
	max_videos = int(maxVideos)
	if (maxVideos == '' or maxVideos == None): 
		max_videos = 1

	server_controller_exists = Server_Controller.query.get(1) != None

	if (server_controller_exists):
		server_controller = Server_Controller.query.get(1)
		server_controller.access_token = Admin.query.get(1).token
		server_controller.MAX_VIDEOS = max_videos
		server_controller.set_media_titles()
		server_controller.is_running = True

		thread = threading.Thread(target=start_server_controller, args=(server_controller,))
		thread.start()

		return_dict = {'status' : 'success'}
		return(jsonify(return_dict))

	server_controller = Server_Controller(Admin.query.get(1).token)
	server_controller.MAX_VIDEOS = max_videos
	server_controller.CURRENT_MOVIE = 0
	server_controller.CURRENT_VIDEO_ID = 0

	thread = threading.Thread(target=start_server_controller, args=(server_controller,))
	thread.start()

	return_dict = {'status' : 'success'}
	return(jsonify(return_dict))

def start_server_controller(server_controller):
	server_controller.run()

@bp.route('/get_movie_titles_file')
@token_auth.login_required
def get_movie_titles_file():
	try:
		START_YEAR = 2014
		END_YEAR = 2019
		movieYear = START_YEAR

		for i in range(END_YEAR - START_YEAR):
			IMDBUrl = 'https://www.imdb.com/search/title?year=' + str(movieYear) + '&title_type=feature&'


			imdbMoviePage = requests.get(IMDBUrl)

			#Movie page is now in a tree an accessible with xpath
			movieTree = html.fromstring(imdbMoviePage.content)

			movieHeaders= movieTree.xpath('//h3[@class="lister-item-header"]')

			#Write movies to csv
			fileStream = open("movieTitles.txt", "a+")
			for header in movieHeaders:

				headerStr = html.tostring(header, encoding='unicode')
				startIndex = headerStr.index('/">')
				endIndex = headerStr.index('</a>')
				
				headerTitle = headerStr[startIndex + 3 : endIndex]
				
				fileStream.write(headerTitle + '\n')
			fileStream.close()	

			movieYear = movieYear + 1

		return Response("{'status':'success!'}", status=200, mimetype='application/json')
	except:
		return Response("{'status':'An error occurred!'}", status=500, mimetype='application/json')

@bp.route('/titles/<year>', methods=['GET'])
def return_titles(year):
	EARLIEST_YEAR = 2014
	LATEST_YEAR = 2018
	MOVIES_PER_YEAR = 50
	print(year)

	if (int(year) > LATEST_YEAR or int(year) < EARLIEST_YEAR):
		return bad_request("Year must be between "+str(EARLIEST_YEAR)+" and "+str(LATEST_YEAR)+" inclusive.")

	return(jsonify(get_movie_titles(year,EARLIEST_YEAR)))


@bp.route('/video_caption/<video_id>', methods=['GET'])
@token_auth.login_required
def get_closed_captions(video_id):
	video_caption_text = get_video_captions(video_id)
	video_caption = Caption(body=video_caption_text, video_id=video_id)
	db.session.add(video_caption)

	db.session.commit()

	return_JSON = {"status" : 'success'}

	return(jsonify(return_JSON))




