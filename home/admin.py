from django.contrib import admin
from .models import Category, Videos, Subcribe, SubscribeHistory, TopUpBalance, BalanceHistory,PaymentSystem


@admin.register(Videos)
class VideoAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['category', 'name', 'seasons', 'part']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Subcribe)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'month']

@admin.register(SubscribeHistory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'active_started_date', 'active_finished_date']


@admin.register(TopUpBalance)
class TopUpBalanceAdmin(admin.ModelAdmin):
    list_display = ['cost', 'user']


admin.site.register(BalanceHistory)
admin.site.register(PaymentSystem)
