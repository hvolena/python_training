class ContactHelper:

    def __init__(self, app):
        self.app = app

    def init_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create_new(self, contact):
        wd = self.app.wd
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
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
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        # submit edition
        wd.find_element_by_name("update").click()
