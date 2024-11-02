from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Teatr)
admin.site.register(Janre)
admin.site.register(Film)
admin.site.register(Show)
admin.site.register(Order)