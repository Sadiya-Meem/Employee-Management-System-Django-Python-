#myapp_admin
from django.contrib import admin
import django.apps
from django.contrib import admin
from .models import Attendance 
admin.site.register(Attendance)

from django.contrib import admin
from .models import SalaryDetail, IssueReport

@admin.register(SalaryDetail)
class SalaryDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'salary', 'bonus', 'leave_days', 'total_salary')

@admin.register(IssueReport)
class IssueReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'issue_description', 'reported_at')

    from django.contrib import admin
from .models import Document
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

    from django.contrib import admin
from .models import EmployeeFeedback

admin.site.register(EmployeeFeedback)

from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email')
    actions = ['send_response']
admin.site.register(ContactMessage, ContactMessageAdmin)

