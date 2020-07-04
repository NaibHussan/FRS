from django.urls import path
from posts import views
# SET THE NAMESPACE!
app_name = 'posts'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
]
