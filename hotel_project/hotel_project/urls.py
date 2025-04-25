# Add this to your main project urls.py file
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Your existing URL patterns
    path('admin/', admin.site.urls),
    # Other URL patterns...
]

# Add these lines at the end of the file to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
