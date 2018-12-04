from django.contrib import admin
from .models import HostGroup,Hosts,AnsiMod,ModArgs
# Register your models here.
for item in [HostGroup,Hosts,AnsiMod,ModArgs]:
    admin.site.register(item)
