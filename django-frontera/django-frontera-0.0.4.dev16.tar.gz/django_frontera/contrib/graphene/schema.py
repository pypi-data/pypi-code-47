from graphene import relay, ObjectType

class CountableConnectionBase(relay.Connection):
    total_count = graphene.Int()
    
    class Meta:
        abstract = True

    def resolve_total_count(self, info, **kwargs):
        return self.iterable.count()