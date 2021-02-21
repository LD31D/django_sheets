from django.contrib import admin

from .models import Sheet


@admin.register(Sheet)
class SheetAdmin(admin.ModelAdmin):
	list_display = ('name', 'key', 'owner')
	readonly_fields = ('key', )
	search_fields = ('name', )
