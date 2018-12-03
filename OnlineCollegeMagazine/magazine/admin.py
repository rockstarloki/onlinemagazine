from django.contrib import admin
from .models import FacultyRegistration, UserRegistration
from .models import StudentRegistration
from .models import ModeratorRegistration


admin.site.register(FacultyRegistration)
admin.site.register(StudentRegistration)
admin.site.register(ModeratorRegistration)
admin.site.register(UserRegistration)
