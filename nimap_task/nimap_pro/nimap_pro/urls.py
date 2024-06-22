"""
URL configuration for nimap_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myapp.views import ClientView,ClientDetailView,ProjectDetailView,ProjectView,UserProjectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/',ClientView.as_view(),name='client_list'),
    path('client/<int:pk>',ClientDetailView.as_view(),name='client_details'),
    path('projects/',ProjectView.as_view(),name='project_list'),
    path('project/<int:pk>',ProjectDetailView.as_view(),name='project_details'),
    path('user-projects/',UserProjectView.as_view(),name='user_project'),
]
