"""VacancyWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path
from django.conf.urls import url
from .views import ArticleYearArchiveView
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('vacancy', views.vacancy, name='vacancy'),
    path('tender', views.tender, name='tender'),
    path('advert', views.advert, name='advert'),
    path('news', views.news, name='news'),
    path('tender/<str:date>/', views.date, name='date'),
    path('search', views.search, name='search'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[-\w]+)/$', ArticleYearArchiveView.as_view(), name="article_year_archive"),
]
