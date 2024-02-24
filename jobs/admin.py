from django.contrib import admin
from . models import *

admin.site.register(Applicant)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Application)

# Register your models here.
