from django.contrib import admin
from .models import Wallet

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'currency', 'user')  # Поля, которые будут отображаться в списке
    list_filter = ('currency', 'user')  # Фильтры для списка
    search_fields = ('name', 'user__username')  # Поля для поиска
    ordering = ('name',)  # Сортировка по умолчанию