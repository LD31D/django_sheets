from django.urls import path

from . import views


urlpatterns = [
	path('logout/', views.LogoutView.as_view(), name='logout'),
	
	path('login/', views.CustomLoginView.as_view(), name='login'),
]
