from config import create_new_user, create_new_session, get_user, update_user
from config import login_user, email_user, password_user
import pytest

'''Fixture '''
@pytest.fixture
def Authorization():
    create_new_user(login_user, email_user, password_user)
    create_new_session(login_user, password_user)
    yield



'''Tests'''
def test_get_user(Authorization):
    
    user_data = get_user(login_user)
    login_from_request = user_data["login"]
    email_from_request = user_data["email"]

    assert login_user == login_from_request and email_user == email_from_request




def test_update_user(Authorization):
     
    new_login = 'new_login_valentyn'
    new_email = 'new_mail_valentyn@gmail.com'
    update_user(new_login, new_email)

    updated_user_data = get_user(new_login)

    login_from_request = updated_user_data["login"]
    email_from_request = updated_user_data["email"]

    assert new_login == login_from_request and new_email == email_from_request

    