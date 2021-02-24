from rest_framework import viewsets

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Sheet, Cell
from .serializers import CellsSerializer


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
	serializer_class = CellsSerializer

	def get_queryset(self):
		sheet = get_object_or_404(
				Sheet, 
				key=self.kwargs.get("sheet_key")
			)

		queryset = sheet.cells

		return queryset
