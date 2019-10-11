from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .forms import UserCreationForm
from django.shortcuts import render, redirect
from cronJob.models import CronJob
import requests


def home(request):
    return render(request, 'home.html', {})


def index(request):
    if request.method == "POST":
        # titel, adresse
        title = request.POST.get("title")
        url = request.POST.get("http")

        # login
        userName = request.POST.get("benutzername")
        password = request.POST.get("passwort")

        # set time and date
        schedule = calcSchedule(request)

        # messages
        messageFail = checkTrue(request.POST.get("fehlgeschlagen"))
        messageSuccess = checkTrue(request.POST.get("erfolgreich"))
        messageTooMuchFailures = checkTrue(request.POST.get("deaktiviert"))

        if schedule == 'x':
            messages.error(request, "!! Ausführung: Eine Option muss ausgewählt sein !!")
            return render(request, 'crone.html', {})

        # save
        saveAnswer = checkTrue(request.POST.get("speichern"))

        print(title, url, userName, password, messageFail, messageSuccess,
              messageTooMuchFailures, saveAnswer)

        if title:
            obj = CronJob.objects.create \
                (title=title,
                 url=url,
                 userName=userName,
                 password=password,
                 schedule=schedule,
                 messageFail=messageFail,
                 messageSuccess=messageSuccess,
                 messageTooMuchFailures=messageTooMuchFailures,
                 saveAnswer=saveAnswer)
            obj.save()
            messages.success(request, 'Erfolgreich gespeichert')

        return render(request, 'crone.html', {})
    else:
        return render(request, 'crone.html', {})


def checkTrue(cb):
    return (cb == "True")


def calcSchedule(request):
    if (request.POST.get("ausführung", "") == "1"):
        result = "*/" + request.POST.get("minute", "") + " * * * *"
        return result
    elif (request.POST.get("ausführung", "") == "2"):
        result = request.POST.get("tagStunde", "") + " " + request.POST.get("tagMinute", "") + " * * *"
        return result
    elif (request.POST.get("ausführung", "") == "3"):
        result = request.POST.get("monatTag", "") + " " + request.POST.get("monatStunde",
                                                                           "") + " " + request.POST.get(
            "monatMinute", "") + " * *"
        return result
    else:
        return 'x'

def userLogin(request):
    userForm = AuthenticationForm()
    if request.method == "POST":
        userForm = AuthenticationForm(data=request.POST)
        if userForm.is_valid():
            username = userForm.cleaned_data['username']
            password = userForm.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
    return render(request, 'login.html', {'userForm': userForm})


def userLogout(request):
    logout(request)
    return redirect(reverse('homepage'))


def userAuthentification(request):
    authentificationForm = UserCreationForm()
    if request.method == "POST":
        authentificationForm = UserCreationForm(data=request.POST)
        if authentificationForm.is_valid():
            authentificationForm.save()
            username = authentificationForm.cleaned_data['username']
            password = authentificationForm.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)

    return render(request, 'authentification.html', {'authentificationForm': authentificationForm})


def testFunction(request):
    from cronJob.models import CronJob

    URL = "http://127.0.0.1:8000/index"

    PARAMS = {'title': '123456',
              'http': 'www.google.com',
              'benutzername': 'Test',
              'passwort': 'testpassword123',
              'ausführung': '2',
              'tagStunde': '16',
              'tagMinute': '15',
              'fehlgeschlagen': True,
              'speichern': True
              }

    requests.post(url=URL, params=PARAMS)

    # db auslesen
    success = 'Falset'
    entrys = CronJob.objects.all()
    for entry in entrys:
        if entry.title == '123456':
            success = 'True'
            break

    if success:
        print("Test erfolgreich.")
    else:
        print("Test failed")

    return render(request, 'test.html'), {'success': success}
