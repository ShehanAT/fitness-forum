import pytest
from django.urls import reverse 


@pytest.mark.django_db
def test_login_fail(api_client):
    login_url = reverse('forum:login')
    data = {
        'form_data':{
            'username': 'failed_login',
            'password': 'failed_login'
        }
    }
    response = api_client.post(login_url, data, format='json')
    assert response.status_code == 400 
    # assert response.json() == {'login_form': {'non_field_errors': ['Invalid credentials']}}
    assert response.cookies.get('sessionid') is None 