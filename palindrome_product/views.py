from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import itertools

class palindromeform(forms.Form):
    x = forms.IntegerField(max_value=10000000)
    y = forms.IntegerField(max_value=10000000)

def palindrome(request):
    if request.method == 'POST': # If the form has been submitted...
        form = palindromeform(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            prod = pp(x, y)
            return HttpResponse("the largest palindrome product is %s" % (prod))
    else:
        form = palindromeform() # An unbound form

    return render(request, 'palindrome_form.html', {
        'form': form,
    })

def pp(bot, top):                                                                      
    """return the largest palindrone product"""                                
    x = [i for i in range(bot, top)]    #the range of numbers to multiply        
                                                                               
    y = itertools.product(x, repeat=2)   #tuple of every pair                  
    z = [i[0] * i[1] for i in y]         #product of every pair                
                                                                               
    for i in sorted(set(z)):             #sort the products                    
        if str(i) == str(i)[::-1]:       #item is a palindrome                 
            pal = i
    return pal
