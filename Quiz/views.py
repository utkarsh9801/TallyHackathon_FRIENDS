from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *
from .Serializers import scoreSerializer
from django.http import HttpResponse
import datetime


# Create your views here.
def ss(request):
    if request.method == 'POST':
        print(request.POST)
        return redirect('home')
    else:
        return render(request, 'Quiz/ss.html')

def adminPanel(request):
    if request.user.is_staff:
        return render(request, 'Quiz/adminPanel.html')
    else:
        return redirect('home')


def home(request):
    scores = 0

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse("User is not logged in :)")
        print(request.POST, "hello sanchit")
        questions = QuesModel.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score / (total * 10) * 100
        scores = int(percent)
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }

        Data = {
            'user': request.user.username,
            'score': scores,
            'isTestGiven': True,
        }
        Serializer = scoreSerializer(data=Data)
        if Serializer.is_valid():
            print("valid")
            Serializer.save()
        else:
            print("error command", Serializer.errors)
            return HttpResponse(Serializer.errors)
        return render(request, 'Quiz/result.html', context)
    else:
        questions = QuesModel.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'Quiz/home.html', context)


def addQuestion(request):
    if request.user.is_staff:
        form = addQuestionform()
        if (request.method == 'POST'):
            form = addQuestionform(request.POST)
            if (form.is_valid()):
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'Quiz/addQuestion.html', context)
    else:
        return redirect('home')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = createuserform()
        if request.method == 'POST':
            form = createuserform(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
        context = {
            'form': form,
        }
        return render(request, 'Quiz/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        context = {}
        return render(request, 'Quiz/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('/')
