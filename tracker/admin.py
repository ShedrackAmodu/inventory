from django.contrib import admin
from .models import Activity

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'priority', 'is_completed', 'start_time', 'end_time')
    list_filter = ('category', 'priority', 'is_completed', 'created_at')
    search_fields = ('title', 'description')
