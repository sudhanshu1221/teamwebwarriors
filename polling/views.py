
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from polling.models import Question, Choice


def main_page(request):
    all_question_qs = Question.objects.all()
    context = {
        'question_list': all_question_qs,
    }

    return render(request, 'polling/main_page.html', context)


def details(request, ques_id):
    question_qs = Question.objects.filter(pk=ques_id)

    if question_qs:
        question = question_qs[0]

        # Fetching choices for this question
        choice_list = Choice.objects.filter(question=question)

        context = {
            "question": question,
            "choice_list": choice_list,
        }

        return render(request, "polling/details.html", context=context)
    else:
        response = "Question with id=" + str(id) + " not found."
        return HttpResponse(response)


def results(request, ques_id):
    question_qs = Question.objects.filter(pk=ques_id)

    if question_qs:
        question = question_qs.first()

        choice_list = Choice.objects.filter(question=question)

        context = {
            "question": question,
            "choice_list": choice_list,
        }

        return render(request, "polling/results.html", context=context)
    else:
        response = "Question with this id is not present."
        return HttpResponse(response)


def vote(request, ques_id):
    selected_choice_id = request.POST['choice']

    selected_choice_qs = Choice.objects.filter(pk=selected_choice_id)

    # Checking if choice with id=selected_choice_id exists or not
    if selected_choice_qs:
        selected_choice = selected_choice_qs[0]

        selected_choice.number_of_votes += 1

        selected_choice.save()

        print(reverse("Results", kwargs={"ques_id": ques_id}))

        return HttpResponseRedirect(reverse('Results', kwargs={'ques_id': ques_id}))
    else:
        response = "Choice with this id is not present."
        return HttpResponse(response)
