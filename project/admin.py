from django.contrib import admin
from .models import Project,Votes

admin.site.site_header='AwwardMe Admin'
admin.site.site_title='AwwardMe Admin Dashboard'


class VotesInLine(admin.TabularInline):
    model=Votes
    extra=3
    
class ProjectInLine(admin.ModelAdmin):
    fieldsets=[
        (None,{'fields':['user']}),
        (None,{'fields':['image']}),
        (None,{'fields':['title']}),
        (None,{'fields':['description']}),
    ]
    inlines=[VotesInLine]

# Register your models here.
admin.site.register(Project,ProjectInLine)