from django.contrib import admin
from .models import create_user_profile, City, Profile

# Register your models here.
#admin.site.register(create_user_profile)
admin.site.register(City)
admin.site.register(Profile)