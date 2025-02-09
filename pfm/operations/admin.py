from django.contrib import admin
from .models import Operation

@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ('wallet', 'date', 'time', 'amount', 'direction', 'description')  # Поля, которые будут отображаться в списке
    list_filter = ('direction', 'wallet')  # Фильтры для списка
    search_fields = ('description', 'wallet__name')  # Поля для поиска
    ordering = ('-date',)  # Сортировка по умолчанию (по дате в обратном порядке)