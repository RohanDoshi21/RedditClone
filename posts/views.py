from xml.dom import ValidationErr
from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from posts.serializers import PostSerializer, VoteSerializer
from .models import Post, Vote
# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class VoteCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    # queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):  # defining query set here, name has to be the same
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)

    def perform_create(self, serializer):  # name has to be same perform_create
        if self.get_queryset().exists():
            raise ValidationError('You have already voted for this post :)')

        serializer.save(voter=self.request.user,
                        post=Post.objects.get(pk=self.kwargs['pk']))

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('You never voted...')
