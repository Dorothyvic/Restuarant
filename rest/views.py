from django.shortcuts import render
from .models import Contact, Subscribe
from django.core.mail import send_mail


def index(request):
    if request.method == 'POST':
        email = request.POST['email']

        user_email = Subscribe.objects.create(email=email)
        return render(request, 'contact-done.html', {'email': email})

    else:
        return render(request, 'index.html', {})


def about(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        user = Contact.objects.create(name=name, email=email, subject=subject, message=message)

        send_mail(
            subject,
            message,
            email,
            ['dorothyvic24@gmail.com'],
        )

        return render(request, 'contact-done.html', {'name': name})
    else:
        return render(request, 'about.html', {})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        user = Contact.objects.create(name=name, email=email, subject=subject, message=message)

        send_mail(
            subject,
            message,
            email,
            ['dorothyvic24@gmail.com'],
        )

        return render(request, 'contact-done.html', {'name': name})
    else:
        return render(request, 'contact.html', {})