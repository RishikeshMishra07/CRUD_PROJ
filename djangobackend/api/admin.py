from django.contrib import admin
from .models import students

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = [ 'stuid', 'stuname', 'stuemail', 'stuage'] 

admin.site.register(students, StudentAdmin)