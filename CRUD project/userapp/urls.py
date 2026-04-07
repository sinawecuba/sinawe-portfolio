from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user-list'),            # List all users
    path('Add/', views.AddUser, name='add-user'),          # Add new user
    path('Edit/<int:id>/', views.EditUser, name='edit-user'),   # Edit user by ID
    path('Delete/<int:eid>/', views.DeleteUser, name='delete-user'),  # Delete user by ID
    path('View/<int:eid>/', views.ViewUser, name='view-user'),       # View user details
]
