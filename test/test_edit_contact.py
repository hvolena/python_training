# -*- coding: utf-8 -*-
import pytest

def test_edit_first_contact(app):
        app.return_home_page()
        app.contact.edit_first_contact(firstname="Пупкин")
