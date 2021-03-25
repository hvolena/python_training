# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_edit_first_contact(app):
        app.session.login(username="admin", password="secret")
        app.return_home_page()
        app.contact.edit_first_contact(firstname="Пупкин")
        app.session.logout()
