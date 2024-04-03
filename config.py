import requests
import json


token = '7646d281e48bdc23002d6eafeb70259d'  # Ваш токен для доступу до API (якщо потрібний)

headers_for_auth = {
  "Authorization": f"Token token={token}"}

login_user = 'test_user_valentyn'
email_user = 'test_v@gmail.com'
password_user = 'test12345!'



'''Create new user'''
def create_new_user(login, email, password):

    new_user_credentionals = { 
        "user": {
        "login": login,
        "email": email,
        "password": password
        }
    }
    new_u = requests.post('https://favqs.com/api/users', headers=headers_for_auth, json=new_user_credentionals)




'''Create new session'''
def create_new_session(login, password):

    session_credentionals = { 
        "user": {
        "login": login,
        "password": password
        }
    }

    session_request = requests.post('https://favqs.com/api/session', headers=headers_for_auth, json=session_credentionals)
    session_request_response_json = json.loads(session_request.text)

    global user_token
    
    user_token = session_request_response_json["User-Token"]




def get_user(user_name):
  
    global headers_for_user_request

    headers_for_user_request = {
        "User-Token": user_token,
        "Authorization": f"Token token={token}"}
    
    request_get_user = requests.get(f'https://favqs.com/api/users/{user_name}', headers=headers_for_user_request)
    request_get_user_json = json.loads(request_get_user.text)

    global login_from_request, account_details_from_request, email_from_request

    login_from_request = request_get_user_json["login"]
    account_details_from_request = request_get_user_json["account_details"]
    email_from_request = account_details_from_request['email']
    
    return {"login": login_from_request, "email": email_from_request}




def update_user(updated_login, updated_email):
    global new_login_user
    new_login_user = updated_login
    headers_for_user_request = {
        "User-Token": user_token,
        "Authorization": f"Token token={token}"
    }

    update_user_headers = { 
        "user": {
            "login": updated_login,
            "email": updated_email,
        }
    }
  
    request_update_user = requests.put('https://favqs.com/api/users/test_user_valentyn', headers=headers_for_user_request, json=update_user_headers)
    print(request_update_user.text)

