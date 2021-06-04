from django.contrib import admin
from .models import Todo, ToDoProgrammingContest

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
class TodoPCAdmin(admin.ModelAdmin):
    list_display = ('platform', 'staring_time', 'completed')    

# Register your models here.

admin.site.register(Todo, TodoAdmin)
admin.site.register(ToDoProgrammingContest, TodoPCAdmin)