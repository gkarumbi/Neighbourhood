from . import views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('', views.index, name='index'),
    url('register/', views.signup, name='signup'),
    url('account/', include('django.contrib.auth.urls')),
]