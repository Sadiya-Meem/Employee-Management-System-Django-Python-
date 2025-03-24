# myapp/views.py
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import AttendanceForm, IssueReportForm, RegistrationForm # Removed PaymentMethodForm
from .models import Attendance, SalaryDetail, IssueReport,ContactMessage  # Removed PaymentMethod
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def help(request):
    return render(request, 'help.html')

def contactform(request):
    return render(request, 'contactform.html')

def service(request):
    return render(request, 'service.html')

def regis(request):
    return render(request, 'regis.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return HttpResponse("Your password and confirm password are not the same")
        else:
            data = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            data.save()
            return redirect('login_view')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def forgot(request):
    return render(request, 'forgot.html')

def attendance_view(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendsheet')  # Redirect to the attendance sheet after submission
    else:
        form = AttendanceForm()
    return render(request, 'attendance.html', {'form': form})

def attendsheet_view(request):
    attendances = Attendance.objects.all()
    return render(request, 'attendsheet.html', {'attendances': attendances})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def salary_view(request):
    user = request.user
    salary_detail = SalaryDetail.objects.filter(user=user).first()

    if request.method == 'POST':
        issue_form = IssueReportForm(request.POST)
        if issue_form.is_valid():
            issue = issue_form.save(commit=False)
            issue.user = user
            issue.save()
            return redirect('salary')  # Ensure this matches your URL name for the salary view
    else:
        issue_form = IssueReportForm()

    context = {
        'salary_detail': salary_detail,
        'issue_form': issue_form,
    }

    return render(request, 'salary.html', context)

def holidays_view(request):
    return render(request, 'holidays.html')


# Other views as per your existing implementation

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            father_name = form.cleaned_data['father_name']
            mother_name = form.cleaned_data['mother_name']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            joining_date = form.cleaned_data['joining_date']
            
            # Assuming you have a model to save this data
            # Save to database or use as needed
            
            # Redirect to personal profile page with data
            return redirect('personalinfo', name=name, father_name=father_name,
                            mother_name=mother_name, address=address,
                            phone=phone, email=email, joining_date=joining_date)
    else:
        form = RegistrationForm()
    return render(request, 'regis.html', {'form': form})

def personalinfo(request, name, father_name, mother_name, address, phone, email, joining_date):
    context = {
        'name': name,
        'father_name': father_name,
        'mother_name': mother_name,
        'address': address,
        'phone': phone,
        'email': email,
        'joining_date': joining_date,
    }
    return render(request, 'personalinfo.html', context)

# Other views continued as per your existing implementation

from django.shortcuts import render

def leave_view(request):
    # Your view logic here
    return render(request, 'leave.html')


from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document.html', {'documents': documents})

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})
def document_view(request):
    # Your view logic here
    return render(request, 'document.html')

from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import EmployeeFeedback

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submitted_successfully')  # Replace with your success URL
    else:
        form = FeedbackForm()
    
    return render(request, 'analytics.html', {'form': form})

def analytics(request):
    # Your view logic here
    return render(request, 'analytics.html')
from django.shortcuts import render

def submitted_successfully_view(request):
    # Your view logic here
    return render(request, 'submitted_successfully.html')  # Adjust as per your actual implementation

def set_password(request):
    if request.method == 'POST':
        username = request.POST['username']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if new_password != confirm_password:
            messages.error(request, "New passwords do not match.")
            return redirect('set_password')

        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            messages.success(request, "Password has been set successfully. You can now log in with your new password.")
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, "Username does not exist.")
            return redirect('set_password')

    return render(request, 'set_password.html')

def saveEnquiry(request):
    return render(request,'contactform.html')

def contactform(request):
    return render(request, 'contactform.html')


def tasks(request):
    return render(request, 'tasks.html')


#contact function
def save_enquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save the message to the database
        ContactMessage.objects.create(name=name, email=email, message=message)
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contactform')  # Replace 'contact' with the name of your contact page URL pattern
    return render(request, 'contactform.html')