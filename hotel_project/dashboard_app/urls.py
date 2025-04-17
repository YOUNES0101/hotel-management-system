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
    path('', views.dashboard, name='dashboard'),
    path('manange_reservations/', views.manage_reservations, name='manage_reservations'),
    path('settings/', views.settings, name='settings'),
    path('manange_users/', views.manage_users, name='manage_users'),
    path('add_user/', views.add_user_view, name='add_user'),
]
