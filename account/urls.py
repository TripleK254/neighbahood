from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register', views.register, name="register"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout', views.logout, name="logout"),
    path('blog', views.blog, name="blog"),
    path('add-business', views.add_business, name="add-business"),
    path('profile', views.profile, name="profile"),
    path('add-policestation', views.add_policestation, name="add-policestation"),
    path('add-health-center', views.add_health_center, name="add-health-center"),
    path('search', views.search, name="search"),
    path('verifyemail', views.verify_email, name="verifyemail"),
  
]