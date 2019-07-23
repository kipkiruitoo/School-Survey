from django.shortcuts import render
from rest_framework import generics,permissions
from .models import User
from django.contrib.auth import authenticate,login
from rest_framework_jwt.settings import api_settings
from .serializers import TokenSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import status

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class RegisterUsersView(generics.CreateAPIView):
    """
    POST auth/register/
    """
    permission_classes = (permissions.AllowAny,)

    def post(self,request,*args,**kwargs):
        username = request.data.get("username","")
        password = request.data.get("password","")
        email = request.data.get("email","")
        role = request.data.get("role","Admin")
        if not username and not password and not email:
            return Response(
                data={
                    "message":"username,password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username,password=password,email=email,role=role
        )
        querys = User.objects.filter(email=email ).values()
        print(querys)
        return Response(data={
            "message": "Account created successfully",
            "user_details": querys[0]
        },
            status=status.HTTP_201_CREATED)

class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """
    # This permission class will overide the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)
    # serializer_class = SurveySerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        email = request.data.get("email", "")
        password = request.data.get("password", "")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            querys = User.objects.filter(email=email ).values()
            print(querys[0]['role'])
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()
            return Response(data={
                'message':'Login successful',
                'userRole':querys[0]['role'],
                'token': serializer.data['token']
            },status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class UserListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def retrieve(self, request):
        user = User.objects.all()
        
        serializer = UserSerializer(user)
        print(serializer)
        return Response(user,status=status.HTTP_200_OK)

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET users/:id/
    PUT users/:id/
    DELETE users/:id/
    """
    # permission_classes = (permissions.IsAuthenticated)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self,request,*args,**kwargs):
        try:
            a_user = self.queryset.get(pk=kwargs['pk'])
            return Response(UserSerializer(a_user).data)
        except User.DoesNotExist:
            return Response(
                data={
                    "message":"User with id: {} does not exist".format(kwargs['pk'])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self,request,*args,**kwargs):
        email = request.data.get("email","")
        password = request.data.get("password","")
        username = request.data.get("username","")
        if not email and not username:
            return Response(
                data={
                    "message":"A user must have a email and a username"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            a_user = self.queryset.get(pk=kwargs['pk'])
            serializer = UserSerializer()
            updated_user = serializer.update(a_user,request.data)
            return Response(UserSerializer(updated_user).data)
        except User.DoesNotExist:
            return Response(
                data={
                    "message":"user with id:{} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

        def delete(self,request,*args,**kwargs):
            try:
                a_user = self.queryset.get(pk=kwargs["pk"])
                a_user.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except User.DoesNotExist:
                return Response(
                    data={
                        "message":"User with id:{} does not exist".format(kwargs["pk"])
                    },
                    status=status.HTTP_404_NOT_FOUND
                )



# class SchoolViewSet(viewsets.ModelViewSet):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer
    
#     def get_permissions(self):
#         permission_classes = []
#         if self.action == 'create':
#             permission_classes = [AllowAny]
#         elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
#             permission_classes = [IsLoggedInUserOrAdmin]
#         elif self.action == 'list' or self.action == 'destroy':
#             permission_classes = [IsAdminUser]
#         return [permission() for permission in permission_classes]