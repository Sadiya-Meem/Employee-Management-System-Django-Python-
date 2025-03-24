# myapp/forms.py

from django import forms
from .models import IssueReport, Attendance,Registration

class IssueReportForm(forms.ModelForm):
    class Meta:
        model = IssueReport
        fields = ['user', 'issue_description']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['user', 'date', 'status', 'comments']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    father_name = forms.CharField(max_length=100)
    mother_name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()
    joining_date = forms.DateField()

from .models import Document 
class  DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'description', 'file']

        from django import forms
from .models import EmployeeFeedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = EmployeeFeedback
        fields = ['employee_id', 'company_benefits_opinion', 'improvement_ideas', 'satisfaction_rating', 'anonymous_feedback']