from django.urls import path
from ems_app import views  # Ensure 'ems_app' is the correct name of your app

urlpatterns = [
    path('home/', views.home, name="home"),  # Use 'home' as the name for the home path
    path('about/', views.about, name="about"),  # Optional: add a name for 'about'
    path('add_data/', views.add_data, name="add_data"),
    path('register/', views.register, name="register"),
     path('', views.login_view , name="login"),
    path('logout/', views.logout_view , name="logout"),
    path('contact/', views.contact_view, name='contact'),
path('update_data/<int:id>/', views.update_data , name="update_data"),
    path('delete_data/<int:id>/', views.delete_data , name="delete_data"),

]

    

