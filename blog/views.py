from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
import json

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account Was Created '+ username)
            return redirect ('login')
    context = {
        'form':form
    }
    return render(request, 'blog/register.html',context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is wrong')
    context = {
    }
    return render(request, 'blog/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')		



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


def detailPage(request, pk):
    question = Question.objects.get(id=pk)

    context = {
        'question':question
    }
    return render(request,'blog/detail.html',context)




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

def likeView(request, pk):
    textList = UserClass.objects.get(id=request.user.id).text
    likeList = []
    for i in range(len(textList)):
        likeList.append(textList[i])
    # questionSelected = Question.objects.get(pk=pk)
    # q = questionSelected.likeStatus
    # print(q)
    # if q == 0:
        
    #     q = 1
    #     print('q ==',q,'shod')
    #     questionSelected.save()
    #     print('q',q,'save shod')
    #     w = questionSelected.likes 
    #     w += 1
    #     questionSelected.save()
    #     print('Az avali raftam')
    #     return redirect('home')
    # else:
    #     q = 0
    #     questionSelected.save()
    #     w = questionSelected.likes 
    #     w -= 1
    #     questionSelected.save()
    #     print('Az Dovomi Raftam')
    #     context = {
    #         'question':Question.objects.all()
    #     }
    #     return render(request,'blog/home.html',context)

    questionSelected = Question.objects.get(pk=pk)
    userSelected = UserClass.objects.get(id=request.user.id)
    try:
        q = questionSelected
        w = userSelected
    #Ok she inja
    except:
        print('hello')
    else:
        if str(pk) in likeList:
        # if q.likeStatus == 0:
        #     q.likeStatus = 1
        #     q.save()
            likeList.remove(str(pk))
            a = ''.join(likeList)
            w.text = a
            w.save()
            q.likes -= 1
            q.save()
        else:
            likeList.append(str(pk))
            a = ''.join(likeList)
            w.text = a
            w.save()
            q.likes += 1
            q.save()

        return redirect('home')
