# -*- coding: utf-8 -*-

class OSAsset(object):
	"""
	An asset file used by a volume template for booting or installing an OS.
	"""

	def __init__(self, os_asset_filename, os_asset_file_size_bytes):
		self.os_asset_filename = os_asset_filename;
		self.os_asset_file_size_bytes = os_asset_file_size_bytes;


	"""
	The ID of the OS asset.
	"""
	os_asset_id = None;

	"""
	Owner. Delegates of this user can manage his Ansible bundles as well. When
	null, defaults to the API authenticated user.
	"""
	user_id_owner = None;

	"""
	The user which last updated the bundle.
	"""
	user_id_authenticated = None;

	"""
	Public assets are published by us and are accessible by all users.
	"""
	os_asset_is_public = False;

	"""
	Filename of the OS asset file.
	"""
	os_asset_filename = None;

	"""
	File size of the stored OS asset content. Null if os_asset_source_url is
	given.
	"""
	os_asset_file_size_bytes = None;

	"""
	File mime of the OS asset file.
	"""
	os_asset_file_mime = "application/octet-stream";

	"""
	Stored contents in base 64.
	"""
	os_asset_contents_base64 = None;

	"""
	Original content sha256 hash as a lowercase hex string.
	"""
	os_asset_contents_sha256_hex = None;

	"""
	Usage of OS asset.
	"""
	os_asset_usage = None;

	"""
	URL from which to serve the file. If just absolute pathname, the file will
	be served from our repo. If a complete http(s) URL it will be used as is. If
	os_asset_contents_base64 is set this will be ignored.
	"""
	os_asset_source_url = None;

	"""
	Date and time of the OS template's creation.
	"""
	os_asset_created_timestamp = None;

	"""
	Date and time of the OS template's update (replace).
	"""
	os_asset_updated_timestamp = None;

	"""
	The schema type.
	"""
	type = None;
