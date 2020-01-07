from app import db
from app import basedir
from app.YouTubeAPICalls import search_videos_list, get_video_stats, get_comment_threads
from app.models import Video, Description, Comment, Caption, Server_Controller, Admin
from youtube_transcript_api import YouTubeTranscriptApi
import pickle
import os


#TODO seperate getting data and commiting to database 



def get_movie_titles(year, EARLIEST_YEAR):
	print("getting file")
	print("base directory: ", basedir)
	movieTitlesFile = open(basedir + "/movieTitles.txt", "r")
	movie_titles_JSON = {"type":"movie titles"}
	l_movie_titles = []

	#Reading the movie titles specific to that year
	counter_min = (int(year) - EARLIEST_YEAR) * 50
	counter_max = counter_min + 50
	counter = 0
	print("reading file")
	for line in movieTitlesFile:
		print(line)
		if (counter >= counter_min and counter < counter_max):
			l_movie_titles.append(line[:len(line) - 1])

		counter+=1
	print('file read')

	movie_titles_JSON["titles"] = l_movie_titles
	return(movie_titles_JSON)

def get_youtube_list(title, max_results):
	with open(basedir + '/service1.pkl', 'rb') as input:
		youtube = pickle.load(input)

	max_results = 5
	queryTerm =  title + ' movie review'
	movieListJSON = search_videos_list(youtube, queryTerm, max_results)

	l_video_id = []

	for item in movieListJSON:
		videoId = item["id"]["videoId"]
		channelId = item["snippet"]["channelId"]
		videoTitle = item["snippet"]["title"]
		videoDescription = item["snippet"]["description"]
		channelTitle = item["snippet"]["channelTitle"]
		mediaTitle = title

		stats_response = get_video_stats(youtube, videoId)

		view_count = stats_response[0]["statistics"]["viewCount"]
		like_count = stats_response[0]["statistics"]["likeCount"]
		dislike_count = stats_response[0]["statistics"]["dislikeCount"]
		favorite_count = stats_response[0]["statistics"]["favoriteCount"]
		comment_count = stats_response[0]["statistics"]["commentCount"]

		l_video_id.append(videoId)

		video = Video(id=videoId, title=videoTitle, views=view_count, likeCount=like_count,
			dislikeCount=dislike_count, channel_id=channelTitle, favoriteCount=favorite_count, commentCount=comment_count, mediaTitle=mediaTitle)
		print(video)
		db.session.add(video)

		#Add video description
		description = Description(body=videoDescription, video_id=videoId)
		db.session.add(description)
		db.session.commit()
	print(l_video_id)
	return_JSON = {"video_IDs" : l_video_id}
	return return_JSON

def comment_threads(video_id, max_comment_threads):
	with open(basedir + '/service1.pkl', 'rb') as input:
		youtube = pickle.load(input)

	commentThreads = get_comment_threads(youtube, video_id, max_comment_threads)

	for item in commentThreads: 
		parentId = item["id"]
		topLevelComment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

		comment = Comment(body=topLevelComment, video_id=video_id)

		db.session.add(comment)

	db.session.commit()

	return_JSON = {"status" : 'success'}
	return return_JSON

def caption_data(video_ids):
	transcript_data = YouTubeTranscriptApi.get_transcripts(video_ids=video_ids, continue_after_error=True)
	for vid in transcript_data[0]:
		text_list = []
		counter = 0
		for trans_dict in transcript_data[0][vid]:
			#I think this is where they are getting concatenateds
			if counter < 2:
				print(trans_dict['text'])
				counter +=1
			text_list.append(trans_dict['text'])
			text_list.append(' ')

		caption_text = "".join(text_list)
		caption = Caption(body=caption_text, video_id=vid)
		db.session.add(caption)
		db.session.commit()

	return_JSON = {"status" : 'success'}
	return return_JSON



def remove_video_entry(videoid):
	video = Video.query.filter_by(id=videoid).first()
	if (video is None):
		return('not found')

	description = Description.query.filter_by(video_id=videoid).first()
	if (description is not None):
		db.session.delete(description)

	comments = Comment.query.filter_by(video_id=videoid).all()
	if (comments is not None):
		for comment in comments:
			db.session.delete(comment)

	caption = Caption.query.filter_by(video_id=videoid).first()
	if (caption is not None):
		db.session.delete(caption)

	db.session.delete(video)
	db.session.commit()
	


