from rest_framework.generics import CreateAPIView
from .serializers import UserRegisterSerializer
from accounts.models import User
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

# view for creating a new user object
class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
    authentication_classes = []

    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=HTTP_201_CREATED)