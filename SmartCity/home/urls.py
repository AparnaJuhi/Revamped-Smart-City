
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index,name='index'),
    path("about", views.about,name='about'),
    path("contact", views.contact,name='contact'),
    path("signin",views.signin,name='signin'),
    path("postsign",views.postsign,name='postsign'),
    path("logout",views.logout,name='logout'),
    path(r"^signup",views.signup,name='signup'),

]
