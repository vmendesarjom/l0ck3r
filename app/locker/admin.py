from django.contrib import admin

# Register your models here.

from .models import Projector, Reserve, Slot

admin.site.register(Projector)
admin.site.register(Reserve)
admin.site.register(Slot)