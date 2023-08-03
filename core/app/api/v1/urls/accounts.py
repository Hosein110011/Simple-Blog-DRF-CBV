from django.urls import path, include
from ..views import (RegistrationApiView, ChangePasswordApiView, TestEmailSend
                   , CustomDiscardAuthToken,CustomObtainAuthToken, CustomTokenObtainPairView)
from rest_framework_simplejwt.views import (
                                            TokenRefreshView,TokenVerifyView
                                            )






urlpatterns = [
    # registration
    path('registratoin/', RegistrationApiView.as_view(), name='registration'),
    
    # login token
    path('token/login/', CustomObtainAuthToken.as_view(), name = 'token-login'),
    path('token/logout/', CustomDiscardAuthToken.as_view(), name='token-logout'),
    
    path('test-email' ,TestEmailSend.as_view(), name='test-email'),
    
    # activation
    # path('activation/confirm/', ),

    # resend activation
    #path('activation/resend/'),

    # change password
    path('change-password/', ChangePasswordApiView.as_view(), name='change-password'),
    
    # reset password
    
    # login jwt
    # path('jwt/create/', TokenObtainPairView.as_view(), name="jwt-create"),
    path('jwt/create/', CustomTokenObtainPairView.as_view(), name="jwt-create"),
    path('jwt/refresh/', TokenRefreshView.as_view(), name="jwt-refresh"),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),

]
