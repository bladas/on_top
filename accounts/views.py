from djoser.serializers import UserSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class UserDetailView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
