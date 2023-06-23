from django.shortcuts import render
from .models import Job
from django.shortcuts import redirect, render
from django.urls import reverse


# https://docs.djangoproject.com/en/4.1/topics/pagination/
from django.core.paginator import Paginator


# decorator login required
from django.contrib.auth.decorators import login_required


# Apply Form
from .forms import ApplyForm , JobForm


# Filtration
from .Filters import JobFilter


# Model Queryset in Django
# https://docs.djangoproject.com/en/4.1/ref/models/querysets/


# Will Retrieve all jobs 
def job_list(request): 
    jobs = Job.objects.all()
    context = {"jobs": jobs,
    }
    
    # Filters
    myfilter = JobFilter(request.GET, queryset=jobs)
    jobs = myfilter.qs # qs == queryset
    
    # Pagination
    paginator = Paginator(jobs, 5) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'jobs': page_obj, 'myfilter' : myfilter} # templates name
    return render(request, 'job_list.html', context)


def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug) # will retrieve on job
    # job_detail = Job.object.filter() # will retrieve on job from a list according to some filtration


    # Django bootstrap:  https://django-bootstrap4.readthedocs.io/en/latest/quickstart.html
    if request.method=='POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
                    myform = form.save(commit=False)
                    myform.job = job_detail
                    myform.save()
                    print('Done')


    else:
        form = ApplyForm()

    context = {'job' : job_detail , 'form' : form}
    return render(request,'job_detail.html', context)

@login_required
def add_job(request):
    if request.method=='POST':
        #pass
        form = JobForm(request.POST , request.FILES) # request.FILES if theres any pic <form method="POST" enctype="multipart/form-data">
        if form.is_valid(): # to make sure the form is valid
            myform = form.save(commit=False) # save the form but not in the db because i need to add the person who added the job
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list')) # after saving redirect to the job list REVERSE takes the urls (project:app)


    else:
        form = JobForm()
    return render(request,'add_job.html', {'form': form})
