from . import views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('', views.index, name='index'),
    # url(r'^logout/$',views.logout, {"next_page":'/'},name="logout"),
    url('register/', views.signup, name='signup'),
    url('account/', include('django.contrib.auth.urls')),
    url('all-hoods/',views.neighbourhoods,name='hood'),
    url('new-hood/', views.create_neighbourhood, name='new-hood'),
    
]