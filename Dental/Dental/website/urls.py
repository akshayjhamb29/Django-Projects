
from django.urls import path
from . import views
#import views from inside of this directory

urlpatterns = [
	path('',views.home, name="home"),
	path('contact.html',views.contact, name="contact"),
]
