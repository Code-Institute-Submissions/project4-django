from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from .forms import Newjob, Editjob
from .models import job_database
# from payment.views import charge

# Create your views here.

def show_listing(request):
    jobs = job_database.objects.all()
    return render(request, 'show_listing.html', {
        'data':jobs
    })

def add_listing(request):
    if request.method == "POST":
        new_listing = Newjob(request.POST)
        if new_listing.is_valid():
            instance = new_listing.save(commit=False)
            instance.user = request.user
            instance.save()
        return redirect(show_listing)
        
    else : 
        new_listing = Newjob()
        return render(request, 'add_listing.html',{
            'form' : new_listing
            })

def edit_listing(request, id):
    job = get_object_or_404(job_database, pk=id)
    
    if request.method == "POST":
        edit_job = Editjob(request.POST, instance=job)
        if edit_job.is_valid():
            edit_job.user = request.user
            edit_job.save()
            return redirect(show_listing)
    else:
        edit_job = Editjob(instance=job)
        return render(request, 'edit_listing.html',{
            'form': edit_job
        })
    return render(request, 'edit_listing.html')
    
def confirm_delete(request, id):
    job = get_object_or_404(job_database, pk=id)
    return render(request, 'confirm_delete.html', {
        'job' : job
    })
    
def delete_job(request, id):
    job_database.objects.filter(pk=id).delete()
    return redirect(show_listing)

