from django.contrib import admin
from .models import Chemical, Utilization, Usecase

# Register your models here.
admin.site.register(Chemical)
admin.site.register(Utilization)
admin.site.register(Usecase)