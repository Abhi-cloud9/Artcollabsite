from django.contrib import admin

from .models import UserProfile, Skillset, Contact
admin.site.register(UserProfile)
admin.site.register(Skillset)
admin.site.register(Contact)
