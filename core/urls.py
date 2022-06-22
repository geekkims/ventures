from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('accounts.urls')),
    path('', include('website.urls')),
    path('jobs/', include('jobs.urls')),
]
