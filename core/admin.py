from django.contrib import admin

from core.models.doctor import Doctor, Profession, Position

# Register your models here.


admin.site.register(Doctor)
admin.site.register(Profession)
admin.site.register(Position)
