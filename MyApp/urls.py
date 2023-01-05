from . import views
from MyApp import api
from django.urls import path

urlpatterns = [
 path('',views.home,name='home'),
 path('data/', views.dht11, name='Data'),
 path('data2', views.dht12, name='Data2'),
 path('data3', views.dht13, name='Data3'),
 path('api/list', api.Dlist, name='DHT11List'),
 path('api/post', api.Dhtviews.as_view(), name='DHT_post'),
]

