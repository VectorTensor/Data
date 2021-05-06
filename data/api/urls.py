from django.urls import path,include
from .views import index,delete


urlpatterns=[path('',index.as_view()),
        path('del',delete)]





