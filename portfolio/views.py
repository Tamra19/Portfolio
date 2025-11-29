from django.shortcuts import render, redirect
from .models import Project, Contact

#contact
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

def about(request):
    return render(request, 'portfolio/about.html')

def contact_me(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            #save to database
            contact_msg = form.save()
            
            #send email notification to yourself
            subject = f"New portfolio message from {contact_msg.name}"
            message = f"You have received a new message\n\nName: {contact_msg.name}\nEmail: {contact_msg.email}\nMessage: {contact_msg.message}"
            
            #Ensure EMAIL_HSOT_USER is set in settings.py
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER]     #send msg to yourself
            
            try:
                send_mail(subject, message, from_email, recipient_list)
            except Exception as e:
                #handling erros gracefully (log them in production)
                print(f"Email error: {e}")
            
            messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
            return redirect('contact')  #redirect to avoid re-submission on refresh
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})