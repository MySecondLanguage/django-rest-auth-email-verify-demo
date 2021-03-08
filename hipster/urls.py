"""hipster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include, re_path

from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authtoken import views

from rest_auth.views import PasswordResetConfirmView
from allauth.account.views import AccountInactiveView



from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Wejhaat API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('rest-auth/', include('rest_auth.urls')), #for forget password api endpoint
    path('rest-auth/registration/', include('rest_auth.registration.urls')), # handle the error: https://github.com/iMerica/dj-rest-auth/issues/9  # https://django-allauth.readthedocs.io/en/latest/configuration.html
    path("account-inactive/", AccountInactiveView.as_view(), name="account_inactive"),
    re_path(r'^rest-auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),

     path("api/docs/", include_docs_urls(title="Tourism API")),
     path('doc/', schema_view),
]
