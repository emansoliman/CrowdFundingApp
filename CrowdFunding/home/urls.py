
from django.urls import path , include
from . import views


urlpatterns = [
    path('',  views.index , name='index'),
    path('new_category',  views.new_category , name='new_category'),
    path('show',  views.show , name='show'),
    path('my_projects',  views.my_projects , name='my_projects'),
]


