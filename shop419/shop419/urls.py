"""
URL configuration for shop419 project.

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
from django.contrib import admin
from django.urls import path, include

# adding this line to support hosting of static files
from django.conf.urls.static  import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mainapp.urls')),
    path('cart/',include('cart.urls')),
    path('orders/',include('orders.urls')),
    path('payments/',include('payments.urls')),
    path('auth/',include('authentication.urls')),
    path('auth/',include('django.contrib.auth.urls')), # to include the paths configured in the app,here
]
# the following line allows us to use the given media path during development
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)