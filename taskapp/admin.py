from django.contrib import admin

# Register your models here.
# from adminfilters.multiselect import UnionFieldListFilter
# from advanced_filters.admin import AdminAdvancedFiltersMixin

from django.contrib import admin
from django.db import models
from django.forms import Textarea
# from django.utils.translation import ugettext_lazy as _
# from .models import Task, Item
from taskapp.models import Task, Item

# from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter


class ItemInline(admin.TabularInline):
    model = Item
    extra = 0


class TaskAdmin(admin.ModelAdmin):
    list_display = ['number', 'title', 'user', 'partner', 'created_at', 'deadline', 'priority', 'state']
    list_display_links = ['number', 'title']
    search_fields = ['id', 'title', 'item__item_description',
                     'user__username', 'user__first_name', 'user__last_name',
                     'partner__name', 'partner__email']

    # list_filter = ('user', 'state', 'priority', 'deadline')
    advanced_filter_fields = (
        'user__username',
        'partner__name',
        'state',
        'priority',
        'deadline',
        'created_at',
        'created_by',
        'title',
        'description',
        'resolution',
    )
    # ordering = ['created_at']
    readonly_fields = ('created_at', 'last_modified', 'created_by',)
    # autocomplete_fields = ['user', 'partner']


    inlines = [ItemInline]

    # formfield_overrides = {
    #     models.TextField: {
    #         'widget': Textarea(attrs={'rows': 4, 'cols': 32})
    #     }
    # }

    def user_name(self, obj):
        return obj.user.username

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj is None:
            fieldsets = (  # Creation form
                (None, {'fields': ('title', ('user', 'partner'), 'deadline', ('state', 'priority'), 'description')}),
            )
        return fieldsets



admin.site.register(Task, TaskAdmin)
