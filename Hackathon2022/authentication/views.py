from django.contrib.auth import authenticate, login, logout
from django.contrib.sites import requests
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
import re
from bs4 import BeautifulSoup
import requests


# Create your views here.

def homes(request):
    return render(request, 'authentication/index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username taken, please input another username")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered")
            return redirect('home')

        if len(username) > 20:
            messages.error(request, "Username must be under 10 characters")

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, 'Your account has been successfully created')

        # Welcome email

        subject = 'Welcome to boilermake - Django login'
        message = 'Hello ' + myuser.first_name + '!!\n' + 'Welcome to boilermake2022!\n' + \
                  'Thank you for visiting our website \n We have also sent you a confirmation email\n ' \
                  'please confirm your email\n Thank you!'
        # from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, to_list, fail_silently=True)

        return redirect('signin')

    return render(request, 'authentication/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'authentication/index.html', {'fname': fname})

        else:
            messages.error(request, 'Bad Credentials')
            return redirect('home')

    return render(request, 'authentication/signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')

def stats(request):
    r = requests.get('https://www.sports-reference.com/cbb/conferences/big-ten/2020-schedule.html')
    soup = BeautifulSoup(r.content, 'html.parser')
    text = soup.get_text()
    list1 = []
    for line in text.split("\n"):
        if len(re.findall("[0-9]+$", line)) > 0:
            if len(re.findall("\w+,\s\w+\s", line)):
                if len(line.split(", ")) == 3:
                    list1.append(line.split(", ")[2])
    list2 = []
    for i in list1:
        word = re.findall("[a-z\s]+", i.lower())
        print(word)
        num = re.findall("[0-9]+", i)
        dict1 = {}
        dict1["year"] = num[0]
        dict1["team1"] = word[0]
        dict1["team1score"] = num[1]
        dict1["team2"] = word[1]
        dict1["team2score"] = num[2]
        list2.append(dict1)
    #print(list2)
    return render(request, "authentication/stats.html", {'content': list2})


def wisconsin(request):
    list1 = static()
    for i in list1:
        if i["name"] == "wisconsin":
            return render(request, "authentication/wisconsin.html", {'content': i})


def illinois(request):
    list1 = static()
    for i in list1:
        if i["name"] == "illinois":
            return render(request, "authentication/illinois.html", {'content': i})


def ohio_state(request):
    list1 = static()
    for i in list1:
        if i["name"] == "ohio state":
            return render(request, "authentication/ohio_state.html", {'content': i})


def michigan_state(request):
    list1 = static()
    for i in list1:
        if i["name"] == "michigan state":
            return render(request, "authentication/michigan_state.html", {'content': i})


def rutgers(request):
    list1 = static()
    for i in list1:
        if i["name"] == "rutgers":
            return render(request, "authentication/rutgers.html", {'content': i})


def indiana(request):
    list1 = static()
    for i in list1:
        if i["name"] == "indiana":
            return render(request, "authentication/indiana.html", {'content': i})


def purdue(request):
    list1 = static()
    for i in list1:
        if i["name"] == "purdue":
            return render(request, "authentication/purdue.html", {'content': i})


def iowa(request):
    list1 = static()
    for i in list1:
        if i["name"] == "iowa":
            return render(request, "authentication/iowa.html", {'content': i})


def penn_state(request):
    list1 = static()
    for i in list1:
        if i["name"] == "penn_state":
            return render(request, "authentication/penn_state.html", {'content': i})


def michigan(request):
    list1 = static()
    for i in list1:
        if i["name"] == "michigan":
            return render(request, "authentication/michigan.html", {'content': i})


def northwestern(request):
    list1 = static()
    for i in list1:
        if i["name"] == "northwestern":
            return render(request, "authentication/northwestern.html", {'content': i})


def maryland(request):
    list1 = static()
    for i in list1:
        if i["name"] == "maryland":
            return render(request, "authentication/maryland.html", {'content': i})


def minnesota(request):
    list1 = static()
    for i in list1:
        if i["name"] == "minnesota":
            return render(request, "authentication/minnesota.html", {'content': i})


def nebraska(request):
    list1 = static()
    for i in list1:
        if i["name"] == "nebraska":
            return render(request, "authentication/nebraska.html", {'content': i})


def static():
    r = requests.get('https://www.sports-reference.com/cbb/conferences/big-ten/2022.html')
    soup = BeautifulSoup(r.content, 'html.parser')
    text = soup.get_text()
    list1 = []
    for line in text.split("\n"):
        if len(re.findall("[0-9]+$", line)) > 0:
            if len(re.findall("[0-9]\w", line)):
                if len(re.findall("\/", line)) > 0:
                    break;
                else:
                    if len(re.findall("[0-9][a-z]", line.lower())) > 0:
                        dict1 = {}
                        num = re.findall("[0-9]+", line)
                        word = re.findall("[a-z\s]+", line.lower())
                        dict1["ranking"] = num[0]
                        print(word[0])
                        dict1["name"] = word[0]
                        # print(line)
                        # print(num)
                        wl = num[2][3:]
                        if len(wl) == 2:
                            dict1["win"] = wl[0]
                            dict1["loss"] = wl[1]
                            # print("win " + wl[0])
                            # print("loss " + wl[1])
                        elif wl[0] == '1':
                            dict1["win"] = wl[0:2]
                            dict1["loss"] = wl[2]
                            # print("win " + wl[0:2])
                            # print("loss " + wl[2])
                        else:
                            dict1["win"] = wl[0]
                            dict1["loss"] = wl[1:]
                            # print("win " + wl[0])
                            # print("loss " + wl[1:])
                        list1.append(dict1)
    return list1
