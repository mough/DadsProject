
from django.shortcuts import render, redirect
from forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.contrib import messages
from django.contrib.messages import get_messages

def home(request):
    return render(request, 'pages/home.html')  # (request, 'template_name', dictionary(optional))


def create(request):
    return render(request, 'pages/create.html')  # (request, 'template_name', dictionary(optional))


def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name', '')
            contact_email = request.POST.get(
                'contact_email', '')
            form_content = request.POST.get('content', '')
            # email the profile with the contact information
            template = get_template('pages/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content, })
            content = template.render(context)
            email = EmailMessage("New contact form submission",
                                 content,
                                 "Your website" +'<hi@weddinglovely.com>',
                                 ['youremail@gmail.com'],
                                 headers={'Reply-To': contact_email })
            email.send()
            #messages.add_message(request, messages.SUCCESS, 'Hello world.')
            messages.success(request, "Email sent successfully!")
            get_messages(request)
            return redirect('contact')
    return render(request, 'pages/contact.html', {'form': form_class})
