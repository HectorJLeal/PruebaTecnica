from django.contrib import admin
from .models import Base
from .models import Users
# Register your models here.

admin.site.register(Base)
admin.site.register(Users)