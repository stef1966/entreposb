from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('entrepotsb/', include('unites.urls')),
    path('admin/', admin.site.urls),
]
