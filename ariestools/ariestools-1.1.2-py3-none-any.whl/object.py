class Object(object):
    def __str__(self):
        return self.__dict__.__str__()
