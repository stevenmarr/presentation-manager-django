from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Presentation

class PresentationAdminSite(AdminSite):
    site_header = 'Presentation Manager'

admin_site = PresentationAdminSite(name='presentationadmin')

admin_site.register(Presentation)

admin.site.register(Presentation)