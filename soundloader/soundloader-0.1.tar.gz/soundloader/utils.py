#!/usr/bin/python3

import zipfile
from os import makedirs
from requests import get
from mutagen import File
from bs4 import BeautifulSoup
from mutagen.id3 import ID3, APIC
from soundloader import exceptions

header = {
	"Accept-Language": "en-US,en;q=0.5"
}

def request(url, control = False):
	try:
		thing = get(url, headers = header)
	except:
		thing = get(url, headers = header)

	if control:
		try:
			if thing.json()['errors']:
				raise exceptions.InvalidLink("Invalid link ;)")
		except KeyError:
			pass

	return thing

def create_zip(zip_name, nams):
	z = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)

	for a in nams:
		b = a.split("/")[-1]

		try:
			z.write(a, b)
		except FileNotFoundError:
			pass

	z.close()
				
def check_dir(directory):
	try:
		makedirs(directory)
	except FileExistsError:
		pass

def get_ids(body):
	parse = BeautifulSoup(body, "html.parser")

	ids = (
		parse
		.find("meta", property = "twitter:app:url:ipad")
		.get("content")
		.split(":")[-1]
	)

	return ids

def write_tags(song, data):
	tag = File(song, easy = True)
	tag.delete()
	tag['artist'] = data['artist']
	tag['title'] = data['music']
	tag['date'] = data['year']
	tag['genre'] = data['genre']
	tag['length'] = data['duration']
	tag['organization'] = data['label']
	tag.save()
	audio = ID3(song)

	audio['APIC'] = APIC(
		encoding = 3,
		mime = "image/jpeg", 
		type = 3,
		desc = u"Cover",
		data = data['image']
	)

	audio.save()