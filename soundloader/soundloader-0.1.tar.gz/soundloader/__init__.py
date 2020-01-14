#!/usr/bin/python3

import os
from tqdm import tqdm
from requests import get
from soundloader.utils import *

client_id = "a3e059563d7fd3372b49b37f00a00bcf"
api_trk = "https://api-v2.soundcloud.com/tracks/{}?client_id={}"
api_ply = "https://api.soundcloud.com/playlists/{}?client_id={}"
stock_output = "%s/Songs/" % os.getcwd()
stock_recursive_download = False
stock_not_interface = False
stock_zip = False
answers = ["Y", "y", "Yes", "YES"]

def download(ids, output, recursive_download):
	datas = {}
	api_link = api_trk.format(ids, client_id)
	json = request(api_link).json()
	datas['artist'] = json['user']['username']
	datas['music'] = json['title']
	datas['year'] = json['created_at']
	datas['genre'] = json['genre']
	datas['duration'] = str(json['duration'] * 1000)
	datas['label'] = str(json['label_name'])	
	image = json['artwork_url'].replace("large", "t500x500")
	datas['image'] = request(image).content

	pl_url = "{}?client_id={}".format(
		json['media']['transcodings'][0]['url'] , client_id
	)

	pl_file = request(pl_url).json()['url']
	thing = request(pl_file).text
	links = thing.replace("\n", ",").split(",")[7:-1]
	f_path = "{}{}.mp3".format(output, ids)

	if os.path.isfile(f_path):
		if recursive_download:
			return f_path

		ans = input("Track %s already exists, do you want to redownload it?(y or n): " % f_path)

		if not ans in answers:
			return f_path

	song = open(f_path, "wb")

	for a in range(
		0, len(links), 3
	):
		content = request(links[a]).content
		song.write(content)

	song.close()
	write_tags(f_path, datas)
	return f_path

def dw_track(
	link,
	output = stock_output,
	recursive_download = stock_recursive_download
):
	output += "/"
	body = request(link).text
	ids = get_ids(body)
	check_dir(output)
	return download(ids, output, recursive_download)

def dw_album(
	link,
	output = stock_output,
	recursive_download = stock_recursive_download,
	not_interface = stock_not_interface,
	zips = stock_zip
):
	output += "/"
	body = request(link).text
	ids = get_ids(body)
	check_dir(output)
	api_link = api_ply.format(ids, client_id)
	json = request(api_link).json()

	array = [
		download(
			"%d" % a['id'], output, recursive_download
		) for a in tqdm(json['tracks'], disable = not_interface)
	]

	if zips:
		zip_name = "{}{}.zip".format(output, ids)
		create_zip(zip_name, array)
		return array, zip_name
	
	return array