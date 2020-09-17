from django.contrib import admin
from .models  import Transaction_table,User_table
# Register your models here.
admin.site.register(User_table)
admin.site.register(Transaction_table)