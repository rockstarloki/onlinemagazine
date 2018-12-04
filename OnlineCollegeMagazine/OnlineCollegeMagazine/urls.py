"""OnlineCollegeMagazine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView

from magazine import views
from magazine.views import ur_update, validatepost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.openHome),


    path('openhome/',views.openHome),

    path('openuser/',views.openUser),
    path('userRegistertion/',views.showUserRegsitrationpage),
    path('userRegister/',views.userRegister),
    path('userLogin/',views.userLogin),
    path('logout/', views.openHome),
    path('ur_viewprofile/',views.ur_viewprofile),
    path('ur_updateprofile/',views.ur_updateprofile),
    path('ur_update/',ur_update),
    path('postarticle/',views.postarticle),

    path('openmoderator/',views.openModerator),
    path('newModerator/',views.showModeratorRegsitrationpage),
    path('moderatorRegister/',views.moderatorRegister),
    path('moderatorLogin/',views.moderatorLogin),
    path('logout/',views.openHome),
    path('mr_viewprofile/',views.mr_viewprofile),
    path('mr_updateprofile/',views.mr_updateprofile),
    path('mr_update/',views.mr_update),
    path('validatepost/',views.validatepost),


    path('magazine/',views.showmagazine)

]
