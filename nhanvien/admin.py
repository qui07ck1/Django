from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import nhanvien
# Register your models here.



class nhanvien_Admin(admin.ModelAdmin):
    fieldsets = [('Information',{'fields':['emp_no','emp_name','sex','marry','position_name','grade_code','join_date','birth_date','address','telephone']})]
    list_display = ('emp_no','emp_name','grade_code','birth_date','address','telephone')
    search_fields=['emp_no']
    
    
    
    
    
admin.site.register(nhanvien, nhanvien_Admin)