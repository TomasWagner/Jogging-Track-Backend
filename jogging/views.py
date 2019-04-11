from rest_framework import viewsets
from jogging.models import Record, User
from jogging.serializers import UserSerializer, RecordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class RecordViewSet(viewsets.ModelViewSet):
    serializer_class = RecordSerializer 
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        records = []
        role = self.request.user.userprofile.role

        if role == 'User':
            records = Record.objects.filter(user_id=self.request.user.id)

        elif role == 'Admin':
            records = Record.objects.all()
#        role = user.userprfile
        return records

    def get_object(self):
        print(self.kwargs['pk'])
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        #self.check_object_permissions(self.request, obj)
        return obj


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,]

class SignupView(APIView):
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        print(user_serializer)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TokenVerify(APIView):
    def post(self, request):
    	user = User(username=request.user)
    	user_serializer = UserSerializer(user)
    	return Response(user_serializer.data, status=status.HTTP_400_BAD_REQUEST)
