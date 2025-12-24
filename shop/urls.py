from django.contrib import admin
from django.urls import path, include
from products.views import *
from django.conf.urls.static import static
from shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
