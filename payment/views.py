import stripe
import os
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from job_listing.views import show_listing

def charge(request):
    if request.method == 'GET':
        amount = 1000
        key = os.environ["STRIPE_PUBLISHABLE_KEY"] #1
        return render(request, 'charge.html',{
            'key' : key,
            'amount' : amount
        })
    else:
        stripe.api_key = os.environ["STRIPE_SECRET_KEY"]  #2
        charge = stripe.Charge.create(
            amount=1000,
            currency='sgd',
            description='Job Advert Charge',
            source=request.POST['stripeToken']
        )
    # return
    return redirect(show_listing)
