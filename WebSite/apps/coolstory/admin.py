from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Person, PersonHistory


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	list_display = ['id','person_name', 'person_author', 'person_photo']

	class Meta:
		model = Person

@admin.register(PersonHistory)
class HistoryAdmin(admin.ModelAdmin):
	list_display = ['id','person_add', 'history_title', 'history_author', 'history_date']
	
	class Meta:
		model = PersonHistory