from django.contrib import admin

# Register your models here.
from .models import Cracker
from .models import User

admin.site.register(Cracker)
admin.site.register(User)
