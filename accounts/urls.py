from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('profile/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('profile/password/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('profile/delete/', views.UserDeleteView.as_view(), name='user_delete'),  
]