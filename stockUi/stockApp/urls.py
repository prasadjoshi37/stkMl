from django.conf.urls import url
from stockApp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[

    url(r'^$',views.index,name='index'),

]
