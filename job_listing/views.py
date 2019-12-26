from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from .forms import Newjob
from .models import job_database

# Create your views here.

def show_listing(request):
    jobs = job_database.objects.all()
    return render(request, 'show_listing.html', {
        'data':jobs
    })

def add_listing(request):
    # if request.method == "POST":
    #     new_listing = Newjob(request.POST)
    #     if new_listing.is_valid():
    #         instance = new_listing.save(commit=False)
    #         instance.user = request.user
    #         instance.save()
    #     return redirect(show_listing)
        
    # else : 
    new_listing = Newjob()
    return render(request, 'add_listing.html',{
        'form' : new_listing
        })

def edit_listing(request):
    return render(request, 'edit_listing.html')

def confirm_delete(request):
    return render(request, 'confirm_delete.html')
