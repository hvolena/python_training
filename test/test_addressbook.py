# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
        app.login(username="admin", password="secret")
        app.init_new_contact()
        app.create_new_contact(Contact(firstname="Petr", middlename="Smirnov"))
        app.logout()

def test_add_empty_contact(app):
        app.login(username="admin", password="secret")
        app.init_new_contact()
        app.create_new_contact(Contact(firstname="", middlename=""))
        app.logout()


