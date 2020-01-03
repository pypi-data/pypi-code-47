class BaseClass(object):
    def get_file_extension(self, filename):
	    return filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
