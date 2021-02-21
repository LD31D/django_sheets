from django.urls import path

from . import views


urlpatterns = [
	path('<sheet_key>/', views.SheetView.as_view(), name='view'),
]
