from django.contrib import admin

from main.models import Resident, City


class ResidentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'patronymic', 'city']


admin.site.register(City)
admin.site.register(Resident, ResidentAdmin)
