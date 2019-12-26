from django.shortcuts import render

# Create your views here.

def show_listing(request):
    return render(request, 'show_listing.html')

def add_listing(request):
    return render(request, 'add_listing.html')

def edit_listing(request):
    return render(request, 'edit_listing.html')

def confirm_delete(request):
    return render(request, 'confirm_delete.html')
