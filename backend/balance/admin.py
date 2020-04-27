from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Car)
admin.site.register(Ride)
admin.site.register(Refuel)
admin.site.register(Transaction)
