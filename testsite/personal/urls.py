from django.conf.urls import url
from . import views

app_name='personal'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^aboutme/', views.aboutme,name='aboutme')
]
