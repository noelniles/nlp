from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django import forms

class gcdform(forms.Form):
    x = forms.CharField(max_length=100)
    y = forms.CharField(max_length=100)

def gcd(request):
    if request.method == 'POST':         # If the form has been submitted...

        form = gcdform(request.POST)     # A form bound to the POST data

        if form.is_valid():              # All validation rules pass
            # Process the data in form.cleaned_data
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            gcd = euclids_algorithm(int(x), int(y))
            message = "the gcd(%s, %s) = %s" % (x, y, gcd)
            return HttpResponse(message)
    else:
        form = gcdform() # An unbound form

    return render(request, 'gcd_form.html', {
        'form': form,
    })

def euclids_algorithm(x, y):                                                                 
    if x < y:                                                                  
        return euclids_algorithm(y, x)                                                       
    elif x % y == 0:                                                           
        return y                                                               
    elif y == 0:                                                               
        return x                                                               
    else:                                                                      
        return euclids_algorithm(y, x % y)
