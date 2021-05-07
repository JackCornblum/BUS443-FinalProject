from django.contrib import admin
from student.models import Studentinfo, Courseinfo, Dashboardinfo, Enrollmentinfo

# Register your models here.


admin.site.register(Studentinfo)
admin.site.register(Courseinfo)
admin.site.register(Dashboardinfo)
admin.site.register(Enrollmentinfo)