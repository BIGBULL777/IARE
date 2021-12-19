"""IARE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from CoviSafe import urls,views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('citizen_details', views.profileApi)



urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^apicitizen/',views.profileApi.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    url(r'^apilogin/',views.loginview.as_view()),
    url(r'apiregister/',views.registerView.as_view()),
    url(r'^apislots/',views.slots_view.as_view()),







    url(r'', include(router.urls)),
    url(r'get_jwt_token/', obtain_jwt_token), # GET JET TOKEN
    url(r'refresh_jwt_token/', refresh_jwt_token), # REFRESH JET TOKEN
    url(r'verify_jwt_token/', verify_jwt_token), # VERIFY JET TOKE


    # path('',include('CoviSafe.urls')),
    # path('api1',include('CoviSafe.urls')),
]
