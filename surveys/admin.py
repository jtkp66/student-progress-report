from django.contrib import admin
from .models import Survey


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'coordinator',
                    'stsurname', 'stname', 'date_posted', 'stcoord', 'is_complete',)
    list_display_links = ('id', 'coordinator')
    list_filter = ('stcoord', 'coordinator', 'is_complete')
    list_editable = ('is_complete',)
    search_fields = ('coordinator', 'stsurname', 'stname',
                     'sthost', 'is_complete', 'stcoord')
    list_per_page = 25


admin.site.register(Survey, SurveyAdmin)
