from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'


router = DefaultRouter()
router.register('post', views.PostModelViewSet, basename='post')
router.register('category',views.CategoryModelSetView, basename='category')

urlpatterns = router.urls
urlpatterns = [
    path('post/', views.PostListView.as_view(), name = 'post-list'),
    # path('post/<int:id>/', views.PostDetailView.as_view(), name="post-detail"),
    # path('post/', views.PostViewSet.as_view({'get':"list", "post":"create"}), name = 'post-list'),
    # path('post/<int:id>/', views.PostViewSet.as_view({"get":"retrieve", "put":"update", "patch":"partial_update", "delete":"destroy"}), name='post-detail'),
    # path('', include(router.urls)),
]
