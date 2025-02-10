from django.urls import path
from . import views

urlpatterns = [
   path('register/', views.register, name='register'),
   path('login/', views.login_auth, name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('show-users/', views.show_users, name='showUsers'),
   path('delete-user/<int:id>', views.delete_user, name='delete-user'),
   path('edit-user/<int:id>', views.edit_user, name='edit-user'),
]