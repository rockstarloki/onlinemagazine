from django.shortcuts import render, redirect
from .models import ModeratorRegistration
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
    name = request.POST.get("mr_name")
    contact = request.POST.get("mr_contact")
    email = request.POST.get("mr_email")
    password = request.POST.get("mr_pass")

    mr = ModeratorRegistration(name=name, contact=contact, email=email, password=password)
    mr.save()

    return render(request,"moderator.html")


def userLogin(request):
    uname = request.POST.get("ur_email")
    upass = request.POST.get("ur_pass")

    qs = UserRegistration.objects.filter(email=uname,password=upass)
    print(qs)
    if qs:
        pas = UserRegistration.objects.get(email=uname) #for getting the all data to print on html page
        return render(request,"User.html",{"data":pas})
    else:
        return render(request,"home.html",{"type":"h_New User"})






def moderatorLogin(request):
    uname = request.POST.get("mr_email")
    upass = request.POST.get("mr_pass")

    qs = ModeratorRegistration.objects.filter(email=uname, password=upass)
    print(qs)
    if qs:

        pas = ModeratorRegistration.objects.get(email=uname)
        return render(request,"moderator.html",{"data":pas})
    else:
        return render(request, "home.html",{"type":"h_New Moderator"})


def showmagazine(request):
    type = request.GET.get("type")
    return render(request, "magazine.html", {"type": type})


def mr_viewprofile(request):
    email = request.GET.get("type")
    mr = ModeratorRegistration.objects.get(email=email)

    return render(request, "moderator.html", {"mr_viewprofile": mr, "data": mr})

def mr_updateprofile(request):
    email = request.GET.get("type")
    mr = ModeratorRegistration.objects.get(email=email)

    return render(request,"moderator.html",{"mr_updateprofile":mr,"data":mr})


def mr_update(request):
    mr_name = request.POST.get("mr_name")
    mr_contact = request.POST.get("mr_contact")
    mr_email = request.POST.get("mr_email")
    mr_password = request.POST.get("mr_password")

    mr_updateprofile = ModeratorRegistration(name=mr_name, contact=mr_contact, email=mr_email, password=mr_password)
    mr_updateprofile.save()

    return render(request, "moderator.html", {"mr_updateprofile": mr_updateprofile})


def ur_viewprofile(request):
    email = request.GET.get("type")
    ur = UserRegistration.objects.get(email=email)

    return render(request, "User.html", {"ur_viewprofile": ur, "data": ur})


def ur_updateprofile(request):
    email = request.GET.get("type")
    ur = UserRegistration.objects.get(email=email)

    return render(request, "User.html", {"ur_updateprofile": ur, "data": ur})

def ur_update(request):
    ur_name = request.POST.get("ur_name")
    ur_contact = request.POST.get("ur_contact")
    ur_email = request.POST.get("ur_email")
    ur_password = request.POST.get("ur_password")

    ur_updateprofile = UserRegistration(name=ur_name, contact=ur_contact, email=ur_email, password=ur_password)
    ur_updateprofile.save()

    return render(request, "User.html", {"ur_updateprofile": ur_updateprofile})

def validatepost(request):
    pass


def postarticle(request):
    type = request.GET.get("type")

