def search_videos_list(youtube, query_term, max_results):
    request = youtube.search().list(
        part="snippet",
        q=query_term,
        type="video",
        maxResults=max_results
    )

    response = request.execute()
    movieListJSON = response

    return response["items"]

def get_comment_threads(youtube, video_id, max_results):
    print('requesting YT')
    request = youtube.commentThreads().list(
    part="snippet",
    maxResults=100,
    textFormat="plainText",
    videoId=video_id
    )

    response = request.execute()

    return response["items"]

def get_video_stats(youtube, video_id):
    request = youtube.videos().list(
    part="statistics",
    id=video_id
    )

    response = request.execute()

    return response["items"]
    
def get_comments(youtube, parent_id):
    request = youtube.comments().list(
    part="snippet",
    parentId=parent_id,
    textFormat="plainText"
    )

    response = request.execute()

    return response["items"]





