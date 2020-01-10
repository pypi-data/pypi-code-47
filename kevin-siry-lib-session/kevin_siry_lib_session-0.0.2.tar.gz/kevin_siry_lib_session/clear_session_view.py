from rest_framework import generics, status
from rest_framework.response import Response

from . import session


class ClearSessionView(generics.GenericAPIView):

    @staticmethod
    def delete(request):
        try:
            if session.delete_session(request):
                return Response({'Session correctly deleted'},
                                status.HTTP_200_OK)
            else:
                return Response({'Session was not deleted'},
                                status.HTTP_200_OK)
        except Exception:
            return Response(
                {'An unexpected error occurred'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
