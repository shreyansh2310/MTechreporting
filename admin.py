from django.contrib import admin
from .models import institute_db, pending_db , pending_db1 , pending_db2

# Register your models here.

admin.site.register(institute_db)

admin.site.register(pending_db)

admin.site.register(pending_db1)

admin.site.register(pending_db2)