from django.urls import path, include
from . import views
from django.views.generic import TemplateView, RedirectView

app_name = 'blog'

urlpatterns = [
    # path('fbv-index', views.indexView, name = 'fbv-index'),
    path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
    path('go-to-index', RedirectView.as_view(url = 'cbv-index'), name='go-to-index'),
    path('post/', views.ListView.as_view(), name = 'post'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name = 'post-detail'),
    path('post/create/', views.PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('accounts/profile/', views.ListView.as_view(), name='login'),
    path('api/v1/', include('blog.api.v1.urls')),
]
