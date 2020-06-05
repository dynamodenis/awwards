from django.contrib import admin
from .models import Project

admin.site.site_header='AwwardMe Admin'
admin.site.site_title='AwwardMe Admin Dashboard'
# Register your models here.
admin.site.register(Project)