"""barbershop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from admin_notification.views import check_notification_view
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .routers import router

admin.site.site_header = 'BarberShop - Administração'
admin.site.index_title = 'Administração'
admin.site.site_title = 'Barbershop'

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('check/notification', check_notification_view, name="check_notifications"),
]
urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
