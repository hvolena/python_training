
def test_delete_first_contact(app):
    app.return_home_page()
    app.contact.delete_first_contact()
