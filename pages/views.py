from django.shortcuts import render

from .forms import ContactForm


def home(request):
    return render(request, 'pages/about_me.html');

def contact(request):
    form =  ContactForm() #Create an instance of the ContactForm Class
    
    return render(request, 'pages/contact.html', {
        'form': form
        });


# Create your views here.
