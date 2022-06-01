from django.contrib import admin

# Register your models here.
from .models import Session
admin.site.register(Session)

from .models import Billing
admin.site.register(Billing)
