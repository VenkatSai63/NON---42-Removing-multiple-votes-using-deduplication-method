from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('index.html', views.index, name="index"),
    path('signin/', views.Login, name="Login"),
    path('login/', views.Login, name="login_clean"),
    path('auth/login/', views.Login, name="auth_login"),
    path('Login.html', views.Login, name="Login_legacy"),
    path('signup/', views.Register, name="Register"),
    path('register/', views.Register, name="register_clean"),
    path('Register.html', views.Register, name="Register_legacy"),
    path('Signup', views.Signup, name="Signup"),
    path('UserLogin', views.UserLogin, name="UserLogin"),
    path('Dashboard.html', views.Dashboard, name="Dashboard"),
    path('dashboard/', views.Dashboard, name="dashboard_clean"),
    path('DemoLogin', views.DemoLogin, name="DemoLogin"),
    path('ViewVoters.html', views.ViewVoters, name="ViewVoters"),
    path('ViewVotersAction', views.ViewVotersAction, name="ViewVotersAction"),
    path('AddNewVoter.html', views.AddNewVoter, name="AddNewVoter"),
    path('AddNewVoterAction', views.AddNewVoterAction, name="AddNewVoterAction"),
    path('RemoveDuplicate', views.RemoveDuplicate, name="RemoveDuplicate"),
    path('Download', views.Download, name="Download"),
]