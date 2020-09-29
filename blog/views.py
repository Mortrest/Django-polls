from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages


def resultsPage(request, pk):
    question = Question.objects.get(pk=pk)


    context = {
        'question':question
    }
    return render(request,'blog/results.html',context)





def homePage(request):
    question = Question.objects.all()
    latest_question_list = Question.objects.order_by('datePublished')[:5]


    context = {
        'question':latest_question_list
    }
    return render(request,'blog/home.html',context)



def vote(request, pk):
    questionSelected = Question.objects.get(pk=pk)
    try:
        choiceSelected = questionSelected.choices_set.get(pk=request.POST['choice'])

    #Ok she inja
    except(KeyError,Choice.DoesNotExist):
        return render(request, homePage)

    else:
        choiceSelected.vote += 1
        choiceSelected.save()
        return redirect('home')