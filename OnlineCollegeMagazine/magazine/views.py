from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import ModeratorRegistration
from .models import  FacultyRegistration
from .models import StudentRegistration
from .models import UserRegistration

def openHome(request):
    type = "home"
    return render(request, "home.html", {"type": type})

def openUser(request):
    type = request.GET.get("type")
    return render(request,"home.html",{"type":type})


def openModerator(request):
    type = request.GET.get("type")
    return render(request, "home.html", {"type": type})

def showUserRegsitrationpage(request):
    type = request.GET.get("type")
    return render(request,"home.html",{"type":type})

def userRegister(request):
    name = request.POST.get("ur_uname")
    contact = request.POST.get("ur_contact")
    email = request.POST.get("ur_email")
    password = request.POST.get("ur_pass")

    ur = UserRegistration(name=name,contact=contact,email=email,password=password)
    ur.save()

    return redirect("/openuser/?type=h_user")

def showModeratorRegsitrationpage(request):
    type = request.GET.get("type")
    return render(request,"home.html",{"type":type})


def moderatorRegister(request):
    name = request.POST.get("mr_uname")
    contact = request.POST.get("mr_contact")
    email = request.POST.get("mr_email")
    password = request.POST.get("mr_pass")

    mr = ModeratorRegistration(name=name, contact=contact, email=email, password=password)
    mr.save()

    return redirect("/openmoderator/?type=h_moderator")


def userLogin(request):
    uname = request.POST.get("ur_email")
    upass = request.POST.get("ur_pass")

    qs = UserRegistration.objects.filter(email=uname,password=upass)
    print(qs)
    if qs:
        return render(request,"User.html")
    else:
        return render(request,"home.html",{"type":"h_New User"})


def moderatorLogin(request):
    uname = request.POST.get("mr_email")
    upass = request.POST.get("mr_pass")

    qs = ModeratorRegistration.objects.filter(email=uname, password=upass)
    print(qs)
    if qs:
        return render(request,"moderator.html")
    else:
        return render(request, "home.html",{"type":"h_New Moderator"})
