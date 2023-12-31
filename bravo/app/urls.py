from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('',home,name='home'),
    path('search/', search_posts, name='search_posts'),
    path('services/<int:pk>/',services,name='services'),
    path('services/room/<int:pk>/',createRoom,name='room'),
    path('login/',login,name='login'),
    path('logout/',logoutV,name='logout'),
    path('profile/<int:pk>/',profile,name='profile'),
    path('create-seller/<int:pk>/',createSeller,name='createSeller'),
    path('dasboard/<int:pk>/',dashboard,name='dashboard'),
    path('view-room/<str:pk>/',viewRoom,name='viewRoom'),
    path('register/', register, name='register'),
    path('upload/<str:pk>/', upload_file, name='upload_file'),
    path('download/<int:pk>/', download_file, name='download'),
    path('profile-update/<int:pk>/', updateProfile, name='updateProfile'),
    path('delete-banner/<int:pk>/', deleteBanner, name='deleteBanner'),
    path('banner-details/<int:pk>/', PostDetailView.as_view(), name='viewDetails'),


]
