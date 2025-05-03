from django.contrib import admin
from django.urls import path, include
from django.conf import settings             # Import settings
from django.conf.urls.static import static # Import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotel_app.urls')), # Include your app's urls
    path('dashboard/', include('dashboard_app.urls')), # Assuming you have dashboard urls
    # Add other app urls if needed
]

# Add this block to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
