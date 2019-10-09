from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from app.models import FibonacciTest


admin.site.register(FibonacciTest)