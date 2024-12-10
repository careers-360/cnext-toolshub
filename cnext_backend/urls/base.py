"""
URL configuration for cnext_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from .cms_api_urls import urlpatterns as cms_api_urls
from .rp_api_urls import urlpatterns as rp_api_urls
from .college_compare_urls import urlpatterns as college_compare_urls


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += cms_api_urls

# Static and Media URls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += rp_api_urls
urlpatterns+=college_compare_urls
