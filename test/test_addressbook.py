# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact

def test_add_contact(app):
        app.contact.init_new_contact()
        app.contact.create_new(Contact(firstname="Petr", middlename="Smirnov"))

def test_add_empty_contact(app):
        app.contact.init_new_contact()
        app.contact.create_new(Contact(firstname="", middlename=""))


