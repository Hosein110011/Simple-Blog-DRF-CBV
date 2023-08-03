from rest_framework.decorators import api_view,APIView, permission_classes, action
from rest_framework.response import Response
from ...models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.generics import (GenericAPIView, ListAPIView, ListCreateAPIView,
                                        RetrieveAPIView, RetrieveUpdateAPIView, 
                                        RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView)

from rest_framework import mixins
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination



# version 1
"""
@api_view(['POST','GET'])
@permission_classes([IsAdminUser])
def postList(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # else:
        #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
"""

# version 2

# class PostListView(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = PostSerializer(data = request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)


# version 3

# class PostListView(GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args,**kwargs)
        
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
   

# version 4

class PostListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

#---------------------------------------------------------------------------

# version 1

# @api_view(['GET','PUT', 'DELETE'])
# def PostDetail(request, id):
#     post = get_object_or_404(Post, id=id, status=True)
#     if request.method == 'GET':
#         # post = get_object_or_404(Post,id=id,status=True)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = PostSerializer(post, data=request.data)
#         if  serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response({"detail":"item successfully removed"},status=status.HTTP_204_NO_CONTENT)
            # try:
    #     post = Post.objects.get(pk=id)
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)
    # except Post.DoesNotExist:
    #     return Response({"detail":"post does not exist"}, status=status.HTTP_404_NOT_FOUND)


# version 2

# class PostDetailView(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer

#     def get(self, request, id):
#         post = get_object_or_404(Post, id=id, status=True)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)
    
#     def put(self, request, id):
#         post = get_object_or_404(Post, id=id, status=True)
#         serializer = self.serializer_class(post, data=request.data)
#         if  serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#     def delete(self, request, id):
#         post = get_object_or_404(Post, id=id, status=True)
#         post.delete()
#         return Response({"detail":"item successfully removed"},status=status.HTTP_204_NO_CONTENT)



# version 3

# class PostDetailView(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#     lookup_field = 'id'
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    

# version 4

# class PostDetailView(RetrieveUpdateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#     lookup_field = 'id'



# version 5

# class PostDetailView(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#     lookup_field = 'id'


########### version 5 ############

# class PostViewSet(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#     lookup_field = 'id'

#     def list(self, request):
#         seriaizer = self.serializer_class(self.queryset, many=True)
#         return Response(seriaizer.data)
    
#     def retrieve(self, request, id):
#         post_object = get_object_or_404(self.queryset, id=id)
#         serializer = self.serializer_class(post_object)
#         return Response(serializer.data)
    
#     def create(self, request):
#         pass

#     def update(self, request, id):
#         pass

#     def partial_update(self, request, id):
#         pass

#     def destroy(self, request, id):
#         pass


############# version 6 ###############

class PostModelViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['category', 'author', 'status']
    filterset_fields = {'category':["exact", 'in'], 'author':["exact"], 'status':["exact"]}
    search_fields = ['=title', 'content']
    ordering_fields = ['published_date']
    pagination_class = DefaultPagination

    @action(methods=["get"], detail=False)
    def get_ok(self, request):
        return Response({'detail':'ok'})



class CategoryModelSetView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'