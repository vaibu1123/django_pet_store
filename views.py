from django.shortcuts import render,HttpResponse,redirect
from petstoreapp.models import petstoreapp_db
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def dashboard(request):
    m=petstoreapp_db.objects.all()
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)

def delete(request,rid):
   m=petstoreapp_db.objects.filter(id=rid)
   m.delete()
   return redirect('/dashboard')

def edit(request,rid):
   if request.method=='GET':
      
      return render(request,'edit.html')
   else:
      name=request.POST['name']
      price=request.POST['price']

def demo(request):
   return render(request,'demo.html')

def home (request):
   m=petstoreapp_db.objects.all()
   context={}
   context['data']=m
   return render(request,'home.html',context)

def register(request):
   if request.method =='GET':
      return render(request,'register.html')
   else:
      uname=request.POST['uname']
      uemail=request.POST['uemail']
      upass=request.POST['upass']
      cpass=request.POST['cpass']

      if uname =="" or upass =="" or cpass =="":

         context ={}
         context['msg']="field can not be empty"

         return  render(request,'register.html',context)
      
      elif upass != cpass:
         context= {}
         context['msg']="Password and Confirm password should be same"

         return render(request,'register.html',context)
      
      else:

            u=User.objects.create(username= uname,email=uemail)
            u.set_password(upass)
            u.save()

            context= {}
            context['msg']="User register sucessfully"

            return render(request,'register.html',context)
   
def user_login(request):

   if request.method=='GET':
      return render(request,'login.html')
   else:
      uname=request.POST['uname']
      upass=request.POST['upass']
   
      u=authenticate(username=uname,password=upass)

      if u is not None:
         login(request,u)
         return redirect("/")
      else:
         return HttpResponse("username password does not match")
      
def user_logout(request):

   logout(request)

   return redirect("/")
