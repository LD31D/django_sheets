from django.urls import path

from . import views


urlpatterns = [
	path('', views.ArticleCreateView.as_view(), name='main'),
]
