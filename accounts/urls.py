from django.urls import path
from .views import Login_View, Home, Logout_view

urlpatterns = [
    path('', Home, name='home'),
    path('login/', Login_View, name='login'),
    path('logout/', Logout_view, name='logout')

]