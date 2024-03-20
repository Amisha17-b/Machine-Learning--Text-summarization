from django.shortcuts import render,redirect
from tsapp.firebase import registerUser,loginUser,logoutUser
from tsapp.cosine_distance import generate_summary
from tsapp.gensim_model import gensim_summary
from django.contrib import messages

user=None
# Create your views here.
def index(request):
  global user
  return render(request,'index.html',{'user':user})

def gensummary(request):
  return render(request,'gensummary.html')

def login(request):
  if user is None:
    return render(request,'login.html')
  messages.warning(request,"Already signed in user")
  return redirect(index)

def register(request):
   return render(request,'register.html')
 
def onLogin(request):
  global user
  if request.method == 'POST':
    email = str(request.POST.get('email'))
    password = request.POST.get('pass')
    user=loginUser(email,password)
    if isinstance(user,list):
      messages.error(request,str(user[0])+":"+user[1])
      return redirect(login)
    messages.success(request,"Login successful")
    return redirect(index)

def onRegister(request):
  global user
  if request.method == 'POST':
    email = str(request.POST.get('email'))
    password = request.POST.get('pass')
    user=registerUser(email,password)
    if isinstance(user,list):
      messages.error(request,str(user[0])+":"+user[1])
      return redirect(register)
    messages.success(request,"Registered Successfully")
    return redirect(login)

def contact(request):
    return render(request,"<html><h1>CONTACT</h1></html>")

def summarize(request):
  if isinstance(user,list) or user==None:
    messages.success(request,"Please sign in")
    return redirect(login)

  if request.method == 'POST':
      input = str(request.POST.get('input'))
      range = int(request.POST.get('range'))
      if input.strip() :
          result=generate_summary(input,range)
          return render(request, 'index.html', {'input':input,'result': result,'range': range,'user':user})
      else:
          return redirect(index)
  else:
      return render(request, 'index.html')

def gen_summarize(request):
  if isinstance(user,list) or user==None:
    messages.success(request,"Please sign in")
    return redirect(login)

  if request.method == 'POST':
      input = str(request.POST.get('input'))
      range = int(request.POST.get('range'))
      if input.strip():
          result=gensim_summary(input,range)
          return render(request, 'gensummary.html', {'input':input,'result': result,'range': range,'user':user})
  else:
      return redirect(gensummary)

def logout(request):
  global user
  user=logoutUser()
  if user is None:
    messages.success(request,"Sign Out successful")
    return redirect(index)