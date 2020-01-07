from app import app
from app import db
from app.models import Video, Description, Comment, Caption
from app.YouTubeAPICalls import search_videos_list, get_video_stats, get_comment_threads
from flask import Response
from flask import jsonify
from flask import render_template, redirect, url_for
from app.api.auth import basic_auth
from .videoCaptions import get_video_captions
from flask_login import login_required

import requests 
import datetime
from lxml import html
from lxml.etree import tostring
import pickle
from flask_login import current_user, login_user

@app.route('/')
@app.route('/control')
@login_required
def show_control_center():
	return(render_template('control_page.html'))

@app.route('/login')
def login():
	if current_user.is_authenticated:
		return redirect(url_for('show_control_center'))

	return(render_template('login.html'))

@app.route('/get_movie_titles_file')
def get_movie_titles():
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








	
