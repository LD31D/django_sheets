from rest_framework import serializers

from .models import Cell


class CellsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cell
        fields = ('coordinates', 'value')