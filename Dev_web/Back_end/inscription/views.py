from django.shortcuts import render, redirect
from django.template import RequestContext

# Create your views here.
from .forms import NewUser




def inscription_form(request):
    form = NewUser(request.POST or None)
    if form.is_valid():
        form.save()
        #form = NewUser() 
        return redirect('connexion')
    context = {
        'form' : form 
    }

    return render(request, 'Pages/inscription.html', context)

