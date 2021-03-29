# -*- coding: utf-8 -*-
import pytest

def test_edit_first_group(app):
        app.group.edit_first_group(group_name="Друзья")
