# -*- coding: utf-8 -*-

class AnsibleBundle(object):
	"""
	An Ansible bundle contains an Ansible project as a single archive file,
	usually .zip
	"""

	def __init__(self, ansible_bundle_type, ansible_bundle_archive_filename):
		self.ansible_bundle_type = ansible_bundle_type;
		self.ansible_bundle_archive_filename = ansible_bundle_archive_filename;


	"""
	Unique Ansible bundle ID.
	"""
	ansible_bundle_id = None;

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
	For example: Hello World!
	"""
	ansible_bundle_title = "No title specified";

	"""
	"""
	ansible_bundle_description = None;

	"""
	"""
	ansible_bundle_type = None;

	"""
	For example: ansible_install_some_stuff.zip
	"""
	ansible_bundle_archive_filename = None;

	"""
	ZIP archive in base64 format.
	"""
	ansible_bundle_archive_contents_base64 = None;

	"""
	Date and time of the Ansible bundle's creation.
	"""
	ansible_bundle_created_timestamp = None;

	"""
	Date and time of the Ansible bundle's update (replace).
	"""
	ansible_bundle_updated_timestamp = None;

	"""
	The schema type
	"""
	type = None;
