from django.contrib import admin

from .models import STSRun, STSRunPlayer

# Register your models here.
admin.site.register(STSRun)
admin.site.register(STSRunPlayer)