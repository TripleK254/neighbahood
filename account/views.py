from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth.models import auth, User
from .models import *
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.template import Context
from django.template.loader import get_template, render_to_string

# Create your views here.
def register(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_pass = request.POST['confirm_password']
        
        if Users.objects.filter(email=email).exists():
            messages.error(request, "email exists!!")
            return redirect('register')

        else:
            if Users.objects.filter(username=username).exists():
                messages.error(request, "username exists!!")
                return redirect('register')
            else:
                if password==confirm_pass:
                    user = Users() 
                    neighborhood_name = request.POST['neighborhood']

                    neighborhood = Neighborhood()
                    user.name = request.POST['name']
                    user.username = username
                    user.email = email
                    user.neighborhood_name =  Neighborhood.objects.get(id=neighborhood_name) 
                    activation_code = Users.objects.make_random_password(length=10, allowed_chars='1235')
                    user.verification_code = activation_code 
                    user.location = request.POST['location']
                    user.password = make_password(password)
                    
                    user.save()
                
                    
                    subject = 'Neibors Account Verification' 
                    message = render_to_string('account/email.html', {'activation_code': activation_code})
                    from_email = 'donotreply.neighbors.com'
                    to = user.email
                    send_mail(subject,message,from_email,[to] ,fail_silently=False, )
                    
                    messages.success(request,'Registered Successfully!!')
                    return redirect("verifyemail")  
                else:
                    messages.error(request,'Password doesnt match!!')
                    return redirect('register')
                
    else:
        neighborhood = Neighborhood.objects.all()
        return render(request,"account/register.html",{'neighborhoods':neighborhood})


def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "invalid credentials!!")
            return redirect('login')

    else:
        form= LoginForm()
        return render(request,'account/login.html',{'form':form})

def profile(request): 
    if request.method=="POST":
        user = request.user
        password = request.POST['password']
        c_password = request.POST['confirm_password']
        if len(password)<4:
            messages.error(request,'Password must be 4 characters or more!!')
            return redirect("profile") 
        else:
            if password==c_password:
                Users.objects.filter(email=user.email).update(password=make_password(password))
                messages.success(request,'saved successfully!')
                return redirect('profile')
            else:
                messages.error(request,'password doesnt match!!')
                return redirect("profile")   

    else:
        return render(request,'account/profile.html')

def logout(request):
    auth.logout(request)
    return redirect("login")

def dashboard(request): 
    if request.method=="POST":
        user = request.user
        post = Posts() #gets new object
        post.title = request.POST['title']
        post.description = request.POST['description']
        post.author = user.username
        post.neighborhood = user.neighborhood_name
        post.save()

        messages.success(request,'posted successfully!!')
        return redirect("dashboard")  
            
    else:
        user = request.user
        business =  Business.objects.all().filter(neighborhood=user.neighborhood_name) 
        health_center = Heath_center.objects.all().filter(neighborhood=user.neighborhood_name)
        emergency = Emergency_service.objects.all().filter(neighborhood=user.neighborhood_name)
        neighborhood = Neighborhood.objects.all()
        return render(request,'account/dashboard.html', {'businesses': business, 'health_centers': health_center, 'emergency_contacts':emergency, 'neighborhoodS':neighborhood })

def blog(request): 
    blog = Posts.objects.all()
    return render(request,'account/blog.html', {'blogs':blog})

def add_business(request): 
    if request.method=="POST":
        bs = Business(commit=False)
        bs.name = request.POST['name']
        bs.email = request.POST['email']
        bs.user = request.POST['user']
        bs.neighborhood = request.POST['neighborhood']
        bs.save()
        messages.success(request,'Successfully saved!!')
        return redirect('add-business')
    else:
        return render(request,'account/add-business.html')

def add_policestation(request): 
    if request.method=="POST":
        p_s = Police_station()
        p_s.name = request.POST['name']
        p_s.neighborhood = request.POST['neighborhood']
        p_s.save()
        messages.success(request,'Successfully saved!!')
        return redirect('add-policestation')
    else:
        return render(request,'account/add-policestation.html')

def add_health_center(request): 
    if request.method=="POST":
        h_c = Heath_center()
        h_c.name = request.POST['name']
        h_c.neighborhood = request.POST['neighborhood']
        h_c.save()

        messages.success(request,'Successfully saved!!')
        return redirect("add-health-center")  
    else:
        return render(request,'account/add-health-center.html')

def search(request): 
    user = request.user
    if request.method=="POST":
        bs_name = request.POST['bs_name']
        results = Business.objects.filter(name__contains=bs_name, neighborhood__contains=user.neighborhood_name)
        count_results = Business.objects.filter(name__contains=bs_name, neighborhood__contains=user.neighborhood_name).count()
        return render(request,'account/search-result.html',{'results':results,'count_result':count_results })  
    else:
        return redirect('dashboard')

def verify_email(request): 
    if request.method=="POST":
        email = request.POST['email']
        code = request.POST['code']
        
        if Users.objects.filter(email=email):
            if Users.objects.filter(verification_code=code):
                Users.objects.filter(email=email).update(is_active=True)
                messages.success(request,'successfully activated!')
                return redirect('login')
            else:
                messages.error(request,'invalid code!!')
                return redirect('verifyemail')
        else:
            messages.error(request,'Email doesnt exist!!')
            return redirect('verifyemail')
                  
    else:
        return render(request,'account/verifyemail.html')