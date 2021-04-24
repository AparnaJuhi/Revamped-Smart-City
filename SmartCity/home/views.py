from django.shortcuts import render, HttpResponse
import pyrebase
from django.contrib import auth
config={'apiKey': "AIzaSyB5OhUoICNtfAO09VY5bBSERXNQWkSnTvw",
    'authDomain': "aparnafireapp.firebaseapp.com",
    'databaseURL': "https://aparnafireapp.firebaseio.com",
    'projectId': "aparnafireapp",
    'storageBucket': "aparnafireapp.appspot.com",
    'messagingSenderId': "529367799017",
    'appId': "1:529367799017:web:18f322315da9b7cc100c78"  
  }
firebase=pyrebase.initialize_app(config)
authe=firebase.auth()
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
     return render(request,'contact.html')
# Create your views here.
def signin(request):
    return render(request,'signin.html')

def postsign(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    try:
        user=authe.sign_in_with_email_and_password(email,password)
        print(user)
        
    except:
        message="Invalid credentials"
        return render(request,'signin.html',{"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,'welcome.html',{"email":email})

def logout(request):
    auth.logout(request)
    message="Successfully logout"
    return render(request,'signin.html',{"message":message})
