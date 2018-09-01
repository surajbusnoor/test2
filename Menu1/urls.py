from django.conf.urls import url
from Menu1 import views
urlpatterns = [
    url(r'^Style1$',views.style1_1),
    url(r'^Index1$',views.index1),
]