from django.contrib import admin
from .models import Job, Category, Apply

# Register your models here.

class jobAdmin(admin.ModelAdmin):
    list_display = ['title', 'job_type', 'vacancy', 'salary', 'experience']
    list_filter = ['job_type', 'experience']


admin.site.register(Job, jobAdmin)
admin.site.register(Category)
admin.site.register(Apply)