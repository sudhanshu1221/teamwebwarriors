from django.shortcuts import render
from .models import Feedback


# Create your views here.

def handle_feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        rating = request.POST['rating']
        feedback = request.POST['feedback']

        feedback = Feedback(name=name, email=email, rating=rating, feedback=feedback)
        feedback.save()

    return render(request, 'feedback/feedback.html', {})
