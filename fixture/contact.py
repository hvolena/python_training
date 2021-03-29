class ContactHelper:

    def __init__(self, app):
        self.app = app

    def init_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create_new(self, contact):
        wd = self.app.wd
        # fill contact form
        self.set_first_name(contact.firstname)
        self.change_field_values("middlename", contact.middlename)
        # submit form
        wd.find_element_by_name("submit").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def edit_first_contact(self, firstname):
        wd = self.app.wd
        # select edit first contact
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # edit form
        self.set_first_name(firstname)
        # submit edition
        wd.find_element_by_name("update").click()

    def set_first_name(self, firstname):
        self.change_field_values("firstname", firstname)

    def change_field_values(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

