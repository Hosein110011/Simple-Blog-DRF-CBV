from django.urls import path, include






urlpatterns = [
    path('', include('app.api.v1.urls.accounts')),
    path('profile/', include('app.api.v1.urls.profiles')),

]
