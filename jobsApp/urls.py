from django.contrib import admin
from django.urls import path 
from . import views
#from . import api 

app_name = 'jobsApp '
urlpatterns = [
    path('', views.job_list, name= "job_list"), # path('path_name/', include('app_name.urls'))
    path('add-job', views.add_job, name='add-job'),
    path('job-detail/<str:slug>', views.job_detail, name='job_detail'),
    
    # API function based views
    #path('api/jobs',api.job_list_api , name='job_list_api'),
    #path('api/jobs/<int:id>',api.job_detail_api , name='job_detail_api'),
    
    # API class based views
    #path('api/v2/jobs',api.JobListApi.as_view() , name='job_list_api'),
    #path('api/v2/jobs/<int:id>',api.JobDetail.as_view() , name='job_detail_api'),
    
]