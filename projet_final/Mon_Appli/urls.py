from django.urls import path # Import du module Path  
from .views import * # Import de notre fichier views
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", home_view, name="home"),
    path('predict/', views.predict, name='predict'),
    path('accounts/login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='login', template_name='registration/logout.html'), name='logout')

    
]