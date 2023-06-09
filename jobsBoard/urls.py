"""
URL configuration for jobApsBoard project.

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
from django.urls import path, include
# from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobsApp.urls')),

    
    # always the accounts before the admin because the admin will overwrite the accounts if its not in the beginning
    #path('accounts/', include('django.contrib.auth.urls')), # a build in feature from django
    #path('accounts/', include('accounts.urls',namespace='accounts')),
    #path('admin/', admin.site.urls), 
    #path('jobApp/', include('jobApp.urls', namespace='jobApps')), # path('path_name/', include('app_name.urls'))
    #path('contact-us/', include('contact.urls',namespace='contact')),
    
    # Django Rest Framework
    #path('api-auth/', include('rest_framework.urls'))
    ]


# for adding the static files in the frontend to the settings
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# for adding the static files (images, ...) by the user to the settings
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 