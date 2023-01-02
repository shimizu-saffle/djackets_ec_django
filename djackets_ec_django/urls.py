from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djackets.urls')),
    path('api/', include('djackets.urls.authtoken')),
]
