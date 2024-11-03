from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('name/', include('calsiapp.urls')),
    path('admin/', admin.site.urls),
]
