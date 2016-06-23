from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^createFriend', views.createFriend, name = 'createFriend'),
    url(r'^mergeIdentities', views.Bonding, name = 'party_time'),

]
