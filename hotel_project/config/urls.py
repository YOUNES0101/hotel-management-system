from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotel_app.urls')),
    path('dashboard/', include('dashboard_app.urls')),
]
