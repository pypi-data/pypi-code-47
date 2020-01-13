from djangoldp.views import LDPViewSet
from .models import Circle


class CirclesJoinableViewset(LDPViewSet):
    model = Circle

    def get_queryset(self):
        return super().get_queryset() \
                      .exclude(team__id=self.request.user.id) \
                      .exclude(status="Private") \
                      .exclude(status="Archived")
