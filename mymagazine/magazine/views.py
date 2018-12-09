from django.shortcuts import render
from django.core.mail import EmailMessage
from mymagazine import settings as se
from magazine.functions import handle_uploaded_file


# Create your views here.
from magazine.models import UserRegistration
from magazine.models import ModeratorRegistration
from magazine.models import ModTechnology
from magazine.models import ModHealth
from magazine.models import ModFashion
from magazine.models import HomeFashion
from magazine.models import HomeTechnology
from magazine.models import HomeHealth


#For home screen oprations home
def openHome(request):
    type = "home"
    return render(request, "index.html", {"type": type})

#For home screen oprations aboutus
def aboutus(request):
    type = "aboutus"
    return render(request,"index.html",{"type":type})

# Showing User login Page
def openUser(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})

# Showing User Registration Page
def showUserRegsitrationpage(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"type":type})

# For User's Details  Saving the data into the database
def userRegister(request):
    name = request.POST.get("ur_uname")
    contact = request.POST.get("ur_contact")
    email = request.POST.get("ur_email")
    password = request.POST.get("ur_pass")

    ur = UserRegistration(name=name,contact=contact,email=email,password=password)
    ur.save()

    return render(request,"index.html",{"message":"User Registered SuccessFully","type":"h_user"})


# Showing User Validating the User login data
def userLogin(request):
    uname = request.POST.get("ur_email")
    upass = request.POST.get("ur_pass")

    qs = UserRegistration.objects.filter(email=uname,password=upass)
    print(qs)
    if qs:
        pas = UserRegistration.objects.get(email=uname) #for getting the all data to print on html page
        return render(request,"user.html",{"data":pas})
    else:
        return render(request,"index.html",{"type":"h_New User"})

# Opening the User the user viewprofile
def ur_viewprofile(request):
    email = request.GET.get("type")
    print(email)
    ur = UserRegistration.objects.get(email=email)
    print(ur)

    return render(request,"user.html",{"ur_viewprofile":ur,"data":ur})# User showing the update_profile

# Opening User Update profile
def ur_updateprofile(request):
    email = request.GET.get("type")
    ur = UserRegistration.objects.get(email=email)
    print(ur)
    return render(request, "User.html", {"ur_updateprofile": ur, "data": ur})

# User updating the profile to the database
def ur_update(request):
    ur_name = request.POST.get("ur_name")
    ur_contact = request.POST.get("ur_contact")
    ur_email = request.POST.get("ur_email")
    ur_password = request.POST.get("ur_password")

    ur_updateprofile = UserRegistration(name=ur_name, contact=ur_contact, email=ur_email, password=ur_password)
    ur_updateprofile.save()

    user=UserRegistration.objects.get(email=ur_email)
    return render(request, "User.html", {"data": user,"ur_updateprofile":user})

# Opening  the Post Article page
def postarticle(request):
    email = request.GET.get("type")
    ur = UserRegistration.objects.get(email=email)
    print(ur)
    return render(request,"user.html",{"postarticle":ur,"data":ur})


# Saving the articles into the database
def  post(request):
    email = request.GET.get("type")
    # print(email)
    article_type = request.POST.get("article_type")
    article_headline = request.POST.get("article_headline")
    article_discription = request.POST.get("article_discription")
    # article_image =request.FILES['file']
    # print(article_image)
    # handle_uploaded_file(request.FILES['file'])

    name = request.POST.get('user_email')
    print(name)

    if article_type == "fashion":
        f = ModFashion(article_type=article_type,article_headline=article_headline,article_dicription=article_discription,user_email=email)
        f.save()
        email = request.POST.get("type")#for getting the user name to the same page after form action
        print(email)
        em = UserRegistration.objects.filter(email=email)

        return render(request,"user.html",{"article":" article successfully posted","data":em})
    elif article_type == "technology":
        t  = ModTechnology(article_type=article_type,article_headline=article_headline,article_dicription=article_discription,user_email=email)
        t.save()

        email = request.POST.get("type")#for getting the user name to the same page after form action
        print(email)
        em = UserRegistration.objects.filter(email=email)
        return render(request, "user.html", {"article": " article successfully posted", "data": em})
    elif article_type == "health":
        h = ModHealth(article_type=article_type,article_headline=article_headline,article_dicription=article_discription,user_email=email)
        h.save()

        email = request.POST.get("type")#for getting the user name to the same page after form action
        print(email)
        # user = UserRegistration.objects.get(email=email)
        # print(user)
        return render(request, "user.html", {"article": " article successfully posted","data":email})
    else:

        email = request.POST.get("type")#for getting the user name to the same page after form action
        print(email)
        # user = UserRegistration.objects.get(email=email)

        return render(request, "user.html", {"message": " Invalid Type of Article","data":email})



# Moderator opertaions like show login page,login validate,show moderator registration page,moderator register save into the database

# Opening the moderator login page
def openModerator(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


# Opening the moderator Home page
def openmoderatorhome(request):
    type = request.GET.get('type')

    modhome = ModeratorRegistration.objects.get(email=type)# for getting the Moderator Details to the same page

    return render(request,"moderator.html",{"data":modhome})

# Opening Aboutus page in moderator
def openmodaboutus(request):
    email = request.GET.get('type')
    modhome = ModeratorRegistration.objects.get(email=email)# for getting the Moderator Details to the same page
    type = 'aboutus'
    return render(request, "moderator.html", {"type":type,"data": modhome})


# Opening the moderator Registration page
def showModeratorRegsitrationpage(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"type":type})

# Validating the moderator login data
def moderatorLogin(request):
    uname = request.POST.get("mr_email")
    upass = request.POST.get("mr_pass")

    qs = ModeratorRegistration.objects.filter(email=uname, password=upass)
    print(qs)
    if qs:

        pas = ModeratorRegistration.objects.get(email=uname)# for getting the Moderator Details to the same page
        return render(request,"moderator.html",{"message":"Moderator Successfully Registered","data":pas})
    else:
        return render(request,"index.html",{"type":"h_moderator"})

# Opening the moderator ViewProfile page
def mr_viewprofile(request):
    email = request.GET.get("type")
    print(email)
    mr = ModeratorRegistration.objects.get(email=email)# for getting the Moderator Details to the same page
    print(mr)
    return render(request, "moderator.html", {"mr_viewprofile": mr, "data": mr})

# Moderator showing moderator update profile page
def mr_updateprofile(request):
    email = request.GET.get("type")
    mr = ModeratorRegistration.objects.get(email=email)# for getting the Moderator Details to the same page

    return render(request,"moderator.html",{"mr_updateprofile":mr,"data":mr})

# Moderator showing moderator Updated the moderator profile page
def mr_update(request):
    mr_name = request.POST.get("mr_name")
    mr_contact = request.POST.get("mr_contact")
    mr_email = request.POST.get("mr_email")
    mr_password = request.POST.get("mr_password")

    mr_updateprofile = ModeratorRegistration(name=mr_name, contact=mr_contact, email=mr_email, password=mr_password)
    mr_updateprofile.save()

    mod = ModeratorRegistration.objects.get(email=mr_email)# for getting the Moderator Details to the same page

    return render(request, "moderator.html", {"mr_updateprofile": mod,"data":mod})

def validatepost(request):
    email = request.GET.get("type")

    pas = ModeratorRegistration.objects.get(email=email)# for getting the Moderator Details to the same page
    print(pas)
    return render(request,"moderator.html",{"validate":"validate","validatepost":pas,"data":pas})

# Opening the User Home
def openuserhome(request):
    type = request.GET.get("type")
    pas = UserRegistration.objects.get(email=type)  # for getting the all data to print on html page
    return render(request, "user.html", {"data": pas})


# Opening the Aboutus in Moderator

def useraboutus(request):
    email = request.GET.get('type')
    name = UserRegistration.objects.get(email=email)# for getting the User Details to the same page
    type = "aboutus"
    return render(request, "index.html", {"type": type,"data":name})


# Opening the Moderator Fashion Article Headline's
def openmodfashion(request):
    type = "fashion"

    user = request.GET.get("type")
    user1 = ModeratorRegistration.objects.get(email=user)# for getting the Moderator Details to the same page
    print(user1)
    fash = ModFashion.objects.all()

    return render(request, "moderator.html", {"fashion": type, "fash": fash, "data": user1})

# Opening the Moderator Technology Article Headline's
def openmodtechnology(request):
    type = "technology"

    user = request.GET.get('type')
    user1 = ModeratorRegistration.objects.get(email=user)# for getting the Moderator Details to the same page

    tech = ModTechnology.objects.all()
    return render(request, "moderator.html", {"technology": type, "tech": tech, 'data': user1})

# Opening the Moderator Health Article Headline's
def openmodhealth(request):
    type = "health"

    user = request.GET.get('type')
    user1 = ModeratorRegistration.objects.get(email=user)# for getting the Moderator Details to the same page

    heal = ModHealth.objects.all()

    return render(request, "moderator.html", {"health": type, "heal": heal, "data": user1})

# Opening the Home Fashion Article Headline's
def openhomefashion(request):
    type = "fashion"

    homefash = HomeFashion.objects.all()

    return render(request,"index.html",{"fashion":type,"data":homefash})

# Opening the Home Technology Article Headline's
def openhometechnology(request):
    type = 'technology'
    hometech = HomeTechnology.objects.all()
    return render(request,"index.html",{"technology":type,"data":hometech})

# Opening the Home Health Article Headline's
def openhomehealth(request):
    type = 'health'
    homehealth = HomeHealth.objects.all()
    return render(request,"index.html",{"health":type,"data":homehealth})

# Opening the Home Health Article Discription
def showhomehealth(request):
    head = request.GET.get('type')

    dis = HomeHealth.objects.filter(article_headline=head)

    type = 'showhomehealth'

    return render(request,"index.html",{"showhomehealth":type,"data":dis})

# Opening the Home Fashiom Article Discription
def showhomefashion(request):
    headline = request.GET.get('type')

    dis = HomeFashion.objects.filter(article_headline=headline)
    type = 'showhomefashion'

    return render(request,"index.html",{"showhomefashion":type,"data":dis})

# Opening the modeerator Technology Article Discription
def showhometech(request):
    head = request.GET.get('type')
    print(head)

    dis = HomeTechnology.objects.filter(article_headline=head)
    type = 'showhometech'
    print(dis)
    return render(request,"index.html",{"showhometech":type,"data":dis})

# Opening the Moderator Fashion Article Discription
def showmodfashion(request):
    head = request.GET.get('type')
    hh = head.split("-")
    heading = hh[0]
    email = hh[1]
    print(heading)
    print(email)

    dis = ModFashion.objects.filter(article_headline=heading)

    name = ModeratorRegistration.objects.get(email=email)# for getting the Moderator Details to the same page

    type = 'showmodfashion'
    return render(request,"moderator.html",{"showmodfashion":type,"fash":dis,"data":name})

# Opening the Moderator Technology Article Discription
def showmodtech(request):
    head = request.GET.get('type')
    hh=head.split("-")
    heading=hh[0]
    email=hh[1]
    print(heading)
    print(email)

    name = ModeratorRegistration.objects.get(email=email)# for getting the Moderator Details to the same page

    dis = ModTechnology.objects.filter(article_headline=heading)

    type = 'showmodtech'
    return render(request, "moderator.html", {"showmodtech": type, "tech": dis,"data":name})

# Opening the Moderator Health Article Discription
def showmodhealth(request):
    head = request.GET.get('type')
    hh = head.split("-")
    heading = hh[0]
    email = hh[1]
    print(heading)
    print(email)

    dis = ModHealth.objects.filter(article_headline=heading)

    name = ModeratorRegistration.objects.get(email=email)# for getting the Moderator Details to the same page

    type = 'showmodhealth'
    return render(request, "moderator.html", {"showmodhealth": type, "heal": dis,"data":name})



# Opening the User Health Article Discription
def showuserhealth(request):
    head = request.GET.get('type')
    hh = head.split("-")
    heading = hh[0]
    email = hh[1]
    print(heading)
    print(email)

    dis = HomeHealth.objects.filter(article_headline=head)

    name = UserRegistration.objects.get(email=email)# for getting the User Details to the same page

    type = 'showuserhealth'
    return render(request, "user.html", {"showuserhealth": type, "heal": dis,"data":name})

# Opening the User Technology Article Discription
def showusertech(request):
    head = request.GET.get('type')
    hh = head.split("-")
    heading = hh[0]
    email = hh[1]
    print(heading)
    print(email)

    dis = HomeTechnology.objects.filter(article_headline=head)
    name = UserRegistration.objects.get(email=email)# for getting the User Details to the same page

    type = 'showusertech'
    return render(request, "user.html", {"showusertech": type, "tech": dis,"data":name})

# Opening the User Technology Article Headline's
def openusertechnology(request):
    type = "technology"

    user = request.GET.get('type')
    user1 = UserRegistration.objects.get(email=user)# for getting the User Details to the same page

    tech = HomeTechnology.objects.all()
    return render(request, "user.html", {"technology": type, "tech": tech, 'data': user1})

# Opening the User Health Article Headline's
def openuserhealth(request):
    type = "health"

    user = request.GET.get('type')
    user1 = UserRegistration.objects.get(email=user)# for getting the User Details to the same page

    heal = HomeHealth.objects.all()

    return render(request, "user.html", {"health": type, "heal": heal, "data": user1})

# Showing the Fashion article headline's
def openuserfashion(request):
    type = "fashion"

    user = request.GET.get("type")
    user1 = UserRegistration.objects.get(email=user)# for getting the User Details to the same page

    fash = HomeFashion.objects.all()

    return render(request, "user.html", {"fashion": type, "fash": fash, "data": user1})


# Showing the Fashion Article Discriptions
def showuserfashion(request):
    head = request.GET.get('type')
    hh = head.split("-")
    heading = hh[0]
    email = hh[1]
    print(heading)
    print(email)


    dis = HomeFashion.objects.filter(article_headline=head)
    name = UserRegistration.objects.get(email=email)# for getting the User Details to the same page


    type = 'showuserfashion'

    return render(request, "user.html", {"showuserfashion": type,"fash":dis,"data":name})

# sending the data into the Home Article Database
def validate(request):
    email = request.GET.get("type")
    print(email)
    modr = ModeratorRegistration.objects.get(email=email)# for getting the Moderator Details to the same page
    article_type = request.POST.get('art_type')
    print(article_type)

    if article_type == 'fashion':
        fashall = ModFashion.objects.all()
        type = 'validate'

        return render(request,"moderator.html",{'validate':type,'art_type':article_type,'data':modr,'articles':fashall})
    elif article_type == 'technology':

        techall = ModTechnology.objects.all()
        type = 'validate'
        return render(request, "moderator.html", {'validate':type, 'data': modr,'art_type':article_type ,'articles':techall})
    elif article_type == 'health':
        healall = ModHealth.objects.all()
        type = 'validate'

        return render(request, "moderator.html", {'validate': type,'art_type':article_type, 'data': modr, 'articles':healall})
    else:
        type = 'validate'

        return render(request,"moderator.html",{'validate':type,'art_type':article_type,'data':modr,'type':'Invalid type'})

# Showing the sendemail page
def sendmail(request):
    moder = request.POST.get('type')
    to = request.POST.get('to')
    subject = request.POST.get('subject')
    mesage = request.POST.get('message')
    emails = to.spilt(',')

    ema =  EmailMessage(subject=subject,body=mesage,from_email=se.EMAIL_HOST_USER,to=emails)
    ema.send(False)

    mod = ModeratorRegistration.objects.get(email=moder)# for getting the Moderator Details to the same page

    return render(request,"moderator.html",{'sendemail':mod,"data":mod,'replay':'message successfully send' })

# Showing the articles which are posted by user's
def valid(request):
    article_data = request.GET.get('type')
    art_data = article_data.split('-')
    head = art_data[0]
    mail = art_data[1]

    name = ModeratorRegistration.objects.get(email=mail)# for getting the Moderator Details to the same page

    if head == 'fashion':
        art = ModFashion.objects.get(article_type=head)
        type = 'valid'
        return render(request,"moderator.html",{"valid":type,"data":name,"art":art})
    elif head == 'technology':
        art = ModTechnology.objects.get(article_type=head)
        type = 'valid'
        return render(request, "moderator.html", {"valid": type, "data": name, "art": art})
    elif head == 'health':
        art = ModHealth.objects.get(article_type=head)
        type = 'valid'
        return render(request, "moderator.html", {"valid": type, "data": name, "art": art})
    else:
        type = 'valid'
        return render(request, "moderator.html", {"valid":type,"ty""message":"Invalid type","data":name})

# sending the mail to the posted user
def send(request):
    datall = request.GET.get('type')
    dat = datall.split("-")
    head = dat[0]
    name = dat[1]

    name = ModeratorRegistration.objects.get(email=name)# for getting the Moderator Details to the same page


    article = ModTechnology.objects.get(article_headline=head)
    print(article)

    type = 'sendmail'
    return render(request,"moderator.html",{"sendmail":type,"article":article,"data":name})


def validarticle(request):
    type = request.POST.get('article_type')
    head = request.POST.get('article_headline')
    discription = request.POST.get('article_dicription')
    article_image = request.POST.get('article_image')
    name = request.GET.get('type')

    email = ModeratorRegistration.objects.get(email=name)# for getting the Moderator Details to the same page

    if type == 'fashion':
        hf = HomeFashion(article_headline=head,article_dicription=discription,article_image=article_image)
        hf.save()
        return render(request,"moderator.html",{"meassage":"Aticle Post Successfully","data":email})
    elif type == 'technology':
        ht = HomeTechnology(article_headline=head,article_dicription=discription,article_image=article_image)
        ht.save()
        return render(request, "moderator.html", {"meassage": "Aticle Post Successfully", "data": email})
    elif type == 'health':
        hh = HomeHealth(article_headline=head, article_dicription=discription, article_image=article_image)
        hh.save()
        return render(request, "moderator.html", {"meassage": "Aticle Post Successfully", "data": email})
    else:
        return render(request, "moderator.html", {"meassage": "Aticle Post Successfully", "data": email})


def moderatorRegister(request):
    name = request.POST.get('mr_name')
    contact = request.POST.get('mr_contact')
    email = request.POST.get('mr_email')
    password = request.POST.get('mr_pass')

    mr = ModeratorRegistration(name=name,contact=contact,email=email,password=password)
    mr.save()

    return render(request,"index.html",{"message":" Moderator Registered SuccessFully","type":"h_moderator"})


def sent(request):
    name = request.GET.get('type')
    to = request.POST.get('to')
    message = request.POST.get('message')
    subject = request.POST.get('subject')
    email = list(to)
    em = EmailMessage(to=email,subject=subject,body=message,from_email=se.EMAIL_HOST_USER)
    em.send(True)

    email = ModeratorRegistration.objects.get(email=name)
    return render(request,"moderator.html",{"emailmessage":"Email Send Successfully","data":email})
