from django.shortcuts import render,redirect
from tsapp.firebase import registerUser,loginUser,logoutUser
from tsapp.cosine_distance import generate_summary
from tsapp.gensim_model import gensim_summary
from django.contrib import messages

# Initializing a global variable user to None

user=None
# Create your views here.
# View function for rendering the index page

def index(request):
  global user
  return render(request,'index.html',{'user':user})

# View function for rendering the gensummary page
def gensummary(request):
  return render(request,'gensummary.html')

# View function for rendering the login page
def login(request):
  if user is None:
    return render(request,'login.html')
  messages.warning(request,"Already signed in user")
  return redirect(index)

# View function for rendering the register page
def register(request):
   return render(request,'register.html')
 
 # View function for handling user login
def onLogin(request):
  global user
  if request.method == 'POST':
    email = str(request.POST.get('email'))
    password = request.POST.get('pass')
    user=loginUser(email,password)
    # Authenticating user using Firebase authentication
    if isinstance(user,list):
       # If authentication fails, display error message and redirect to login page
      messages.error(request,str(user[0])+":"+user[1])
      return redirect(login)
    messages.success(request,"Login successful")
    return redirect(index)

# View function for handling user registration
def onRegister(request):
  global user
  if request.method == 'POST':
    email = str(request.POST.get('email'))
    password = request.POST.get('pass')
    user=registerUser(email,password)
    # Registering user using Firebase authentication
    if isinstance(user,list):
       # If registration fails, display error message and redirect to register page
      messages.error(request,str(user[0])+":"+user[1])
      return redirect(register)
    messages.success(request,"Registered Successfully")
    return redirect(login)
  
# View function for rendering the contact page
def contact(request):
    return render(request,"<html><h1>CONTACT</h1></html>")

# View function for generating text summary
def summarize(request):
  if isinstance(user,list) or user==None:
     # If user is not logged in, display message and redirect to login page
    messages.success(request,"Please sign in")
    return redirect(login)

  if request.method == 'POST':
       # Handling POST request for text summarization
      input = str(request.POST.get('input'))
      range = int(request.POST.get('range'))
      if input.strip() :
          # If input text is not empty, generate summary using cosine distance
          result=generate_summary(input,range)
          return render(request, 'index.html', {'input':input,'result': result,'range': range,'user':user})
      else:
          return redirect(index)
  else:
      return render(request, 'index.html')

# View function for generating text summary using gensim
def gen_summarize(request):
  if isinstance(user,list) or user==None:
     # If user is not logged in, display message and redirect to login page
    messages.success(request,"Please sign in")
    return redirect(login)

  if request.method == 'POST':
      # Handling POST request for text summarization
      input = str(request.POST.get('input'))
      range = int(request.POST.get('range'))
      if input.strip():
          # If input text is not empty, generate summary using gensim
          result=gensim_summary(input,range)
          return render(request, 'gensummary.html', {'input':input,'result': result,'range': range,'user':user})
  else:
      return redirect(gensummary)
# View function for user logout
def logout(request):
  global user
  user=logoutUser()
  # Logging out user using Firebase authentication
  if user is None:
    # If logout is successful, display success message and redirect to index page
    messages.success(request,"Sign Out successful")
    return redirect(index)