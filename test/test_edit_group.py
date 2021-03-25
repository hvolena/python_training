# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_edit_first_group(app):
        app.session.login(username="admin", password="secret")
        app.group.edit_first_group(group_name="Друзья")
        app.session.logout()
