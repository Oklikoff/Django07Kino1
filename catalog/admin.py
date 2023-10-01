from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Animal)
admin.site.register(Client)
admin.site.register(Veterinarian)
admin.site.register(Appointment)