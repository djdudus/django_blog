from django.contrib import admin

from .models import Set, Brick, SetBricks

# Register your models here.
admin.site.register(Set)
admin.site.register(Brick)
admin.site.register(SetBricks)
