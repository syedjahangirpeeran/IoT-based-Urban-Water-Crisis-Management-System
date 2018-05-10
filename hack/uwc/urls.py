from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.home,name="home"),
    url(r'^map/$',views.map,name="map"),
    url(r'^turbidity/$',views.turbidity,name="turbidity"),
    url(r'^turgraph/$',views.turgraph,name="turgraph"),
    url(r'^flowrate/$',views.flowrate,name="flowrate"),
    url(r'^moisture/$',views.moisture,name="moisture"),
    url(r'^levelrange/$',views.levelrange,name="levelrange"),
    url(r'^sensortable/$', views.sensortable, name="sensortable"),
    url(r'^passage/$', views.passage, name="passage"),
    url(r'^map2/$', views.map2, name="map2"),
    url(r'^(?P<sensor1>[0-9]+.[0-9]+)/(?P<sensor2>[0-9]+.?[0-9]*)/(?P<sensor3>[0-9]+.?[0-9]*)/(?P<sensor4>[0-9]+.?[0-9]*)/(?P<sensor5>[0-9]+.?[0-9]*)/(?P<sensor6>[0-9]+.?[0-9]*)/(?P<time>[A-Za-z][A-Za-z][A-Za-z] [A-Za-z][A-Za-z][A-Za-z] [012]?[0-9] [012]?[0-9]:[0-5][0-9]:[0-5][0-9] [0-9][0-9][0-9][0-9])/$',views.Display,name="Display"),
]