"""mymagazine URL Configuration

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
from magazine.views import ur_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.openHome),

    path('openhome/', views.openHome),
    path('openhomefashion/',views.openhomefashion),
    path('showhomefashion/',views.showhomefashion),

    path('openhometechnology/',views.openhometechnology),
    path('showhometech/',views.showhometech),

    path('openhomehealth/',views.openhomehealth),
    path('showhomehealth/',views.showhomehealth),

    path('logout/', views.openHome),

    path('aboutus/',views.aboutus),

    path('openmoderatorhome/',views.openmoderatorhome),
    path('openmoderator/', views.openModerator),
    path('newModerator/',views.showModeratorRegsitrationpage),
    path('moderatorLogin/',views.moderatorLogin),
    path('mr_viewprofile/', views.mr_viewprofile),
    path('mr_updateprofile/', views.mr_updateprofile),
    path('mr_update/', views.mr_update),
    path('validatepost/', views.validatepost),
    path('validate/',views.validate),
    path('sendmail/',views.sendmail),

    path('openmodfashion/',views.openmodfashion),
    path('showmodfashion/',views.showmodfashion),
    path('openmodtechnology/',views.openmodtechnology),
    path('showmodtech/',views.showmodtech),
    path('openmodhealth/',views.openmodhealth),
    path('showmodhealth/',views.showmodhealth),

    path('openuserhome/',views.openuserhome),
    path('openuser/',views.openUser),
    path('userRegistertion/',views.showUserRegsitrationpage),
    path('userRegister/',views.userRegister),
    path('userLogin/',views.userLogin),
    path('ur_viewprofile/',views.ur_viewprofile),
    path('ur_updateprofile/',views.ur_updateprofile),
    path('ur_update/',ur_update),
    path('postarticle/',views.postarticle),
    path('post/',views.post),

    path('openusertechnology/',views.openusertechnology),
    path('showusertech/',views.showusertech),

    path('openuserfashion/', views.openuserfashion),
    path('showuserfashion/',views.showuserfashion),

    path('openuserhealth/',views.openuserhealth),
    path('showuserhealth/',views.showuserhealth)




]
