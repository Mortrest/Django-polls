from django.urls import path
from .views import *


urlpatterns = [
    path('',homePage, name = 'home'),
    path('<int:pk>/', vote, name = 'vote'),
    path('<int:pk>/results', resultsPage, name = 'results'),
    path('like/<int:pk>/', likeView, name = 'like'),
    path('register/',registerPage, name = 'register'),
    path('login/',loginPage, name = 'login'),
    path('logout/',logoutUser, name= 'logout'),
    path('detail/<int:pk>',detailPage, name= 'detail'),
    

]
