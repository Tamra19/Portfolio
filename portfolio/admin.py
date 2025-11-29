from django.contrib import admin
from .models import Project, ProjectImage
# Register your models here.

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1   #number of empty image upload fields (what is the meaning of extra)

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)