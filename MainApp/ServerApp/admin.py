from django.contrib import admin
from .models import PhysicalServers, VirtualServers


admin.site.register(PhysicalServers)
admin.site.register(VirtualServers)
