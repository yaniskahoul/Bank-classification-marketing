from django.urls import path # Import du module Path  
from .views import * # Import de notre fichier views
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", home_view, name="home"),
    path('predict/', views.predict, name='predict'),
    path('logout/', LogoutView.as_view(next_page='home', template_name='logout.html'), name='logout'),
    path('login/', views.user_login, name='login')
    
]