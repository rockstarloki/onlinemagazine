from django.contrib import admin
from .models import UserRegistration
from .models import HomeFashion
from .models import HomeTechnology
from .models import HomeHealth
from .models import ModeratorRegistration
from .models import ModHealth

admin.site.register(ModeratorRegistration)
admin.site.register(UserRegistration)
admin.site.register(HomeFashion)
admin.site.register(HomeTechnology)
admin.site.register(HomeHealth)
admin.site.register(ModHealth)
