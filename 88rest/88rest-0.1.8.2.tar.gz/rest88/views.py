from rest_framework.views import APIView as _APIView
from .request import Request


class APIView(_APIView):

    def initialize_request(self, request, *args, **kwargs):
        """
       Returns the initial request object.
       """
        parser_context = self.get_parser_context(request)

        return Request(
            request,
            parsers=self.get_parsers(),
            authenticators=self.get_authenticators(),
            negotiator=self.get_content_negotiator(),
            parser_context=parser_context
        )
