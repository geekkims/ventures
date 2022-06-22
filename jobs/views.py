from django.shortcuts import render

from jobs.forms import PostJobForm
from . import models
from django.db import models
import uuid
from .models import Company, Industry,Categories





# Create your views here.


def jobs(request):
    return render(request,"frontend/jobs/job-listing.html")






def postjob(request):
    industry = Industry.objects.filter(active=True)
    categories = Categories.objects.filter(active=True)
    
    form = PostJobForm()
    if request.method == "POST":
        form = PostJobForm(request.POST, request.FILES)
        if form.is_valid():    
            print("PostJobForm --------------- PostJobForm IS VALID", request.POST.get('title'), request.POST.get('company'))
            form.save()
        else:
            print("PostJobForm --------------- PostJobForm ERRORS", form.errors)
    context ={
        "form": form,
        "industry": industry,
        "categories": categories
    }
    return render(request, "frontend/jobs/post-job.html", context)










