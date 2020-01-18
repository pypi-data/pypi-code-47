#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'channel2index'

import os
import time

from html_telegraph_poster import TelegraphPoster
import telegram
import telegram.ext
from telegram.ext import Updater, MessageHandler, Filters

def getPoster(token):
	if token:
		return TelegraphPoster(access_token = token)
	return TelegraphPoster()

def post(token, source, posts):
	p = getPoster(token)
	if source.username:
		author_url = 'https://t.me/' + source.username,
	else:
		author_url = None
	text = '''	
<div>
	<p><strong>【频道简介】</strong></p>
	<p>%s</p>
	<br/>
	<p><strong>【索引】</strong></p>
	%s
</div>
	''' % (source.description.split()[0], ''.join(posts))
	r = p.post(
		title = '【频道手册】' + source.title, 
		author = source.title, 
		author_url = author_url,
		text = text)
	return r['url']

TEST = -1001181967872
CUT = [':', '：', '\n', '.', '-']

def trim(t):
	pivot = 'telegra.ph/'
	if pivot in t:
		index = t.find(pivot)
		t = t[index + len(pivot):]
	if t.startswith('http'):
		return t
	for c in CUT:
		t = t.split(c)[0]
	return t

def getBriefRaw(r):
	if r.document:
		return r.document.file_name
	if r.poll:
		return r.poll.question
	if r.text: 
		return r.text
	return ''

def getBrief(r):
	b = trim(getBriefRaw(r))
	if len(b) > 35:
		return b[:30] + '...'
	return b

def gen(source, bot_token, telegraph_token=None):
	tele = Updater(bot_token, use_context=True)
	test_channel = tele.bot.get_chat(-1001181967872)
	source = source.split('/')[-1]
	source = tele.bot.get_chat('@' + source)
	posts = []
	raw_index = 0
	real_index = 0
	skip = 0
	while skip < 30:
		raw_index +=1
		try:
			r = tele.bot.forward_message(TEST, source.id, raw_index)
		except:
			skip += 1
			continue
		skip = 0
		brief = getBrief(r)
		if not brief:
			continue
		link = 'https://t.me/%s/%s' % (source.username, raw_index)
		real_index += 1
		posts.append(
			'<p>%d.<a href="%s">%s</a></p>' % 
			(real_index, link, brief))
	return post(telegraph_token, source, posts)
		

