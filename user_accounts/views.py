from django.shortcuts import render,redirect
from user_accounts.forms import Register_form,user_change_form
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponse
from books.models import Purcehase_model
# Create your views here.



# singup related stars here 
def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = Register_form(request.POST)
            if form.is_valid():
                messages.success(request,"Welcome to our website")
                form.save()
                return redirect("loginpage")
        else : 
            form = Register_form(request.POST)
        return render(request,"./signup.html",{'form':form})
    else : 
        return redirect("profilepage")


# signup related form ends here 

# login related form 
def User_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=name,password=password) #checking user in the database or not
                if user is not None:
                    login(request,user)
                    return redirect("profilepage")
        else :
            form = AuthenticationForm()
        return render(request,"./login.html",{'form':form})
    else:
        return redirect("profilepage")
        
# def profile(request):
#     if request.user.is_authenticated:
#         return render(request,"./profile.html",{'user':request.user}) 
#     else :
#         return redirect("loginpage")
    
def profile(request):
    

    if request.user.is_authenticated:
        purchase_all_history= Purcehase_model.objects.filter(user= request.user)
        if request.method == "POST":
            form = user_change_form(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,"Account Updated Suceessfully")
                form.save()
                return redirect("profilepage")
        else: 
            form = user_change_form(instance=request.user)
        return render(request,"./profile.html",{'form':form,'data':purchase_all_history})
    else : 
        return redirect("singup")
    
def update_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = user_change_form(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,"Account Updated Suceessfully")
                form.save()
                return redirect("profilepage")
        else: 
            form = user_change_form(instance=request.user)
        return render(request,"./update_profile.html",{'form':form})
    else : 
        return redirect("singup")
    
# user logout area 

def user_logout(request):
    logout(request)
    return redirect("loginpage")

def change_pass(request):
    if request.method == "POST":
        form = PasswordChangeForm(user =request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            # form.cleaned_data['user']
            return redirect("profilepage")
    else : 
        form = PasswordChangeForm(user = request.user)
        return render(request,"./passchangeform.html",{'form':form})
    
# change password without old password

    
def change_pass2(request):
    if request.method == "POST":
        form = SetPasswordForm(user =request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            # form.cleaned_data['user']
            return redirect("profilepage")
    else : 
        form = SetPasswordForm(user = request.user)
    return render(request,"./passchangeform.html",{'form':form})




# change user data 

# def change_user_data(request):
#     if not request.user.is_authenticated:
#         if request.method == "POST":
#             form = Register_form(request.POST)
#             if form.is_valid():
#                 messages.success(request,"Welcome to our website")
#                 form.save()
#                 return redirect("loginpage")
#         else : 
#             form = Register_form(request.POST)
#         return render(request,"signup.html",{'form':form})
#     else : 
#         return redirect("profilepage")





    




    




