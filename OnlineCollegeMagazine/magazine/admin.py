from django.contrib import admin
from .models import UserRegistration
from .models import ModeratorRegistration

admin.site.register(ModeratorRegistration)
admin.site.register(UserRegistration)
