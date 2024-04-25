from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.users.api.urls')),
    path('api/', include('apps.spends.api_spends.urls')),
]