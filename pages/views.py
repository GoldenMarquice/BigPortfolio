from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from .forms import ContactForm


def home(request):
    return render(request, 'pages/about_me.html');

def contact(request):
    #When clicking send email button do this:

    if request.method == 'POST':
        form = ContactForm(request.POST) #Create an instance of the ContactForm Class

        if form.is_valid ():
        #Show a message in the terminal
            print('The form is valid.')

            #Get the data from the HTML template
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']

            html = render_to_string('pages/contact_template.html',{
                'name': name,
                'email': email,
                'content': content
            })

            #print each attribute to verify if we are getting the data!
            print(name,email,content, html)

            #use the template to send the email
            #send
            send_mail(subject, 'This is the message', 'noreply@something', ['usmcmarquice@gmail.com'], html_message=html)

            # Redirect to a success page or do something else
            return redirect('contact')  # You should define a 'success' URL in your Django app
            
        
        #Go back to the contact page
        #do not forget to import the redirect shortcut

#If we do not get a post request, just create an instance of the form
    else:
        form = ContactForm()


    #Render the form in the html template.
    return render(request, 'pages/contact.html', {
        'form': form
        });


# Create your views here.
