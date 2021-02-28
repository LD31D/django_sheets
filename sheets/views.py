from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication 


from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Sheet, Cell
from .serializers import CellSerializer


class SheetView(LoginRequiredMixin, DetailView):
	template_name = 'sheets/sheet_view/index.html'

	def get_object(self, queryset=None):
		sheet = get_object_or_404(
				Sheet, 
				owner=self.request.user, 
				key=self.kwargs.get("sheet_key")
			)

		return sheet



class CellsViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = CellSerializer

	def get_queryset(self):
		sheet_obj = get_object_or_404(
				Sheet, 
				key=self.kwargs.get('sheet_key')
			)

		queryset = sheet_obj.cells

		return queryset


class CellViewSet(viewsets.ViewSet):
	serializer_class = CellSerializer
	authentication_classes = (BasicAuthentication, )


	def get(self, request, sheet_key, coordinates):
		sheet_obj = get_object_or_404(Sheet, key=sheet_key)
		cell_obj = get_object_or_404(sheet_obj.cells, coordinates=coordinates)

		serializer = self.serializer_class(cell_obj)
		return Response(serializer.data)

	def create_or_update(self, request, sheet_key, coordinates):
		sheet_obj = get_object_or_404(Sheet, key=sheet_key)

		cell_value = request.data['value']

		cell_obj, created = Cell.objects.update_or_create(
				coordinates=coordinates, 
				sheet=sheet_obj, 
				defaults={'value': cell_value}
			)

		if cell_value == "":
			cell_obj.delete()

		serializer = self.serializer_class(cell_obj)		
		return Response(serializer.data)
