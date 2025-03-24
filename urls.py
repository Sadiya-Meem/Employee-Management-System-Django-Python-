from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import feedback_view
from .views import register, personalinfo
from .views import salary_view
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('help/', views.help, name='help'),
    path('contactform/', views.contactform, name='contactform'),
    path('saveenquiry/', views.save_enquiry,name='saveenquiry'),
    path('service/', views.service, name='service'),
    path('regis/', views.regis, name='regis'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login_view'),
    path('set_password/', views.set_password, name='set_password'),
    path('forgot/', views.forgot, name='forgot'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('salary/', views.salary_view, name='salary'),
    path('holidays',views.holidays_view, name='holidays'),
    path('attendance/', views.attendance_view, name='attendance'),
    path('attendsheet/', views.attendsheet_view, name='attendsheet'),
    path('documents/', views.document_list, name='document_list'),
    path('upload/', views.upload_document, name='upload_document'),
    path('analytics/', views.feedback_view, name='analytics'),
    path('analytics/', views.analytics, name='analytics'),
    path('submitted_successfully/', views.submitted_successfully_view, name='submitted_successfully'),
    path('document/', views.document_view, name='document'),
    path('register/', views.register, name='register'),
    path('leave/', views.leave_view, name='leave'),
    path('tasks/', views.tasks, name='tasks'),
    path('personal-info/', views.personalinfo, name='personal_info'),
    path('personalinfo/<str:name>/<str:father_name>/<str:mother_name>/<str:address>/<str:phone>/<str:email>/<str:joining_date>/', views.personalinfo, name='personalinfo')
    
]





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

