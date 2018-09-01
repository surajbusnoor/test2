from django.conf.urls import url
from formUser import views

urlpatterns = [
url(r'^user_forms$',views.usrForm),
url(r'^index$',views.index),
]