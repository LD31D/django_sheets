from django.urls import path
from django.urls import include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'cells', views.CellsViewSet, basename='cutareadel')


urlpatterns = [
	path('<sheet_key>/', views.SheetView.as_view(), name='view'),
	path('<sheet_key>/', include(router.urls)),
]
