from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.contrib.auth.models import User

from .forms import Registration_form

from .models import Record


# Create your views here.

def home(request):

    if request.user.is_authenticated:
        data = Record.objects.filter(user = request.user)

        if not data.exists():
            messages.success(request, "you do not have any data!")
        # messages.success(request,f"hello")
        return render(request, 'home.html',{'data':data})

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'login successful!')
            return redirect('home')
        else:
            messages.success(request, 'wrong credentials!')
            return redirect('home')
            # show error



    else:   
        return render(request, 'home.html',{})
    

def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out...')
    return redirect('home')


def register_user(request):
    if(request.method == 'POST'):
        form  = Registration_form(request.POST)
        if(form.is_valid()):
            form.save()



            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request,"Registration successful! welcome!")
                return redirect('home')
            
        else:
            return render(request, 'register.html',{'form':form})

                
    

    else:
        form = Registration_form()

    


    return render(request, 'register.html',{'form' : form})



# @login_required(login_url='/home/')
def add_data(request):
    if not request.user.is_authenticated:
        return redirect('home')
    

    
    return render(request , 'add-data.html')
