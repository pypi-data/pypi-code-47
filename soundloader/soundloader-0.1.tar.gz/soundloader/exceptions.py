#!/usr/bin/python3

class InvalidLink(Exception):
	def __init__(self, message):
		super().__init__(message)