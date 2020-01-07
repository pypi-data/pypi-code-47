from app import db
from app import login

from flask import jsonify
import requests
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import base64
import os

class Video(db.Model):
	id = db.Column(db.String(15), primary_key=True)
	title = db.Column(db.String(100), index=True)
	mediaTitle = db.Column(db.String(100))
	date = db.Column(db.DateTime)
	views = db.Column(db.Integer)
	likeCount = db.Column(db.Integer)
	dislikeCount = db.Column(db.Integer)
	favoriteCount = db.Column(db.Integer)
	commentCount = db.Column(db.Integer)
	channel_id = db.Column(db.Text)
	score = db.Column(db.Integer)
	description = db.relationship("Description", lazy='dynamic')
	comments = db.relationship("Comment", lazy='dynamic')
	caption = db.relationship("Caption", lazy='dynamic')

	def to_dict(self):
		return_dict = {'title': self.title}
		return_dict['mediaTitle'] = self.mediaTitle
		return_dict['views'] = self.views
		return_dict['likeCount'] = self.likeCount
		return_dict['dislikeCount'] = self.dislikeCount
		return_dict['favoriteCount'] = self.favoriteCount
		return_dict['commentCount'] = self.commentCount

		l_comment_dict = []
		for comment in self.comments.all():
			l_comment_dict.append(comment.body)
		return_dict['comments'] = l_comment_dict

		for description in self.description.all():
			return_dict['description'] = description.body
		for caption in self.caption.all():
			return_dict['caption'] = caption.body

		return(return_dict)


	def __repr__(self):
		return '<Video id={}, title={}>'.format(self.id, self.title)

class Description(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.Text)
	video_id = db.Column(db.String(15), db.ForeignKey("video.id"))

	def to_dict(self):
		return_dict = {'body' : self.body}

	def __repr__(self):
		return'<body= {}>'.format(self.body)

class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.Text)
	video_id = db.Column(db.String(15), db.ForeignKey("video.id"))

	def to_dict(self):
		return_dict = {'body' : self.body}

	def __repr__(self):
		return '<body= {}>'.format(self.body)

class Caption(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.Text)
	video_id = db.Column(db.String(15), db.ForeignKey("video.id"))

	def to_dict(self):
		return_dict = {'body' : self.body}

	def __repr__(self):
		return '<body= {}>'.format(self.body)

#This helps flask_login determine that the current user of a website is of type 
#Admin and can verify them as such
@login.user_loader
def load_user(id):
    return Admin.query.get(int(id))

class Admin(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), unique=True)
	token = db.Column(db.String(32), index=True, unique=True)
	logged_in = db.Column(db.Boolean)
	password_hash = db.Column(db.String(128))

	def get_token(self):
		now = datetime.utcnow()
		self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
		db.session.add(self)
		return self.token

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	@staticmethod
	def check_token(token):
		admin = Admin.query.filter_by(token=token).first()
		if admin is None:
			return None
		return admin
	def __repr__(self):
		return '<username= {}, token = {}>'.format(self.username, self.token)

#The server controller calls the internal APIs in sequential
#order and monitors their responses 


class Server_Controller(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	CURRENT_API = db.Column(db.Integer)
	CURRENT_FILE_INDEX = db.Column(db.Integer)
	CURRENT_MOVIE = db.Column(db.Integer)
	CURRENT_VIDEO_ID = db.Column(db.Integer)
	is_running = db.Column(db.Boolean)
	is_finished = db.Column(db.Boolean)

	l_movie_titles = []
	access_token = ''
	MAX_VIDEOS = 1

	def __init__(self, access_token, max_videos=1):
		self.set_media_titles()
		self.access_token = access_token
		self.MAX_VIDEOS = max_videos


	def run(self):
		movie_counter = 0
		video_counter = 0
		self.is_running = True


		for title in self.l_movie_titles[self.CURRENT_MOVIE:]:
			if (movie_counter == self.MAX_VIDEOS):
				break
			videoIDs_JSON = requests.post('https://truereview.dev/api/videos/'+ title, headers={'Authorization': 'Bearer '+self.access_token})

			movie_counter += 1
			self.CURRENT_MOVIE += 1
			self.save_state()

		self.is_running = False
		self.save_state()


	def set_media_titles(self):
		self.CURRENT_API = 0
		movieTitlesFile = open("movieTitles.txt", "r")
		for line in movieTitlesFile:
			self.l_movie_titles.append(line[:len(line) - 1])

	def get_videos(self, title):
		self.CURRENT_API = 1
		videoIDs_JSON = requests.post('https://truereview.dev/api/youtube_list/'+ title, headers={'Authorization': 'Bearer '+self.access_token})
		videoIDs_JSON = videoIDs_JSON.json()

		l_videoIDs = videoIDs_JSON['video_IDs']
		
		return l_videoIDs


	def get_comment_threads(self, video_id):
		self.CURRENT_API = 2
		response = requests.get('https://truereview.dev/api/comment_threads/'+video_id, headers={'Authorization': 'Bearer '+self.access_token})
		if (response.status_code != requests.codes.ok):
			pass

	def get_video_captions(self, video_id):
		self.CURRENT_API = 1
		response = requests.get('https://truereview.dev/api/video_caption/'+video_id, headers={'Authorization': 'Bearer '+self.access_token})
		if (response.status_code != requests.codes.ok):
			pass

	def save_state(self):
		db.session.add(self)
		db.session.commit()

	def to_dict(self):
		return_dict = {'current_movie':self.CURRENT_MOVIE}
		return_dict['current_video'] = self.CURRENT_VIDEO_ID
		return_dict['current_api'] = self.CURRENT_API

		return(return_dict)



