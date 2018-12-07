from django.contrib import admin
from .models import UserRegistration
from .models import Fashion
from .models import Technology
from .models import Health
from .models import ModeratorRegistration

admin.site.register(ModeratorRegistration)
admin.site.register(UserRegistration)
admin.site.register(Fashion)
admin.site.register(Technology)
admin.site.register(Health)
