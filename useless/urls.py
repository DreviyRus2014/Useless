from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('passkeys/', include('passkeys.urls')),
    path('auth/login', views.login, name="login"),
    path('auth/addpasskey', views.add_passkey, name="addpasskey"),
    path('auth/register',views.register, name="register"),
    path('auth/logout', views.logout, name="logout"),
    re_path('^$', views.home, name='home')
]
