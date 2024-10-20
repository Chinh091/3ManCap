"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# myproject/urls.py
# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from _3mancap import views  # Import the dashboard view

urlpatterns = [
    path('admin/', admin.site.urls),
    # Remove the _3mancap prefix and serve the dashboard directly from root URL
    path('', views.dashboard, name='home'),  # Serve the dashboard at the root
    # Optionally, include other URLs if necessary
    # path('_3mancap/', include('_3mancap.urls')),
    path('', include('_3mancap.urls')),
]
