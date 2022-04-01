from django.urls import path

app_name = 'mainapp'

import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.index, name='index'),
]