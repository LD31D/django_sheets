from django.urls import path
from django.urls import include

from . import views


urlpatterns = [
	path('<sheet_key>/', views.SheetView.as_view(), name='view'),

	path('<sheet_key>/api/cells/', views.CellsViewSet.as_view({'get': 'list'})),
	path(
			'<sheet_key>/api/cell/<coordinates>/', 
			views.CellViewSet.as_view({
					'get': 'get', 
					'post': 'create_or_update', 
					'put': 'create_or_update'
				})
		)
]
