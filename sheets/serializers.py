from rest_framework import serializers

from .models import Cell


class CellSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cell
        fields = ('coordinates', 'value')