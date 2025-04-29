from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index',views.index,name="index"),
    path('contact',views.contact,name='contact'),
    path('login',views.loginUser,name='login'),
    path('signup',views.signupUser,name='signup'),
    path('logout',views.logoutUser,name='logout'),
    path('review',views.review,name='review'),
    path('profile',views.profile,name='profile'),
    path('package',views.package,name='package'),
]