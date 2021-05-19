from django.shortcuts import render
from .models import Contact


# Create your views here.

def handle_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_num = request.POST['phone']
        message = request.POST['message']

        contact = Contact(name=name, email=email, phone=phone_num, message=message)
        contact.save()

    return render(request, 'contact/contact.html', {})
