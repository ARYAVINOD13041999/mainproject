from django.contrib import admin

from momo_app import models

# Register your models here.

admin.site.register(models.customer)
admin.site.register(models.worker)
admin.site.register(models.complaint)
admin.site.register(models.add)
admin.site.register(models.schedule)
admin.site.register(models.appointment)