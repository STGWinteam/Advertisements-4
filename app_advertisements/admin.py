from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'negotiable', 'created_date', 'last_updated_date')
    list_filter = ('price', 'negotiable', 'created')
    actions = ['make_negotiable_as_false', 'make_negotiable_as_true']
    fieldsets = (
        ('Общее', {
            'fields': ['title', 'description'],
            'classes': ['collapse']
        }),
        ('Финансы', {
            'fields': ['price', 'negotiable'],
            'classes': ['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_negotiable_as_false(self, request, queryset):
        queryset.update(negotiable=False)

    @admin.action(description='Добавить возозможность торга')
    def make_negotiable_as_true(self, request, queryset):
        queryset.update(negotiable=True)

admin.site.register(Advertisement, AdvertisementAdmin)
