def create_reverse_many_to_one(model, payload):
    from .connector import ORM88

    class RelatedManyToOneDescriptors(ORM88):
        def __init__(self, *args, **kwargs):
            kwargs.update({
                'model': model
            })
            super(RelatedManyToOneDescriptors, self).__init__(*args, **kwargs)
            self._payload = payload

        def all(self):
            if self._prefetch_done:
                return self
            return super(RelatedManyToOneDescriptors, self).all()

    return RelatedManyToOneDescriptors
