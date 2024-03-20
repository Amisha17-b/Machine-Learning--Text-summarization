import json
import pyrebase
 
config={
  "apiKey": "AIzaSyDEPUfacyMTaPv2xLo9C-ysTaW8e9s-cP4",
  "authDomain": "text-summarization-6b509.firebaseapp.com",
  "databaseURL": "https://text-summarization-6b509-default-rtdb.firebaseio.com",
  "projectId": "text-summarization-6b509",
  "storageBucket": "text-summarization-6b509.appspot.com",
  "messagingSenderId": "50940842118",
  "appId": "1:50940842118:web:460a4e3b196f67b3770107",
  "measurementId": "G-D61YV6W77J"
}

firebase = pyrebase.initialize_app(config)
auth=firebase.auth()

def registerUser(email,password):
  # print (email+" "+password)
  try:
    user=auth.create_user_with_email_and_password(email,password)
    return user
  except Exception as e: 
    error_json = e.args[1]
    error_msg = json.loads(error_json)['error']['message']
    error_code = json.loads(error_json)['error']['code']
    print(error_msg)
    print(error_code)
    return [error_code,error_msg]
  
def loginUser(email,password):
  try:
    user=auth.sign_in_with_email_and_password(email,password)
    return user
  except Exception as e: 
    error_json = e.args[1]
    error_msg = json.loads(error_json)['error']['message']
    error_code = json.loads(error_json)['error']['code']
    print(error_msg)
    print(error_code)
    return [error_code,error_msg]
  
def logoutUser():
  try:
    auth.current_user = None
    return auth.current_user
  except Exception as e: 
    error_json = e.args[1]
    error_msg = json.loads(error_json)['error']['message']
    error_code = json.loads(error_json)['error']['code']
    print(error_msg)
    print(error_code)
  return [error_code,error_msg]