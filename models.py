from django.db import models
from django.contrib.auth.models import User

class Attendance(models.Model):
    STATUS_CHOICES = (
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
        ('LATE', 'Late'),
        ('EXCUSED', 'Excused'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PRESENT')
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.status}"

from django.db import models
from django.contrib.auth.models import User

class SalaryDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2)
    leave_days = models.IntegerField()
    total_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        self.total_salary = self.salary + self.bonus - (self.salary / 30 * self.leave_days)
        super().save(*args, **kwargs)

    def str(self):
        return f"Salary details for {self.user.username}"

class IssueReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_description = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Issue reported by {self.user.username} on {self.reported_at}"
class Registration(models.Model):
    Uname = models.CharField(max_length=100)
    Fname = models.CharField(max_length=100)
    Mname = models.CharField(max_length=100)
    present_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    joining = models.DateField()
    position = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return f"Registration for {self.Uname}"
    

    from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='documents/')

    def str(self):
        return self.title
    

    from django.db import models

class EmployeeFeedback(models.Model):
    employee_id = models.CharField(max_length=50, blank=True, null=True)
    company_benefits_opinion = models.TextField(blank=True, null=True)
    improvement_ideas = models.TextField(blank=True, null=True)
    satisfaction_rating = models.IntegerField()
    anonymous_feedback = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        if self.anonymous_feedback:
            return "Feedback from Anonymous"
        else:
            return f"Feedback from Employee {self.employee_id}"
        
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'Message from {self.name}'
