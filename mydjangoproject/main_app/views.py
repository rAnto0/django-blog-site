from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import Posts, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import PostsSerializer


class PostsAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class PostsAPIList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PostsAPIListPagination


class PostsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )


class PostsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (IsAdminOrReadOnly,)
