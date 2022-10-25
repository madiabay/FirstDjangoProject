from django.contrib import admin
# from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin

from .models import Rubric, Article

# Register your models here.
#class Rubric(admin.ModelAdmin):
#    list_display = ('name', 'title')
#    list_display_links = ('name', 'title')
#    search_fields = ('title',)

# admin.site.register(Rubric, MPTTModelAdmin)
admin.site.register(
    Rubric,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(Article)