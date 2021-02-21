from django import forms

from sheets.models import Sheet


class SheetForm(forms.ModelForm):

    class Meta:
        model = Sheet
        fields = ('name', )
        # labels = {
        # 	'body': 'Your Comment: '
        # }
        