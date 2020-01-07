import requests
from lxml import html
from lxml.etree import tostring
from youtube_transcript_api import YouTubeTranscriptApi

#Totally useless file tbh
def get_video_captions(video_id):

	CAPTION_URL = 'https://www.diycaptions.com/php/get-automatic-captions-as-txt.php?id='+video_id+'&language=asr'

	captionPage = requests.get(CAPTION_URL)
	captionTree = html.fromstring(captionPage.content)
	caption = captionTree.xpath('//div[@contenteditable="true"]/text()')

	return(str(caption))

if (__name__ == '__main__'):
	video_id='Cjim2F5Kk38'
	transcript_data = YouTubeTranscriptApi.get_transcripts(['Cjim2F5Kk38', 'DtdRCCMvllo'])
	for vid in transcript_data[0]:
		text_list = []
		counter = 0
		for trans_dict in transcript_data[0][vid]:
			if counter < 3:
				print(trans_dict['text'])
			text_list.append(trans_dict['text'])

		caption_text = "".join(text_list)
	# print(caption_text)



