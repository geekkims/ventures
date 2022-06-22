from django.contrib import admin

from jobs.models import Categories, Company, Industry, Jobs

# Register your models here.

admin.site.register([Industry,Company,Categories,Jobs])