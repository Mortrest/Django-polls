from django.urls import path
from .views import *


urlpatterns = [
    path('',homePage, name = 'home'),
    path('<int:pk>/', vote, name = 'vote'),
    path('<int:pk>/results', resultsPage, name = 'results'),


    

]
