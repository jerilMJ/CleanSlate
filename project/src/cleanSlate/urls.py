"""cleanSlate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from joblist.views import jobs_list_view
from pages.views import home_view, contact_view, about_view, login_view, signup_view
from report.views import report_place

urlpatterns = [
    path('', home_view, name="home"),
    path('home/', home_view, name="home"),
    path('contact/', contact_view, name="contact"),
    path('about/', about_view, name="about"),
    path('jobs/', jobs_list_view, name="jobs"),
    path('report/', report_place, name="report"),
    path('login/', login_view, name="login"),
    path('signup/', signup_view, name="signup"),
    path('admin/', admin.site.urls),
]
