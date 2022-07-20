from rest_framework import generics
from DRF.blog.models import Post
from DRF.blog_api.serializers import PostSerializer
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions, BasePermission, SAFE_METHODS


class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

name = 'testteasdasdasdst'