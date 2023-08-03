from django.urls import path, include
from . import views
from django.views.generic import TemplateView


app_name = 'app'

urlpatterns = [
    path('api/v1/', include('app.api.v1.urls')),
    path('', include('django.contrib.auth.urls'))
]
