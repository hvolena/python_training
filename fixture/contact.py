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
