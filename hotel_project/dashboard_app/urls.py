# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.dashboard_home, name='dashboard_home'),
#     path('reservations/', views.manage_reservations, name='manage_reservations'),
#     path('rooms/', views.manage_rooms, name='manage_rooms'),
#     path('users/', views.manage_users, name='manage_users'),
#     path('users/add/', views.add_user, name='add_user'),
#     path('users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
#     path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
# ]


from django.urls import path
from . import views


urlpatterns = [

    path('', views.DashboardHomeView.as_view(), name='dashboard_home'),
    # User management URLs
    path('users/', views.UserListView.as_view(), name='users'),
    path('users/add/', views.UserCreateView.as_view(), name='user_add'),
    path('users/<int:pk>/edit/', views.UserUpdateView.as_view(), name='user_edit'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    # Room management URLs
    path('rooms/', views.RoomListView.as_view(), name='rooms'),
    path('rooms/add/', views.RoomCreateView.as_view(), name='room_add'),
    path('rooms/<int:pk>/edit/', views.RoomUpdateView.as_view(), name='room_edit'),
    path('rooms/<int:pk>/delete/', views.RoomDeleteView.as_view(), name='room_delete'),
    # Reservation management URL
    # Add other URLs as needed
]

